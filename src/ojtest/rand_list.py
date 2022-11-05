
from random import randint
import pyperclip
from typing import TypeVar, List, Union
from functools import cmp_to_key

INC = cmp_to_key(lambda x, y: x - y)


def rand_int_list(length: int,
                  min_val=0,
                  max_val=100,
                  copy=True) -> List[int]:
    """Generate a list consists of integer values and copy it to the clipboard

        A simple example: 
            rand_int_list(10, 0, 100) -> [32, 74, 60, 33, 31, 84, 64, 43, 63, 34]
    """
    int_list = rand_int_list_generic(length, min_val, max_val)
    s = str(int_list)

    if copy:
        pyperclip.copy(s)

    return int_list


def rand_int_list_unique(length: int,
                         min_val=0,
                         max_val=100,
                         copy=True) -> List[int]:
    """Generate a list consists of UNIQUE integer values and copy it to the clipboard

        A simple example: 
            rand_int_list_unique(10, 0, 100) -> [97, 98, 38, 41, 73, 17, 18, 51, 20, 25]
    """
    int_list_unique = rand_int_list_generic(
        length, min_val, max_val, unique=True)
    s = str(int_list_unique)

    if copy:
        pyperclip.copy(s)

    return int_list_unique


def rand_int_list_sorted(length: int,
                         min_val=0,
                         max_val=100,
                         key=INC,
                         copy=True) -> List[int]:
    """Generate a list consists of SORTED integer values and copy it to the clipboard

        A simple example: 
            rand_int_list_sorted(10, 0, 100) -> [5, 19, 35, 37, 46, 64, 69, 75, 78, 91]
    """

    int_list_sorted = sorted(rand_int_list_generic(
        length, min_val, max_val), key=key)
    s = str(int_list_sorted)

    if copy:
        pyperclip.copy(s)

    return int_list_sorted


def rand_int_list_sorted_unique(length: int,
                                min_val=0,
                                max_val=100,
                                key=INC,
                                copy=True) -> List[int]:
    """Generate a list consists of SORTED AND UNIQUE integer values and copy it to the clipboard

        A simple example: 
            rand_int_list_sorted_unique(10, 0, 100) -> [0, 33, 48, 53, 71, 74, 86, 87, 89, 97]
    """

    int_list_sorted_unique = sorted(rand_int_list_generic(
        length, min_val, max_val, unique=True), key=key)
    s = str(int_list_sorted_unique)

    if copy:
        pyperclip.copy(s)

    return int_list_sorted_unique


def rand_int_list_generic(length: int,
                          min_val: int,
                          max_val: int,
                          unique=False,
                          copy=True) -> List[int]:
    int_list = [randint(min_val, max_val) for i in range(length)]

    if unique:
        int_list = list(set(int_list))

    return int_list
