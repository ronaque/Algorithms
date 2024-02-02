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

def int_2_string_32(input_int):
    """
    Converts a 32 bit integer to a string.
    Parameters
    ----------
    input_int: The integer to be converted.

    Returns
    -------
    A string.
    """
    if input_int.bit_length() > 32:
        raise RuntimeError("The input integer is too long to be converted to a 32 bits string")

    result = ""
    for i in range(4):
        int_char = chr(input_int & 0xFF)
        if int_char != '\n':
            result = int_char + result
        # result = chr(input_int & 0xFF) + result
        input_int = input_int >> 8
    return result

def string_2_int_32(input_string):
    """
    Converts a string to a 32 bit integer.
    Parameters
    ----------
    input_string: The string to be converted.

    Returns
    -------
    An integer.
    """
    result = 0
    for c in input_string:
        int_c = ord(c)
        result = (result << 8) + int_c

    if result.bit_length() > 32:
        raise RuntimeError("The input string is too long to be converted to a 32 bits integer")
    return result

def string_2_int_128(input_string):
    """
    Converts a string to a 128 bit integer.
    Parameters
    ----------
    input_string: The string to be converted.

    Returns
    -------
    An integer.
    """
    result = 0
    for c in input_string:
        int_c = ord(c)
        result = (result << 8) + int_c

    if result.bit_length() > 128:
        raise RuntimeError("The input string is too long to be converted to a 128 bits integer")

    return result