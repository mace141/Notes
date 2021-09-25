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

"""
    Value	             Method	                Result
s = "Hello"	        s.upper()	                "HELLO"
s = "Hello"	        s.lower()	                "hello"
s = "Hello"	        s.islower()	               False
s = "hello"	        s.islower()	               True
s = "Hello"	        s.isupper()	               False
s = "HELLO"	        s.isupper()	               True
s = "Hello"	        s.startswith("He")    	   True
s = "Hello"	        s.endswith("lo")	         True
s = "Hello World"	  s.split()	            ["Hello", "World"]
s = "i-am-a-dog"	  s.split("-")	        ["i", "am", "a", "dog"]
s = "--"            s.join(['a', 'b'])        'a--b'

Method	      Purpose
isalpha()	    returns True if the string consists only of letters and is not blank.
isalnum()	    returns True if the string consists only of letters and numbers and is not blank.
isdecimal()	  returns True if the string consists only of numeric characters and is not blank.
isspace()	    returns True if the string consists only of spaces, tabs, and newlines and is not blank.
istitle()	    returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.
""" 

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
#     Any empty sequence or collections
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
while count < 3:
  if count == 2:
    continue
  print('in while loop')
  count += 1

# pass simply does nothing, while continue will skip to next iteration
# break will exit the loop

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