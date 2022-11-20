from unittest import TestCase

import random
random.seed(42)

import pyperclip
from ojtest import rand_tree

class Test(TestCase):
    def test_rand_tree(self):
        self.assertEqual(rand_tree(10), pyperclip.paste())

    def test_rand_bst(self):
        self.fail()
