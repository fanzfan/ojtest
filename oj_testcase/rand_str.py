
from random import randint
import pyperclip
from functools import cmp_to_key

ALPHABETS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rand_str_alphabetic_lower(length: int,
                              copy=True) -> str:
    """Generate a string consists of lower alphabetics and copy it to the clipboard

        A simple example: 
            rand_str_alphabetic_lower(10) -> "firhykkfkv"
    """
    return rand_str_alphabetic_generic('lower', length, copy)


def rand_str_alphabetic_capital(length: int,
                                copy=True) -> str:
    """Generate a string consists of capital alphabetics and copy it to the clipboard

        A simple example: 
            rand_str_alphabetic_capital(10) -> "MKONCZHFOU"
    """
    return rand_str_alphabetic_generic('capital', length, copy)


def rand_str_alphabetic(length: int,
                        copy=True) -> str:
    """Generate a string consists of alphabetics and copy it to the clipboard

        A simple example: 
            rand_str_alphabetic(10) -> "TITVqaehLo"
    """
    return rand_str_alphabetic_generic('mixed', length, copy)


def rand_str_alphabetic_generic(method: str,
                                length: int,
                                copy=True) -> str:

    if method == 'lower':
        start, end = 0, 25
    elif method == 'capital':
        start, end = 26, 51
    else:
        start, end = 0, 51

    s = [ALPHABETS[randint(start, end)] for i in range(length)]
    s = '"' + ''.join(s) + '"'

    if copy:
        pyperclip.copy(s)

    return s


def rand_str_digital(length: int,
                     radix=10,
                     copy=True) -> str:

    """Generate a string consists of digits and copy it to the clipboard

        A simple example: 
            rand_str_digital(10) -> "1460269723"
    """
    if radix > 36:
        pass
    start, end = 0, radix - 1
    s = [DIGITS[randint(start, end)] for i in range(length)]
    s = '"' + ''.join(s) + '"'

    if copy:
        pyperclip.copy(s)

    return s
