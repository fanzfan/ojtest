import random
from unittest import TestCase

import pyperclip
from ojtest import (rand_int_list,
                    rand_int_list_unique,
                    rand_int_list_sorted,
                    rand_int_list_sorted_unique)

random.seed(42)


class TestList(TestCase):

    def test_rand_int_list(self):
        self.assertEqual(rand_int_list(100)[1], pyperclip.paste())

    def test_rand_int_list_unique(self):
        self.assertEqual(rand_int_list_unique(100), pyperclip.paste())

    def test_rand_int_list_sorted(self):
        self.assertEqual(rand_int_list_sorted(100), pyperclip.paste())

    def test_rand_int_list_sorted_unique(self):
        self.assertEqual(rand_int_list_sorted_unique(100), pyperclip.paste())
