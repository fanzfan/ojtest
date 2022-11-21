import collections
from random import random, randint

import pyperclip

# Using random() to judge if the node is null
# when random() > NULL_THRESHOLD, the function will make current node null
NULL_THRESHOLD = 0.8


def rand_tree(max_depth: int,
              min_val=0,
              max_val=20,
              n_ary=2,
              null_possibility=NULL_THRESHOLD) -> str:
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
    tree = [str(randint(min_val, max_val))]

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

                if random() < null_possibility:
                    tree.append(str(randint(min_val, max_val)))
                    n_cnt += 1
                else:
                    tree.append('null')

    s = ', '.join(tree)
    s = '[' + s + ']'
    pyperclip.copy(s)

    return s


def rand_bst(max_depth: int,
             min_val=0,
             max_val=30,
             null_possibility=NULL_THRESHOLD) -> str:
    """Generate a binary search tree consists of UNIQUE random integers.

        Examples:
            rand_bst(4) -> [10, 4, 23, 1, 9, 16, 24, null, 2, 7, null, 13, null, null, 26]

                      (10)
                     /   \
                  (4)     (23)
                 / \       / \
              (1)  (9)   (16) (24)
               \    /     /     \
               (2) (7)  (13)    (26)
    """

    root_val = randint(min_val // 3 * 2 + max_val // 3, min_val // 3 + max_val // 3 * 2)
    queue = collections.deque()
    queue.append([min_val, root_val, max_val])

    tree = [str(queue[0][1])]
    depth = 1

    while depth < max_depth:
        current_size = len(queue)

        for _ in range(current_size):
            node = queue.popleft()

            # left child
            if random() < null_possibility and node[1] - node[0] > 1:
                left_val = randint(node[0] + 1, node[1] - 1)
                tree.append(str(left_val))
                queue.append([node[0], left_val, node[1]])
            else:
                tree.append('null')

            # right child
            if random() < null_possibility and node[2] - node[1] > 1:
                right_val = randint(node[1] + 1, node[2] - 1)
                tree.append(str(right_val))
                queue.append([node[1], right_val, node[2]])
            else:
                tree.append('null')

        depth += 1

    s = ', '.join(tree)
    s = '[' + s + ']'
    pyperclip.copy(s)

    return s
