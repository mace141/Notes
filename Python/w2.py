# [[[[[[[[[[[[[[[[[[[[[[[[[ Local Packages and Modules ]]]]]]]]]]]]]]]]]]]]]]]]]

# Two kinds of modules:
#     Directories
#         __init__.py initializes the directory module when it is imported or ran
#           as a program
#         __main__.py runs if it is invoked as a program
#     Files

# Modules can be invoked in two ways:
#     As a script
#         python3 my_package/my_module.py
#     As a module
#         python3 -m my_package.my_module

# When invoking a directory as a module, the __init__ and __main__ files will run
# But when invoking it as a program, only the __main__ file will run

# Importing a module will run its ancestor __init__.py 

# [[[[[[[[[[[[[[[[[[[[[[[[[ Managing Dependencies ]]]]]]]]]]]]]]]]]]]]]]]]]

#  Python     | Node.js equivalent
# ------------|---------------------
#  pyenv      | nvm
#  pip        | npm --global
#  virtualenv | nvm + node_modules
#  pipenv     | npm + nvm
#  Pipfile    | package.json

# pyenv installs versions of Python on your machine and switches between them
# pip only does global installations of packages
# virtualenv allows users to create isolated Python environments for diff projects
# pipenv ties together pip and virtualenv

# [[[[[[[[[[[[[[[[[[[[[[[[[ Pipenv Workflow ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= Creating a New Project =========================

# Follow these steps to initialize a virtual environment with pipenv:
#     Create a project directory
#     Change working directory to project directory
#     Run `pipenv --python "$PYENV_ROOT/versions/«version_name»/bin/python"`

# ========================= Installing Packages =========================

# pipenv install «package_name»

# pipenv install «package_name»~=«package_version»
#     e.g. pipenv install Flask~=1.1

# ========================= Running the App =========================

# `pipenv shell`
#     This command activates the virtual environment and uses packages configured
#       in the .venv directory

# ========================= Getting Ready for Deployment =========================

# `pipenv lock -r > requirements.txt`
#     This will generate a requirements.txt file, which pip will use to install
#       packages on your server (e.g. Heroku)

# [[[[[[[[[[[[[[[[[[[[[[[[[ Python Unit Testing ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= General File Layout =========================

# your-project
# ├── Pipfile
# ├── Pipfile.lock
# ├── app
# │   ├── __init__.py
# │   └── app code...
# └── test
#     ├── __init__.py
#     └── tests...

# ------------------------- Testing Files with the Same Name -------------------------

# If you need to test modules with the same name, then change them into packages
#   by adding __init__.py to the test directory and subdirectories

# your-project
# ├── Pipfile
# ├── Pipfile.lock
# ├── app
# │   ├── __init__.py
# │   └── app code...
# └── test
#     ├── __init__.py
#     ├── module1
#     │   ├── __init__.py
#     │   └── test_with_same_name.py
#     └── module2
#         ├── __init__.py
#         └── test_with_same_name.py

# ========================= unittest =========================

# Python's unittest package is class-based. You must define classes and the tests
#   are defined as methods. The class must also inherit from unittest.TestCase

import unittest

class TestSomeStuff(unittest.TestCase):
  """
  This is a test case, something run by both unittest
  and pytest.
  """

  def setUp(self):
    """The setUp method runs before each test."""
    pass

  def tearDown(self):
    """The tearDown method runs after each test."""
    pass

  def test_some_thing(self):
    """
    All methods that begin with "test_" are run as
    unit tests. Do your assertions in here so that
    the test runner will capture them.
    """
    pass

# ========================= pytest =========================

# pytest is not as prescriptive; there are various ways to define unit test. 
#   However, the test modules should always be named `test_*.py` or `*_test.py`

# ------------------------- Parameterized Functions -------------------------

# Sometimes your test logic will be very similar for several tests. Pytest allows
#   you to parametrize the test cases to reduce repetition

# Regular tests
def test_reverso_with_even_letters():
  result = reverso("ABCD")

  assert result == "DCBA"

def test_reverso_with_odd_letters():
  result = reverso("ABC")

  assert result == "CBA"

def test_reverso_with_no_letters():
  result = reverso("")

  assert result == ""

# Parametrized tests
from pytest import mark

@mark.parametrize("s,expected", [("ABCD", "DBCA"), ("ABC", "CBA"), ("", "")])
def test_reverso(s, expected):
  result = reverso(s)
  assert result == expected

# ========================= Assertions =========================

# To make assertions in pytest, you use the `assert` keyword which accepts a 
#   Python expression. If it is falsey, then it will throw an AssertionError.

def test_double_function_returns_twice_passed_in():
    result = double(3)
    assert result == 6

# With unittest, the assertions are built-in methods inherited from 
#   unittest.TestCase. Below are some examples.

#  Method	                    | Checks that
# ----------------------------|------------------------
#  assertEqual(a, b)	        | a == b
#  assertNotEqual(a, b)	      | a != b
#  assertTrue(x)	            | bool(x) is True
#  assertFalse(x)	            | bool(x) is False
#  assertIs(a, b)	            | a is b
#  assertIsNot(a, b)	        | a is not b
#  assertIsNone(x)	          | x is None
#  assertIsNotNone(x)	        | x is not None
#  assertIn(a, b)	            | a in b
#  assertNotIn(a, b)	        | a not in b
#  assertIsInstance(a, b)	    | isinstance(a, b)
#  assertNotIsInstance(a, b)	| not isinstance(a, b)

class TestDoubleFunction(unittest.TestCase):
  def test_returns_twice_passed_in(self):
    lst1 = [1, 2, 3]
    lst2 = [1, 1 + 1, 1 + 1 + 1]
    self.assertEqual(lst1, lst2)