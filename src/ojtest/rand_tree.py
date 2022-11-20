import collections
from random import random, randint

import pyperclip

# Using random() to judge if the node is null
# when random() > NULL_THRESHOLD, the function will make current node null
NULL_THRESHOLD = 0.8


def rand_tree(max_depth: int,
              min_val=0,
              max_val=20,
              n_ary=2) -> str:
    """Generate a tree consists of random integers, a binary tree will be provided by default

        Examples:
            rand_tree(4) -> [92, 98, 1, 43, null, 66, 45, null, 35, 48, 94, null, 87]

             (92)
             /  \
         (98)    (1)
         /       /  \
      (43)    (66)  (45)
        \      / \    \
       (35)  (48)(94) (87)

    """
    s = '[' + str(randint(min_val, max_val)) + ', '

    # current depth
    depth = 1

    # nodes count of next layer
    n_cnt = 1

    # BFS
    while depth < max_depth and n_cnt > 0:
        current_size = n_cnt
        depth += 1
        n_cnt = 0

        for _ in range(current_size):

            for _ in range(n_ary):

                if random() < NULL_THRESHOLD:
                    s += str(randint(min_val, max_val)) + ', '
                    n_cnt += 1
                else:
                    s += 'null, '

    s = s[0:-2] + ']'
    pyperclip.copy(s)

    return s


def rand_bst(max_depth: int,
             min_val=0,
             max_val=30,
             n_ary=2) -> str:
    """Generate a BALANCED binary search tree consists of UNIQUE random integers.

        Examples:
            TODO
    """

    # TODO: Choose a way from options below
    # Option 1: Construct a BST from a sorted list, then traverse and get the result list
    # Option 2: Directly generate a list, using the definition of BST : ->
    # (left child node(LCN)'s val is lower, right child node(RCN)'s val is greater)
    # this method need a queue to store 3 parameters [min_val, max_val, node_val]
    # like for a root node (42), min_val = 0, max_val = 100
    # for its LCN, val is randint(0, 42 - 1), let's assume it is 20
    # for RCN, val is randint(42 + 1, 100), assume it is 75
    # then a simple bst is built

    pass
