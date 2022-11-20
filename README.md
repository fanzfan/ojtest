# OjTest - An auto-copied testcase generator for online judges.  

Install  `pip3 install ojtest`   

Requirements :  [PyperClip](https://github.com/asweigart/pyperclip)  
If you find this project helpful, star it!

---

## Function

### 1. generate a random list consists of integer values and copy it to the clipboard
1. rand_int_list
2. rand_int_list_sorted
3. rand_int_list_unique
4. rand_int_list_sorted_unique

### 2. generate a random string and copy it to the clipboard
1. rand_str
2. rand_str_alphabetics
3. rand_str_alphabetic_lower
4. rand_str_alphabetic_capital
5. rand_str_digital

### 3. generate a random tree and copy it to the clipboard
1. rand_tree
---

## Usage

### 1. get a N-ary tree of random integers
```python
import ojtest as oj
import random

random.seed(42)

oj.rand_tree(3)
# or j.rand_tree(3, min_val=0, max_val=20)
# or j.rand_tree(3, min_val=0, max_val=20, n_ary=2)
# [6, 20, 14, 16, null, 19, 3, 20, null, 8, null, 9, 9]
"""
             (6)
             /  \
         (20)    (14)
         /       /  \
      (16)    (19)  (3)
      /       /     / \
    (20)    (8)   (9) (9)
"""
```

---

### 2. get a string consists of customized char sets(string format)
Default char set is alphabets
```python
import ojtest as oj
import random

random.seed(42)

oj.rand_str(50)
# "GiwCkhgoCuKCOySWewyfgUDwPdZHLOQgESkMqVMaLWckpfVcuy"

oj.rand_str(length=50, char_set='QWERTYqwerty987654')
# "9RyyeW74R9E4ryqEWwrEwR9e7yYyyqeEY4wY79e4wtWwWt9eEq"
```

---


### 3. get a string consists of alphabets
```python
import ojtest as oj
import random

random.seed(42)

oj.rand_str_alphabetic(50)
# or oj.rand_str_alphabetic(length=50)
# or oj.rand_str(50)
# "GiwCkhgoCuKCOySWewyfgUDwPdZHLOQgESkMqVMaLWckpfVcuy"
```

---

### 4. get a list consists of random integer values  
By default, min value is 0, and max value is 100
```python
import ojtest as oj
import random

random.seed(42)

oj.rand_int_list(10, 0, 100)
# or oj.rand_int_list(10)  # default min_val = 0, max_val = 100
# or oj.rand_int_list(length=10, min_val=0, max_val=100)
# [81, 14, 3, 94, 35, 31, 28, 17, 94, 13]
```

---
### 5. get a list consists of sorted random integer values  
By default, min value is 0, and max value is 100
```python
import ojtest as oj
import random

random.seed(42)

oj.rand_int_list_sorted(10, 0, 100)
# or oj.rand_int_list_sorted(10)
# or oj.rand_int_list_sorted(length=10, min_val=0, max_val=100)
# [3, 13, 14, 17, 28, 31, 35, 81, 94, 94]
```

---
### 6. get a list consists of customized sorted random integer values  
By default, min value is 0, and max value is 100
```python
import ojtest as oj
from functools import cmp_to_key
import random

random.seed(42)

# decreasing sort
key = cmp_to_key(lambda x, y: y - x)
oj.rand_int_list_sorted(10, 0, 100, key = key)
# oj.rand_int_list_sorted(length=10, min_val=0, max_val=100, key = cmp_to_key(lambda x, y: y - x))
# [94, 94, 81, 35, 31, 28, 17, 14, 13, 3]
```

