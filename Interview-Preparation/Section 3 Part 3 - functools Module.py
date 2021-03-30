
# from functools import cached_property
# from functools import lru_cache


# @lru_cache(maxsize=256)
# def fib(n):
#     '''
#      0, 1, 1, 2, 3, 5, 8
#     '''
#     print(n)
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)


# class Data:
#     def __init__(self, n):
#         self.n = n

#     @property
#     def f(self):
#         total = 0
#         for i in range(self.n):
#             for j in range(self.n):
#                 for k in range(self.n):
#                     total += i + j + k
#         return total

print(ord('A'))

print('HELLO WORLD'.isupper())
print('HELLO WORLD'.islower())

import string

print(string.ascii_uppercase)

def is_upper(s):
    for letter in s:  
        if letter not in string.ascii_uppercase:
            return False
    return True

uppercase_set = set(string.ascii_uppercase)

print(is_upper('HELLO WORLD'))

def is_upper_using_set(s):
    for letter in s:  
        if letter not in uppercase_set:
            return False
    return True

# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit(is_upper('HELLO WORLD')))
#     print(timeit.timeit(is_upper_using_set('HELLO WORLD')))

def is_upper_cleaner(s):
    return all(letter in uppercase_set for letter in s)

print(is_upper_cleaner('HELLO WORLD'))

whitespace_set = set(string.whitespace)

print(''.join(letter for letter in "HELLO WORLD" if letter not in whitespace_set))

import iteritools as it



