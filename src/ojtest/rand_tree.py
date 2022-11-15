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
            rand_tree(3) -> [92, 98, 1, 43, null, 66, 45, null, 35, 48, 94, null, 87]
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


def rand_bst(num_of_elements: int,
             min_val=0,
             max_val=20,
             n_ary=2) -> str:
    """Generate a BALANCED binary search tree consists of UNIQUE random integers.

        Examples:
            rand_tree(3) -> [92, 98, 1, 43, null, 66, 45, null, 35, 48, 94, null, 87]
    """
    pass
