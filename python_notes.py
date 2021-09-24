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

print("Spaghetti"[15])    # => IndexError: string index out of range
print("Spaghetti"[1:4])  # => pag
print("Spaghetti"[4:-1])    # => hett
print("Spaghetti"[4:4])  # => (empty string)

