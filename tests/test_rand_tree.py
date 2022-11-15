from unittest import TestCase

import random
random.seed(42)

import pyperclip
from src.ojtest import(rand_tree,
                       )

class Test(TestCase):
    def test_rand_tree(self):
        self.assertEqual(rand_tree(), pyperclip.paste())

    def test_rand_bst(self):
        self.assertEqual(rand_tree(), pyperclip.paste())
