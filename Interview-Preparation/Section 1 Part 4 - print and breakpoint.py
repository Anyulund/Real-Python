'''
def max1(lst):
    max_num = 0
    for num in lst:
        if num > max_num:s
            max_num =num
    return num 

print(max1([1, -2, 4]))
'''
def max(lst):
    max_num = -float('inf')
    for num in lst:
        #breakpoint()
        if num > max_num:
            max_num = num
    return max_num


print(max([-1, -2, -4]))

# breakpoint() works only for versions of python 3.7 or higher
# in python before that you do:
# import pdb;pdb.set_trace()
'''
lst = [1,2,-5,4]

def square(x):
    return x*x

map(square, lst) #gives <map at address>

# This will give you a list of squared values
# It basically maps the function on the list of input values
# And gives you a list of the output values

list(map(square, lst))

for num in lst:
    result.append(square(num))

[square(num) for num in lst]

'''

'''
lst = [1,2,-5,4]

def is_odd(x):
    return x % 2 == 1

print(list(filter(is_odd, lst)))

print([num for num in lst if is_odd(num)])

#grid = [[0. 0, 0],[0, 0, 0]]

num_rows = 2
num_cols = 3

grid = []

for _ in range(num_rows):
    curr_row = []
    for _ in range(num_cols):
        curr_row.append(0)
    grid.append(curr_row)
print(grid)

grid = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
print(grid)

#print(max((lst, lambda x: x * x))) #debug later

print(any([(lambda x: x % 2 == 1)(num) for num in lst]))

print(all([(lambda x: x % 2 == 1)(num) for num in lst]))
'''

class A(object):
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def __repr__(self):
        return f"""
            My name is {self.name}.
            I am {self.age} years old
            """
name = 'Bob'
age = 40
#print(A(name, age))

animals = ['cat', 'dog', 'cheetah','rhino']

print(sorted(animals))
print(sorted(animals, reverse= True))

animalsdict = [\
    {'type': 'cat', 'name': 'Stephanie', 'age': 8},\
        {'type': 'dog', 'name': 'Devon', 'age': 3},\
            {'type': 'rhino', 'name':'Moe','age':5}]

print(sorted(animalsdict, key=lambda animal: animal['age'], reverse=True))

print(animalsdict.sort(key=lambda animal: animal['age']))
print(animalsdict)