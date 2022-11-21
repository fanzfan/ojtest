import random
from unittest import TestCase

import pyperclip
from ojtest import rand_tree

random.seed(42)


class Test(TestCase):
    def test_rand_tree(self):
        for _ in range(10):
            self.assertEqual(rand_tree(10), pyperclip.paste())

    def test_rand_bst(self):
        for _ in range(10):
            self.assertEqual(rand_tree(4), pyperclip.paste())
