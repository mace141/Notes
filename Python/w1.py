# [[[[[[[[[[[[[[[[[[[[[[[[[ Differences with JavaScript ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= Whitespace-aware =========================

# Python uses a colon and whitespace to indicate a code block

if (False):
  print('Hello world')

# ========================= Declaring Functions =========================

def sayHello():
  print('Hello')

# ========================= Semicolons =========================

# Python does not need semicolons
# Putting more than 1 statement on a line is bad form
  # print('first'); print('second');

# ========================= Logical Operators =========================

# Python was designed to be readable, hence the operators are `and`, `or`, and `not`

if ((False and False) or not True):
  print('Hello world')

# ========================= Math Operators =========================

# // is used for integer division
  # 10 // 3 ==> 3

# The rest is the same
  # Addition with +
  # Subtraction with -
  # Multiplication with *
  # Division with /
  # Mod (remainder) with %

# [[[[[[[[[[[[[[[[[[[[[[[[[ Number Data Types ]]]]]]]]]]]]]]]]]]]]]]]]]

# Integers

print(3)        # => 3
print(int())    # => 0

# Floating point numbers

print(2.2)      # => 2.2
print(float())  # => 0.0
print(27e-5)    # => 0.00027

# Complex numbers
#     Numbers that consist of a real part and an imaginary part

print(7j)           # => 7j
print(5.1 + 7.7j)   # => (5.1+7.7j)
print(complex(3,5)) # => (3+5j)
print(complex(17))  # => (17+0j)
print(complex())    # => 0j

# Integers will have unlimited precision, where as floating point numbers 
#   eventually run out of memory

# [[[[[[[[[[[[[[[[[[[[[[[[[ String Data Type ]]]]]]]]]]]]]]]]]]]]]]]]]

# Python allows multi-line strings with triple single quotes
# Triple double quotes are used for comments

print(len('hello')) # => 5

# ========================= Indexing =========================

# Indexing out of range will throw an error but slicing out of range will not

# print("Spaghetti"[15])    # => IndexError: string index out of range
print("Spaghetti"[1:4])   # => pag
print("Spaghetti"[4:-1])  # => hett
print("Spaghetti"[4:4])   # => (empty string)

# ========================= Functions =========================

# index()

print("Spaghetti".index('het'))   # => 4
# print("Spaghetti".index('spa'))   # => ValueError: substring not found

# count()

print("Spaghetti".count('t'))     # => 2

#     Value	             Method	                Result
# s = "Hello"	        s.upper()	                "HELLO"
# s = "Hello"	        s.lower()	                "hello"
# s = "Hello"	        s.islower()	               False
# s = "hello"	        s.islower()	               True
# s = "Hello"	        s.isupper()	               False
# s = "HELLO"	        s.isupper()	               True
# s = "Hello"	        s.startswith("He")    	   True
# s = "Hello"	        s.endswith("lo")	         True
# s = "Hello World"	  s.split()	            ["Hello", "World"]
# s = "i-am-a-dog"	  s.split("-")	        ["i", "am", "a", "dog"]
# s = "--"            s.join(['a', 'b'])        'a--b'

# Method	      Purpose
# isalpha()	    returns True if the string consists only of letters and is not blank.
# isalnum()	    returns True if the string consists only of letters and numbers and is not blank.
# isdecimal()	  returns True if the string consists only of numeric characters and is not blank.
# isspace()	    returns True if the string consists only of spaces, tabs, and newlines and is not blank.
# istitle()	    returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

# ========================= Concatenation =========================

print('gold' + 'fish')    # => 'goldfish
print('s' * 5)            # => 'sssss'

# ========================= Formatting =========================

first_name = 'Daniel'
last_name = 'Wu'
print("My name is {0} {1}".format(first_name, last_name))

print(f'My name is {first_name} {last_name}')

# [[[[[[[[[[[[[[[[[[[[[[[[[ Boolean Data Type ]]]]]]]]]]]]]]]]]]]]]]]]]

# Falsey values are
#     None or False
#     Zero of any numeric type
#     Any empty sequences or collections
#         String: ''
#         List: []
#         Tuple: ()
#         Dictionary: {}
#         set()
#         range(0)

# Everything else is truthy

# [[[[[[[[[[[[[[[[[[[[[[[[[ Comparison Operators ]]]]]]]]]]]]]]]]]]]]]]]]]

# In Python, equality operators are process from left to right before the logical
#   operators. 
# Then the logical operators are process in this order: not, and, or

# ========================= Short-Circuit Execution =========================

# Python will stop processing the right side of the logical operator if the left
#   has a definitive True or False

# False and ...
# True or ...

# [[[[[[[[[[[[[[[[[[[[[[[[[ Identity vs. Equality ]]]]]]]]]]]]]]]]]]]]]]]]]

print (2 == 2.0)    # => True
print (2 is 2.0)    # => False

# is -> identity operator
# == -> equality operator

# [[[[[[[[[[[[[[[[[[[[[[[[[ While Statements ]]]]]]]]]]]]]]]]]]]]]]]]]

