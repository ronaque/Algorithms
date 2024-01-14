import ctypes as ct

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
    return (((x) << (y&(w-1))) | ((x) >> (w - (y&(w-1)))))

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
    return (((x) >> (y&(w-1))) | ((x) << (w - (y&(w-1)))))

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
    # Initialize L
    while i != -1:
        L[i // u] = ct.c_uint32((L[i // u] << 8) + key[i]).value
        i -= 1

    # Initialize S
    S[0] = p
    i = 1
    while i < t:
        S[i] = ct.c_uint32(S[i-1] + q).value
        i += 1

    # Mix L into S
    A = B = i = j = key = 0
    while key < t*3:
        A = S[i] = ct.c_uint32(left_rotate(S[i] + (A + B), 3)).value
        B = L[j] = ct.c_uint32(left_rotate(L[j] + (A + B), (A + B))).value
        key += 1
        i = (i + 1) % t
        j = (j + 1) % c


def test():
    key = [0x01, 0x23, 0x45, 0x67,
           0x89, 0xab, 0xcd, 0xef,
           0xfe, 0xdc, 0xba, 0x98,
           0x76, 0x54, 0x32, 0x10]
    print(f"Key: {key}, len: {len(key)}, S: {S}")
    rc5_setup(key)
    print(S)


