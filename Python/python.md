# Python

## Data Types

### Numeric

#### Integers 

``` python
1, 2, 3
int()     # => 0
int('1')  # => 1
```

#### Floats

Integers in Python have unlimited accuracy, but floats will eventually run out
of memory

``` python
0.5, 1.1, 2.05
float()   # => 0.0
27e-5     # => 0.00027
```

#### Complex numbers
* numbers that combine a real and an imaginary part

``` python
7j            # => 7j
5.1 + 7j      # => 5.1+7j
complex()     # => 0j
complex(3)    # => 3+0j
complex(3,5)  # => 3+5j
```

### String

Strings are denoted with single, double, or triple quotes. Triple quotes are used
for multi-line strings. 

``` python
print('hello')
print("bye")
print(
"""
  This string spans
  multiple lines
"""
)
```

#### 