count = 0
while True:
  print(count)
  count += 1
  if count < 5:
    continue
  break

# `pass` simply does nothing, while `continue` will skip to next iteration
# `break` will exit the loop

# [[[[[[[[[[[[[[[[[[[[[[[[[ Handling Exceptions ]]]]]]]]]]]]]]]]]]]]]]]]]

# The `except` block will only run if there is an issue with the `try` block
try:
  print('hello')
except:
  print('fail')

# To catch a specific error, you can specify it with the except statement
a = 100
# b = "5"
try:
  print(a / b)
except ZeroDivisionError:
  pass
except (TypeError, NameError) as e:
  print("ERROR!", e)

# To run code after successful `try` block you can use an `else` block
# To perform cleanup regardless of success or fail, you can use a `finally` block
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Result is", result)
    finally:
        print("Finally...")

# hasattr() can be used to check the existence of a property or method
a = 321
if hasattr(a, '__len__'):
  print('hello')

# [[[[[[[[[[[[[[[[[[[[[[[[[ Lambda Function ]]]]]]]]]]]]]]]]]]]]]]]]]

# Lambda functions are anonymous functions that are meant to be one-liners
to_upper = lambda s: s.upper()

# [[[[[[[[[[[[[[[[[[[[[[[[[ Formatting printing ]]]]]]]]]]]]]]]]]]]]]]]]]

# Python has a very powerful formatting engine for making exactly the strings you 
# need. The format function is one way to apply these options. Like join, format 
# is applied to strings.

# Comma as thousands separator
print('{:,}'.format(1234567890))
# '1,234,567,890'

# Date and Time
from datetime import datetime
d = datetime(2020, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))
# '2020-07-04 12:15:58'

# Percentage
points = 190
total = 220
print('Correct answers: {:.2%}'.format(points/total))
# 'Correct answers: 86.36%'

# Data Table
width=8
print(' decimal      hex   binary')
print('-'*27)
for num in range(1,16):
    for base in 'dXb':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()
#  decimal      hex   binary
# ---------------------------
#        1        1        1
#        2        2       10
#        3        3       11
#        4        4      100
#        5        5      101
#        6        6      110
#        7        7      111
#        8        8     1000
#        9        9     1001
#       10        A     1010
#       11        B     1011
#       12        C     1100
#       13        D     1101
#       14        E     1110
#       15        F     1111

# [[[[[[[[[[[[[[[[[[[[[[[[[ User Input ]]]]]]]]]]]]]]]]]]]]]]]]]

# print("Hello World!")
# answer = input("How are you?\n")
# print("I am fine")

# [[[[[[[[[[[[[[[[[[[[[[[[[ Built-in Data Types ]]]]]]]]]]]]]]]]]]]]]]]]]

# Lists
empty_list = []
empty_list = list()

# Tuples
#   Are similar to lists, but they are immutable
time_blocks = ('AM', 'PM')
tuple('abc')    # => ('a', 'b', 'c')
tuple([1,2,3])  # => (1, 2, 3)

# Ranges
#   An immutable list of numbers typically used for looping
#   Can be declared with 1-3 parameters
#       start - optional (0)
#       end   - required
#       step  - optional (1)
not_empty_list = []
for i in range(2, -5, -1):
  not_empty_list.append(i)
print(not_empty_list)   # => [2, 1, 0, -1, -2, -3, -4]

# Dictionaries
#   Mappable collection where a hashable key is used to reference an object
a = {'one':1, 'two':2, 'three':3}
b = dict(one=1, two=2, three=3)
c = dict([('two', 2), ('one', 1), ('three', 3)])
print(a == b == c)   # => True

# Sets
#   An unordered collection of distinct objects
#   Sets have three common uses in Python:
#       removing duplicates
#       membership testing (that is, finding out if an object is included)
#       mathematical operators: intersection, union, difference, symmetric difference
new_set = {1, 2, 3}
newer_set = set('abracadabra')  # => {'a', 'b', 'r', 'c', 'd'}

# [[[[[[[[[[[[[[[[[[[[[[[[[ Built-in Functions ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= Functions Using Iterables =========================

# filter(function, iterable)
#   Creates a new iterable of the same type where the function returns True

# map(function, iterable)
#   Creates a new iterable of the same type with the result of the function on every item

# sorted(iterable, key=None, reverse=False)
#   creates a new sorted list from the items in the iterable
#   key: optional function which converts item to a value for comparison
#        e.g. key=str.lower
#   reverse: optional boolean
#   `key` and `reverse` parameters must be set with the name and equal sign

# enumerate(iterable, start=0)
#   starts with a sequence and converts it to a series of tuples with index and value
#   `start` parameter must be set with the name and equal sign

# zip(*iterables)
#   creates a zip object filled with tuples that combine the items from each iterable
#   zip will stop when the shortest iterable runs out of items

# ========================= Functions Analyzing Iterables =========================

# len(iterable)
#   returns the length of the iterable

# max(*args, key=None)
#   returns the largest item
#   key: optional function to convert an item for comparison
#   `key` parameter must be set using its name and equal sign

