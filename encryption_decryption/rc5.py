import ctypes as ct

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

def to_byte(num):
    """
    Converts a number to a byte.
    Parameters
    ----------
    num: The number to be converted.

    Returns
    -------
    A byte.
    """
    return num & 0xFF

def to_four_bytes(num):
    """
    Converts a number to a 4 bytes array.
    Parameters
    ----------
    num: The number to be converted.

    Returns
    -------
    A 4 bytes array.
    """
    return num & 0xFFFFFFFF

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
    print("Initializing Encryption")
    A = to_four_bytes(input[0] + S[0])
    B = to_four_bytes(input[1] + S[1])

    i = 1
    while i <= r:
        A = to_four_bytes((left_rotate(A ^ B, B)) + S[2*i])
        B = to_four_bytes((left_rotate(B ^ A, A)) + S[2*i+1])
        i += 1

    output[0] = A
    output[1] = B
    print(f"End of Encryption")

def rc5_decrypt(input, output):
    """

    Parameters
    ----------
    input
    output

    Returns
    -------

    """
    print("\nInitializing Decryption")
    A = to_four_bytes(input[0])
    B = to_four_bytes(input[1])

    i = r
    while i > 0:
        B = (right_rotate(ct.c_uint32(B - S[2*i+1]).value, A)) ^ A
        A = right_rotate(ct.c_uint32(A - S[2*i]).value, B) ^ B
        i -= 1

    output[0] = A - S[0]
    output[1] = B - S[1]
    print(f"End of Decryption")

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

def entry_to_word():
    num = input("Which Hexadecimal number would you like to convert to decimal/denary?  \n")
    num_split = num.split(" ")
    hex_nums = []
    for i in num_split:
        try:
            hex_nums.append(int(i, 16))
        except ValueError:
            print("I/ You did not enter a hexadecimal number!")

    return hex_nums

@timer
def rc5_encryption_algorithm():
    """
    This Algorithm will encrypt a 64 bits Word, and should decrypt it back to the original word.
    It is a Symetric block cipher algorithm, that uses a 128 bits key for encryption and decryption.
    Based on the article "The RC5 Encryption Algorithm" by Ronald L. Rivest, 1994.
    It works by creating a key expansion table S with t words of w bit,
    that will be used to encrypt and decrypt the input word.
    """
    key = [0x00] * b

    in1 = [0 , 0]
    in2 = [0 , 0]
    out = [0 , 0]

    i = 1
    while i < 6:
        print("\nStarting iteration")
        in1[0] = out[0]
        in1[1] = out[1]
        j = 0
        while j < b:
            key[j] = to_byte(out[0] % (255 - j))
            j +=1

        rc5_setup(key)
        rc5_encrypt(in1, out)
        print("key: ", end="")
        for k in key:
            print(f'{k:02x}', sep=" ", end=" ")
        print(f"\nPlaintext: {in1[0]:08X} {in1[1]:08X} --> Ciphertext: {out[0]:08X} {out[1]:08X}")
        rc5_decrypt(out, in2)
        print(f"Ciphertext: {out[0]:08X} {out[1]:08X} --> Plaintext: {in2[0]:08X} {in2[1]:08X}")

        i += 1

