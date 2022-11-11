# OjTest - An auto-copied testcase generator for online judges.  

Install  `pip3 install ojtest`  
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

---

## Usage

### 1. get a string consists of customized char sets(string format)
Default char set is alphabets
```python
import ojtest as oj

oj.rand_str(50)
# "JrtnUhQmUDZTunRTHYIbZyDGNemOYrArXrTIABczpbiurISfaR"

oj.rand_str(length=50, char_set='QWERTYqwerty987654')
# "Rte68ryYeR68e7T87T9Y5tetY687Rr7Tr5t5TWQE684TrQ45Wq"
```

---

### 2. get a string consists of alphabets
```python
import ojtest as oj

oj.rand_str_alphabetic(50)
# or oj.rand_str_alphabetic(length=50)
# or oj.rand_str(50)
# "UfAdzVUbzTxsVvLzOIgjPoMULRymXynTceMdqaxeQFLASxWCEn"
```

---

### 3. get a list consists of random integer values  
By default, min value is 0, and max value is 100
```python
import ojtest as oj

oj.rand_int_list(10, 0, 100)
# or oj.rand_int_list(10)  # default min_val = 0, max_val = 100
# or oj.rand_int_list(length=10, min_val=0, max_val=100)
# [32, 74, 60, 33, 31, 84, 64, 43, 63, 34]
```

---
### 4. get a list consists of sorted random integer values  
By default, min value is 0, and max value is 100
```python
import ojtest as oj

oj.rand_int_list_sorted(10, 0, 100)
# or oj.rand_int_list_sorted(10)
# or oj.rand_int_list_sorted(length=10, min_val=0, max_val=100)
# [5, 19, 35, 37, 46, 64, 69, 75, 78, 91]
```
---
### 5. get a list consists of customized sorted random integer values  
By default, min value is 0, and max value is 100
```python
import ojtest as oj
from functools import cmp_to_key

# decreasing sort
key = cmp_to_key(lambda x, y: y - x)
oj.rand_int_list_sorted(10, 0, 100, key = key)
# oj.rand_int_list_sorted(length=10, min_val=0, max_val=100, key = cmp_to_key(lambda x, y: y - x))
# [88, 67, 53, 49, 22, 21, 20, 18, 4, 3]
```

