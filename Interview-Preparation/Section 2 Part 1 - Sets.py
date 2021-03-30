def count_unique(s):
    '''
    Count number of unique characters in s
    >>> count_unique("aabb")
    2
    >>> count_unique("abcdef")
    6
    '''
    # seen_c = [] # O(1)
    # # # 0 + 1 + 2 + 3 + 4 + ... + n - 1 ~= n^2
    # for c in s: # O(n)
    #     if c not in seen_c: # O(n)
    #         seen_c.append(c) # O(1)
    # return len(seen_c) # O(n^2)

    # seen_c = set() # O(1)
    # for c in s: # O(n)
    #     if c not in seen_c: # O(1)
    #         seen_c.add(c) # O(1)
    # return len(seen_c) # O(n)

    # return len({c for c in s}) # O(n)

    # return len(set(s))  # O(n)


g = (i for i in range(6))
# print(next(g))

print(sum([i for i in range(1,1001)]))

print(sum((i for i in range(1,1001))))

iterator = iter((i for i in range(1,1001)))

print(next(iterator))

iterator_list = iter([i for i in range(1,1001)])

print(next(iterator_list))

lst = [i for i in range(1,1001)]

import sys
print(sys.getsizeof(lst))

gen = (i for i in range(1,1001))
print(sys.getsizeof(g))

def f():
    yield 1
    yield 2
    yield 3

g1 = f()

print(next(g1))
print(next(g1))
print(next(g1))