# OjTest - A testcase generator for online judges.  

Install  `pip3 install oj_testcase`  
If you find this project helpful, star it!

---

## Functions

### 1. generate a random list consists of integer values
1. rand_int_list
2. rand_int_list_sorted
3. rand_int_list_unique
4. rand_int_list_sorted_unique

### 2. generate a random string
1. rand_str_alphabetic
2. rand_str_alphabetic_lower
3. rand_str_alphabetic_capital
4. rand_str_digital

---

## Usage

### 1. get a string consists of alphabets
```python
import ojtest as oj

oj.rand_str_alphabetic(50)
# "UfAdzVUbzTxsVvLzOIgjPoMULRymXynTceMdqaxeQFLASxWCEn"
```

---
### 2. get a list consists of random integer values  

```python
import ojtest as oj

oj.rand_int_list(0, 100, 10)
# [32, 74, 60, 33, 31, 84, 64, 43, 63, 34]
```

---
### 3. get a list consists of sorted random integer values  
```python
import ojtest as oj

oj.rand_int_list_sorted(0, 100, 10)
# [5, 19, 35, 37, 46, 64, 69, 75, 78, 91]
```
