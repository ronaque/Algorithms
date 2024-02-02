import ctypes as ct
from math import ceil

from utils.conversions import string_2_int_32, string_2_int_128, to_four_bytes, to_byte, int_2_string_32
from utils.decorator import timer

w = 32 # Word Size
r = 12 # Number of Rounds
b = 16 # Number o bytes in key (16 = 128 bits)
c = 4 # Number of words in key = ceil(8*b/w)
t = 2*(r+1) # Size of table S = 2*(r+1) = 26 words
S = [0]*t # Expanded key table

# Magic constants
p = 0x0b7e15163
q = 0x9e3779b9

def left_rotate(x, y):
    """
    Executes a Left Rotation Operation in X.
    The number of bits to rotate is setby the variable w, which is a pre-set
    word size of a word used in the algorithm.
    Parameters
    ----------
    x: Unsigned int of 32 bits to be rotate.
    y: y bits to rotate.

    Returns
    -------

    """
    return to_four_bytes((x << (y & (w - 1)))) | to_four_bytes((x >> (w - (y & (w - 1)))))

def right_rotate(x, y):
    """
    Executes a Right Rotation Operation in X.
    The number of bits to rotate is setby the variable w, which is a pre-set
    word size of a word used in the algorithm.
    Parameters
    ----------
    x: Unsigned int of 32 bits to be rotate.
    y: y bits to rotate.

    Returns
    -------

    """
    return to_four_bytes((x >> (y & (w - 1)))) | to_four_bytes((x << (w - (y & (w - 1)))))

def rc5_encrypt(input, output):
    """
    This function will encrypt a 64 bits Word (input) into another 64 bits Word (output).
    The input will be organized in two 32 bits words, A and B, that after encryption with ther key expansion Table S,
    will be organized in the output in the same way.
    This must be done after the key expansion setup.
    Parameters
    ----------
    input
    output

    Returns
    -------

    """
    A = to_four_bytes(input[0] + S[0])
    B = to_four_bytes(input[1] + S[1])

    i = 1
    while i <= r:
        A = to_four_bytes((left_rotate(A ^ B, B)) + S[2*i])
        B = to_four_bytes((left_rotate(B ^ A, A)) + S[2*i+1])
        i += 1

    output[0] = A
    output[1] = B

def rc5_decrypt(input, output):
    """

    Parameters
    ----------
    input
    output

    Returns
    -------

    """
    A = to_four_bytes(input[0])
    B = to_four_bytes(input[1])

    i = r
    while i > 0:
        B = (right_rotate(ct.c_uint32(B - S[2*i+1]).value, A)) ^ A
        A = right_rotate(ct.c_uint32(A - S[2*i]).value, B) ^ B
        i -= 1

    output[0] = ct.c_uint32(A - S[0]).value
    output[1] = ct.c_uint32(B - S[1]).value

def rc5_setup(key):
    """
    R5 algorithm setup, that will make the key expansion to a key array S.
    Parameters
    ----------
    key: The secret key

    Returns
    -------

    """
    u = w//8
    L = [0] * c
    i = b - 1
    # Initialize L: convert the key from bytes to words
    while i != -1:
        L[i // u] = to_four_bytes((L[i // u] << 8) + key[i])
        i -= 1

    # Initialize S using the p and q magic constants
    S[0] = p
    i = 1
    while i < t:
        S[i] = to_four_bytes((S[i-1] + q))
        i += 1

    # Mix L into S
    i = 0
    j = 0
    k = 0
    A = 0
    B = 0
    while k < t*3:
        A = S[i] = to_four_bytes(left_rotate(to_four_bytes(S[i] + to_four_bytes((A + B))), 3))
        B = L[j] = to_four_bytes(left_rotate(to_four_bytes(to_four_bytes(L[j]) + to_four_bytes((A + B))), to_four_bytes((A + B))))
        k += 1
        i = (i + 1) % t
        j = (j + 1) % c

def rc5_entry():
    input_word = input("Enter the 64 bits (8 characters) word to be encrypted: ")
    if len(input_word) < 8:
        raise RuntimeError("The input word must have at least 8 characters")
    key_word = input("Enter the 128 bits key (16 characters) to be used in the encryption: ")
    if len(key_word) != 16:
        raise RuntimeError("The key word must have 16 characters")

    input_parameter = [string_2_int_32(input_word[0:4]), string_2_int_32(input_word[4:8])]
    key_parameter = string_2_int_128(key_word)

    print(f"Initializing encryption of {input_word} with key {key_word}")
    rc5_encryption_algorithm(input_parameter, key_parameter)

@timer
def rc5_encryption_algorithm(input_word, key_word):
    """
    This Algorithm will encrypt a 64 bits Word, and should decrypt it back to the original word.
    It is a Symetric block cipher algorithm, that uses a 128 bits key for encryption and decryption.
    Based on the article "The RC5 Encryption Algorithm" by Ronald L. Rivest, 1994.
    It works by creating a key expansion table S with t words of w bit,
    that will be used to encrypt and decrypt the input word.

    Parameters
    ----------
    input_word: The 64 bits word to be encrypted
    key_word: The 128 bits key to be used in the encryption
    """
    key = [0x00] * b

    output_word = [0 , 0]
    middle_word = [0 , 0]

    j = 0
    while j < b:
        key[j] = to_byte(key_word % (255 - j))
        j +=1

    rc5_setup(key)
    rc5_encrypt(input_word, middle_word)
    print(f"\nPlaintext: {input_word[0]:08X} {input_word[1]:08X} --> Ciphertext: {middle_word[0]:08X} {middle_word[1]:08X}")
    print(f"Plaintext: {int_2_string_32(input_word[0])}{int_2_string_32(input_word[1])} --> Ciphertext: {int_2_string_32(middle_word[0])}{int_2_string_32(middle_word[1])}")


    rc5_decrypt(middle_word, output_word)
    print(f"Ciphertext: {middle_word[0]:08X} {middle_word[1]:08X} --> Plaintext: {output_word[0]:08X} {output_word[1]:08X}")
    print(f"Ciphertext: {int_2_string_32(middle_word[0])}{int_2_string_32(middle_word[1])} --> Plaintext: {int_2_string_32(output_word[0])}{int_2_string_32(output_word[1])}")

    return middle_word, output_word