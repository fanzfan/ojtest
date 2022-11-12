import random
from unittest import TestCase
import pyperclip

from ojtest import (rand_str,
                    rand_str_alphabetic_lower,
                    rand_str_alphabetic_capital,
                    rand_str_alphabetic,
                    rand_str_digital)

random.seed(42)


class TestStr(TestCase):

    def test_rand_str(self):
        self.assertEqual(rand_str(100), pyperclip.paste())

    def test_rand_str_alphabetic_lower(self):
        self.assertEqual(rand_str_alphabetic_lower(100), pyperclip.paste())

    def test_rand_str_alphabetic_capital(self):
        self.assertEqual(rand_str_alphabetic_capital(100), pyperclip.paste())

    def test_rand_str_alphabetic(self):
        self.assertEqual(rand_str_alphabetic(100), pyperclip.paste())

    def test_rand_str_digital(self):
        self.assertEqual(rand_str_digital(100), pyperclip.paste())
