from random import choice as rand_choice

import pyperclip

LOWER = "qwertyuiopasdfghjklzxcvbnm"
CAPITAL = "QWERTYUIOPASDFGHJKLZXCVBNM"
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rand_str(length: int,
             char_set=LOWER + CAPITAL,
             copy=True):
    """Generate a string consists of lower alphabetics and copy it to the clipboard

        Examples:
            rand_str(15)                            -> "FzCVCBfGRMbENBV"
            rand_str(15, char_st="?~abcdABCD1234")  -> "?a4c4?2D2b3AAB~"
    """
    return rand_str_generic(length, char_set, copy)


def rand_str_alphabetic_lower(length: int,
                              copy=True) -> str:
    """Generate a string consists of lower alphabetics and copy it to the clipboard

        Examples:
            rand_str_alphabetic_lower(10) -> "firhykkfkv"
    """
    return rand_str_generic(length, LOWER, copy)


def rand_str_alphabetic_capital(length: int,
                                copy=True) -> str:
    """Generate a string consists of capital alphabetics and copy it to the clipboard

        Examples:
            rand_str_alphabetic_capital(10) -> "MKONCZHFOU"
    """
    return rand_str_generic(length, CAPITAL, copy)


def rand_str_alphabetic(length: int,
                        copy=True) -> str:
    """Generate a string consists of alphabetics and copy it to the clipboard

        Examples:
            rand_str_alphabetic(10) -> "TITVqaehLo"
    """
    return rand_str_generic(length, LOWER + CAPITAL, copy)


def rand_str_digital(length: int,
                     radix=10,
                     copy=True) -> str:
    """Generate a string consists of digits and copy it to the clipboard

        Examples:
            rand_str_digital(10)     -> "1460269723"
            rand_str_digital(10, 16) -> "A6C39DB855"
    """

    char_set = DIGITS[:radix]
    return rand_str_generic(length, char_set, copy)


def rand_str_generic(length: int,
                     char_set: str,
                     copy=True) -> str:
    s = [rand_choice(char_set) for _ in range(length)]
    s = '"' + ''.join(s) + '"'

    if copy:
        pyperclip.copy(s)

    return s