# min(*args, key=None)
#   returns the smallest item
#   key: optional function to convert an item for comparison
#   `key` parameter must be set using its name and equal sign

# sum(iterable)
#   returns the sum

# any(iterable)
#   returns True if any items are true
#   will return False if the iterable is empty because it didnt find any true items

# all(iterable)
#   returns True if all items are true
#   will return True if the iterable is empty because it didnt find any false items

# ========================= Dictionaries =========================

# dir(dictionary)
#   returns a list of keys in the dictionary

# dict.values(), dict.keys(), dict.items()
#   creates a list-like object for iteration
abcs = {'a':1, 'b':2, 'c':3}
for k in abcs.keys():
  print(k)
print('easy as')
for v in abcs.values():
  print(v)

# ========================= Sets =========================

a = {1, 2, 3}
b = {2, 4, 6}

# Union
#   The `|` operator or union(*sets) will return a new set of the combined sets
print(a | b)        # => {1, 2, 3, 4, 6}

# Intersection
#   The `&` operator or intersection(*sets) will return a new set of items that 
#     appear in all sets
print(a & b)        # => {2}

# Difference
#   The `-` operator or difference(*sets) will return a new set of items that 
#     appear in the first set but NOT the others
print(a - b)        # => {1, 3}
print(b - a)        # => {4, 6}

# Symmetric Difference
#   The `^` operator or symmetric_difference(*sets) will return a new set of items 
#     that appear in EXACTLY ONE set but NOT the others
print(a ^ b)        # => {1, 3, 4, 6}

# [[[[[[[[[[[[[[[[[[[[[[[[[ Extra Arguments ]]]]]]]]]]]]]]]]]]]]]]]]]

# Functions may accept extra arguments using the `*` operator
def add(a, b, *args):
  total = a + b 
  for n in args:
    total += n
  return total

add(1, 2, 3, 4)   # => 10

# To add keyword arguments use the `**` operator. Keyword arguments are 
#   conventionally named kwargs
def greet_from_country(greeting, **kwargs):
  for k, v in kwargs.items():
    print(greeting, k, 'from', v)

greet_from_country('Hi', 
                   Michelle='Sweden',
                   Daniel='Brooklyn')
# => Hi Michelle from Sweden
#    Hi Daniel from Brooklyn

# Function arguments must appear in this order:
#     formal positional arguments
#     *args
#     keyword arguments with default values
#     **kwargs

# [[[[[[[[[[[[[[[[[[[[[[[[[ Importing ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= Terms =========================

# A module is simply Python code in a separate file.
# A package is the path to a directory that contains modules which is also a special type of module.
# __init__.py is the default file for a package.
# A submodule is another file in a module’s folder.
# A function is (obviously!) a function in a module.

# ------------------------- Visualization -------------------------

# project
# │   README.md
# │   __init__.py
# |   shopping_cart.py         <== module
# │
# └───pet                      <== package
# │   │
# │   └───mammal               <== module (and package)
# |   |   |   __init__.py
# │   |   │   dog.py           <== submodule
# │   |   │   cat.py           <== submodule
# │   |   │   ...
# │   │
# │   └───fish                 <== module (and package)
# |   |   |   __init__.py
# │   │
# │   └───bird                 <== module (and package)
# |       |   __init__.py
# │
# └───housing                  <== module (and package)
#     │   __init__.py
#     │   aquarium.py          <== submodule
#     │   cage.py              <== submodule
#     │   kennel.py            <== submodule
#     |   ...

# ========================= Import Statements =========================

# Common examples:
# most basic
#     import <module> 
# dot syntax
#     import <package>.<subpackage>.<module> 
# one module in a package
#     from <package> import <module> 
# multiple modules or submodules in a package
#     from <package> import <module>, <module> 
# special case for module's __init__.py to get submodules in the same folder
#     from . import <submodule>
# down to the function level
#     from <module> import <function>, <function> 
# renaming to avoid confusion or conflict
#     from <package> import <module> as <altName> 

# When you have large modules, it is good practice to break up functionality into 
# submodules - that is, separate files - and have __init__.py import them. This 
# means the module can be imported as a whole, or each part imported as it's 
# required. These submodules can even be placed into subfolders (and given their 
# own __init__.py file).

# [[[[[[[[[[[[[[[[[[[[[[[[[ Classes ]]]]]]]]]]]]]]]]]]]]]]]]]

class AngryBird:
  __slots__ = ['_x', '_y']

  def __init__(self, x=0, y=0):
    """
    Construct a new AngryBird with position (0, 0).
    """
    self._x = x
    self._y = y

  def move_up_by(self, dy):
    self._y += dy

  def get_y(self):
    return self._y

# In Python, every instance method gets a reference to the object as the first 
#   parameter

# Under the hood, Python uses a dictionary to store the instance variables of a 
#   class. You can create a dunder class variable `__slots__` to reserve memory
#   for the iVars you know you will use. This speeds up Python's instance 
#   initialization

bird = AngryBird()
print(bird.get_y())
bird.move_up_by(2)
print(bird.get_y())