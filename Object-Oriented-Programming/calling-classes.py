class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

# Instance method 
#--------------------------------------------------------
obj = MyClass()
print(obj.method()) # calling instance via self argument 
print(MyClass.method (obj)) # is the same thing as obj.method() - just passing instance object manually

# Acess class itself via instance method 
#obj. __class__attribute 

# Class method 
print(obj.classmethod()) # doesn't have access to instance object but only to the class object 

# Static method 
print(obj.staticmethod()) #can't access class or instance. Work as regular functions but are within class space. 


# Call method without an instance 
#---------------------------------------------------------
print(MyClass.classmethod())

print(MyClass.staticmethod())

# print(MyClass.method())   #-- This doesn't work, because instance was not created first 

#---------------------------------------------------------
# Pizza example class: 
#---------------------------------------------------------
# Simple Pizza class 
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients 

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

Pizza(['cheese','tomatoes'])
Pizza(['mozzarella', 'tomatoes'])
Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms'])
Pizza(['mozzarella'] * 4)

# Use @classmethod 
# Combine these different ingredients into different types of pizzas 
# use cls arguement under classmethod. This way if you decide to update the name, you don't have to worry about input arguments
class Pizza_combination:
    def __init__(self, ingredients):
        self.ingredients = ingredients 

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella','tomatoes'])

    @classmethod 
    def proscuitto(cls):
        return cls(['mozarella','tomatoes','ham'])

print(Pizza_combination.margherita())
print(Pizza_combination.proscuitto())

# Use Static Method 
import math 

class Pizza_rad:
    def __init__(self, radius, ingredients):
        self.radius = radius 
        self.ingredients = ingredients 

    def __repr__(self):
        return (f'Pizza_rad({self.radius!r},'f'{self.ingredients!r})')

    def area(self):
        return self._circle_area(self.radius)

    # instead of calculating area under the function called area, call static method and calculate it separately
    @staticmethod
    def _circle_area(r):   #the underscore in front of the function name signals that this is internal function
        return r**2 * math.pi

p = Pizza_rad(4,['mozarella','tomatoes'])
print(p)
print(p.area())
print(Pizza_rad._circle_area(4))
print(Pizza_rad(4,['cheese']).area())

'''
KEY TAKEAWAYS

1. Instance methods need a class instance and can access the instance through self.
2. Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
3. Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.
4. Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.
'''

