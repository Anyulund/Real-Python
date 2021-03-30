import sys
print(sys.version)

errno = 50159747054
name = 'Bob'


# Old way to format strings 
print('Hello, %s' % name)
print('%x' % errno)
print('Hey %s, there is a 0x%x error!' % (name, errno))
print('Hey %(name)s, there is a 0x%(errno)x error!' %{'name':name, 'errno':errno})

# New Style
print('Hello, {}'.format(name))
print('Hey, there is a 0x{errno:x} error!'.format(name=name, errno=errno))

# Sring interpolation  f-strings
print(f"Hello, {name}!")

a = 5
b = 10
print(f"Five plus ten is {a + b} and not {2 * (a + b)}.")

def greet(name, question):
    return f"Hello, {name}! How's it {question}?"

print(greet('Bob', 'going'))

def greet2(name, question):
    return "Hello, "+ name + "! How's it" + question + "?"

import dis 
dis.dis(greet)
dis.dis(greet2)

print(f"Hey {name}, there is a {errno:#x} error!")

# Template Strings (Standard Library)

from string import Template 
t = Template('Hey, $name!')
print(t.substitute(name=name))

temp1_string = "Hey $name, there is a $error error!"
print(Template(temp1_string).substitute(name=name, error=hex(errno)))

# Exploring vulnerability of formatted strings used by user. 
# In this case it is better use template strings instead. 


#This is our super secret key: 
SECRET = 'this-is-a-secret'


class Error:
    def __init__(self):
        pass

# A malicious user can craft a format string that can read
# data from the global namespace:
user_input = '{error.__init__.__globals__[SECRET]}'

# This allows them to exfiltrate sensitive information
# like a secret key:

err = Error()
print(user_input.format(error=err))
'''
#Safer choice:
user_input1 = '${error.__init__.__globals__[SECRET]}'
print(Template(user_input1).substitute(error=err))
'''



