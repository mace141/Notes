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

# [[[[[[[[[[[[[[[[[[[[[[[[[ Decorators ]]]]]]]]]]]]]]]]]]]]]]]]] 

# A decorator is a function that takes in another function to extend its behavior
#   and return a modified version of the inner function

# ========================= Callbacks =========================

# Python functions are first-class objects, meaning there are no restrictions to 
#   how the function can be used (can use as argument)

def say_hi(name):
  print(f'Hi, {name}!')

def say_good_morning(name):
  print(f'Good morning, {name}!')

def say_something_to_curtis(say_something_func):
  return say_something_func('Curtis')

say_something_to_curtis(say_hi)            # => Hi, Curtis!
say_something_to_curtis(say_good_morning)  # => Good morning, Curtis!

# ========================= Introspection =========================

# Introspection is the ability to examine objects to determine its behavior or 
#   type. You can use the `dir()` function to observe the say_hi object

print(say_hi)       # <function say_hi at 0x1037a41f0>
print(dir(say_hi))
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', 
# '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', 
# '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
# '__str__', '__subclasshook__']

print(say_hi.__closure__) # None

# ========================= Closures =========================

# A closure is formed when an inner function has access to an outer function's
#   arguments. `say_hi` above did not close over any arguments, but `say_from` 
#   below closed over the `name` argument, Ryan. 

def say_hi_to(name):
  def say_from(author):
    print(f'Hi, {name}!')
    print(f'This is a message from {author}.')
  return say_from

say_hi_ryan_from = say_hi_to('Ryan')
say_hi_ryan_from('Julia')             # Hi, Ryan! This is a message from Julia.
say_hi_ryan_from('Erik')              # Hi, Ryan! This is a message from Erik.

print(say_hi_ryan_from.__closure__)   # (<cell at 0x1093cf1f0: str object at 0x1094035f0>,)
print(say_hi_ryan_from.__closure__[0].cell_contents)  # Ryan

# ========================= Decorators =========================

# Decorators can wrap functions to dynamically modify their behavior

def message_decorator(message_func):
  def message_wrapper(name):
    from_statement = 'This is a message from ' + name
    print(message_func() + from_statement)
  return message_wrapper

def say_hi():
  return 'Hi! '

def say_bye():
  return 'Bye! '

print(say_hi)             # <function say_hi at 0x10f1a9280>>
print(say_hi.__closure__) # None

say_hi = message_decorator(say_hi)
print(say_hi)             # <function message_decorator.<locals>.message_wrapper at 0x10f1a93a0>
print(say_hi.__closure__) # (<cell at 0x10f17b1f0: function object at 0x10f1a9280>,)
print(say_hi.__closure__[0].cell_contents) # <function say_hi at 0x10f1a9280>

# ------------------------- Syntactic Sugar -------------------------

# Use the `@` symbol to prefix the name of a decorator function

def message_decorator(message_func):
  def message_wrapper(name):
    from_statement = 'This is a message from ' + name
    print(message_func() + from_statement)
  return message_wrapper

@message_decorator  # Replaces the need for `say_hi = message_decorator(say_hi)`
def say_hi():
  return 'Hi! '

@message_decorator  # Replaces the need for `say_bye = message_decorator(say_bye)`
def say_bye():
  return 'Bye! '

print(say_hi)   # <function message_decorator.<locals>.message_wrapper at 0x10d53c310>
print(say_bye)  # <function message_decorator.<locals>.message_wrapper at 0x10d53c430>

# ========================= Built-in Class Decorators =========================

# Python has some built-in class decorators: `@property`, `@classmethod`, and
#   `@staticmethod`

# The `@property` decorator can also be used to define setter and deleter methods.
#   `@method_name.setter` and `@method_name.deleter`

class Ring:
  def __init__(self):
    self._nickname = "Shiny ring"

  @property
  def nickname(self):
    return self._nickname

  @nickname.setter
  def nickname(self, value):
    self._nickname = value

  @nickname.deleter
  def nickname(self):
    del self._nickname
    print('Oh no! The ring is gone!')

ring = Ring()
print(ring.nickname)                  # Shiny ring
ring.nickname = "Gollum's precious"
print(ring.nickname)                  # Gollum's precious
del ring.nickname                     # Oh no! The ring is gone!
# print(ring.nickname)                  # AttributeError: 'Ring' object has no attribute '_nickname'

# [[[[[[[[[[[[[[[[[[[[[[[[[ with Keyword ]]]]]]]]]]]]]]]]]]]]]]]]]

f = None
try:
  f = open('some_file.txt')
  # do stuff with f like read the file
finally:
  if f:
    f.close()

# The `with` keyword lets us avoid writing boilerplate everywhere you want to 
#   access some resource whose connection needs to be closed, connections like 
#   those to files and databases

with open('some_file.txt') as f:
  # do stuff with f like read the file
  pass

# [[[[[[[[[[[[[[[[[[[[[[[[[ Psycopg ]]]]]]]]]]]]]]]]]]]]]]]]]

# Psycopg is a package that allows connection and interaction with PostgreSQL

# `pipenv install psycopg2-binary`
#   Installs Psycopg package

# ========================= Setting Up The Database =========================
"""
Use these SQL statements to set up the database
    CREATE USER psycopg_test_user WITH CREATEDB PASSWORD 'password';
    CREATE DATABASE psycopg_test_db WITH OWNER psycopg_test_user;

Set up the tables 
    CREATE TABLE owners (
      id SERIAL PRIMARY KEY,
      first_name VARCHAR(255) NOT NULL,
      last_name VARCHAR(255) NOT NULL,
      email VARCHAR(255) NOT NULL
    );

    -- Make and model should have their own tables
    -- Simplified for now
    CREATE TABLE cars (
      id SERIAL PRIMARY KEY,
      manu_year INTEGER NOT NULL,
      make VARCHAR(255),
      model VARCHAR(255),
      owner_id INTEGER NOT NULL,
      FOREIGN KEY (owner_id) REFERENCES owners(id)
    );

    INSERT INTO owners (first_name, last_name, email)
    VALUES
    ('Tim', 'Petrol', 'rotary@fast.com'),
    ('Ryan', 'Runner', '10sec@jdm.com'),
    ('Tia', 'Petrol', 'typer@wtec.com');

    INSERT INTO cars (manu_year, make, model, owner_id)
    VALUES
    (1993, 'Mazda', 'Rx7', 1),
    (1995, 'Mitsubishi', 'Eclipse', 2),
    (1994, 'Acura', 'Integra', 3);
"""
# ========================= Connecting to PostgreSQL with Psycopg =========================

# Create a file called psycopg_demo.py with the following contents
#   Then run `pipenv run python psycopg_demo.py`

import psycopg2

CONNECTION_PARAMETERS = {
                          'dbname': 'psycopg_test_db',
                          'user': 'psycopg_test_user',
                          'password': 'password',
}

with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
  print(conn.get_dsn_parameters())

  # Output: {'user': 'psycopg_test_user', 'dbname': 'psycopg_test_db', ...}


# ========================= Open a "Cursor" Perform Data Operations =========================

# After connecting to the database, you can create a cursor to perform operations

with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
  with conn.cursor() as curs:
    curs.execute("SELECT USER;")
    result = curs.fetchone()
    print(result) # 'psycopg_test_user'


# ========================= Parametrized SQL Operations =========================

def get_owners_cars(owner_id):
    """
    Fetch and return all cars in the cars table
    :param owner_id: <int> the id of the owner who's cars to return
    :return: <list> the results of the query
    """
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute("""
                         SELECT manu_year, make, model FROM cars
                         WHERE owner_id = %(owner_id)s
                         """,
                         {'owner_id': owner_id})
            results = curs.fetchall()
            return results

print(get_owners_cars(1)) # [(1993, 'Mazda', 'Rx7')]

# [[[[[[[[[[[[[[[[[[[[[[[[[ Introduction to Flask ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/python-for-in-person/week-2--python-for-in-person/introduction-to-flask

# Flask is a framework for building web applications. 

# Benefits of Flask:
#     No rules
#     Easy to use
#     Scalable
#     Flask makes no assumptions about the database layer

# In order to start a Flask app, you have to specify which file to use with the
#   FLASK_APP environment variable

# `export FLASK_APP=app.py`
# `pipenv run flask run`

# To change the environment, you use the FLASK_ENV environment variable
# `export FLASK_ENV=development`

# ========================= Configuration =========================

# Every time you start your virtual environment you need to remember to set the 
#   FLASK_APP environment variable. When you change projects, you'll need to 
#   switch to the appropriate file name. 

# One solution is create your application in app/_init.py_. Another is to use 
#   configuration. The benefit of a configuration file is that you can set many 
#   other environment variables as well, such as FLASK_ENV.

# ------------------------- .flaskenv -------------------------

# In order for Flask to access the .flaskenv file, you need to install 
#   `python-dotenv`

# `pipenv install python-dotenv~=0.13`

# Create a .flaskenv file and add in the environment variables
#     FLASK_APP=app.py
#     FLASK_ENV=development

# ------------------------- app.config -------------------------

# Another approach to configuration is to use a dictionary, `config`, that comes 
#   with Flask. You will often use both.

# - - - - - - - - - - - - - Good: set values directly - - - - - - - - - - - - -

from flask import Flask

app = Flask(__name__)
# Set configuration variable
app.config["greeting"] = 'Hey there, humans!'


@app.route('/')
def hello():
  # Use configuration variable
  return f'<h1>{app.config["greeting"]}</h1>'

# - - - - - - - - - - - - - Better: config class - - - - - - - - - - - - -

# Create a file called config.py and make a class with a property for each 
#   configuration variable
class Config(object):
  GREETING = 'Salutations, superior students!'

# Import the config class in your program
from flask import Flask
# Load configuration class
from config import Config

app = Flask(__name__)
# Apply configuration from class
app.config.from_object(Config)


@app.route('/')
def hello():
  # Use configuration variable
  return f'<h1>{app.config["GREETING"]}</h1>'

# - - - - - - - - - - - - - Best: environment overrides config - - - - - - - - - - - - -

# Sometimes you have a value which changes from environment to environment

# Use the built-in `os` package and create a class variable which tries to get
#   the environment value or sets a default value
import os

class Config(object):
  GREETING = 'Salutations, superior students!'
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-key-for-devs'

# [[[[[[[[[[[[[[[[[[[[[[[[[ Routing In Flask ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= Static Routes =========================

# Routes are set with the `route` decorator on a function. 
@app.route('/')
def some_function():
  return 'Some content'

# You can decorate the same function with multiple URLs
@app.route('/')
@app.route('/home')
def home():
  return '<h1>Home</h1>'

# ========================= Wildcards =========================

# Wildcards are placed between `<` and `>` in the path. They are also accessible
#   in the parameters of the function
@app.route('/item/<id>')
def item(id):
  return f'<h1>Item {id}</h1>'

# You can also specify the data type of the wildcard
@app.route('/item/<int:id>')
def item(id):
  return f'<h1>Item {id}</h1>'

# ========================= Before Request =========================

# To run code before each request, use the `before_request` decorator
@app.before_request
def before_request_function():
  print("before_request is running")

# ========================= After Request =========================
  
# To run code after each request, use the `after_request` decorator
@app.after_request
def after_request_function():
  print("after_request is running")

# ========================= Before First Request =========================

# To run code before the first request, use the `before_first_request` decorator
#   This is great for initializing your application
@app.before_first_request
def before_first_function():
  print("before_first_request happens once")

# ========================= Static Assets =========================
  
# Flask has a built-in route `/static` that will look for a directory named 
#   `/static` in your project where you create the Flask object

# [[[[[[[[[[[[[[[[[[[[[[[[[ Routing Blueprints In Flask ]]]]]]]]]]]]]]]]]]]]]]]]]

# A Blueprint is a way to organize a group of related routes

# ========================= Creating and Registering =========================

# To create a Blueprint, import it from Flask and call its constructor

# routes/admin.py
from flask import Blueprint

bp = Blueprint('admin', __name__, url_prefix='/admin')
# This creates a blueprint named admin

# To register a blueprint, use the `register_blueprint` method of the Flask object
import routes

app = Flask(__name__)

app.register_blueprint(routes.admin.bp)

# ========================= Using the Blueprint =========================

# In the file where you created the Blueprint, you can use the blueprint object
#   to register individual routes

# routes/admin.py
from flask import Blueprint

bp = Blueprint('admin', __name__, url_prefix='/admin')

# This route is now /admin/dashboard because it uses the
# url_prefix="/admin" from the Blueprint registration as
# the beginning of the route and, then, adding the route
# registered, /dashboard, to it.
@bp.route('/dashboard', methods=('GET', 'POST'))
def admin_dashboard():
  pass

# [[[[[[[[[[[[[[[[[[[[[[[[[ Flask Sessions ]]]]]]]]]]]]]]]]]]]]]]]]]

# To store session related data, import session from flask
from flask import Flask, session # More things, if you need them

app = Flask(__name__)

# other configuration of the Flask application object

@app.route('/visits-counter/')
def visits():
  if 'visits' in session:
    # reading and updating session data
    session['visits'] = session.get('visits') + 1
  else:
    # setting session data
    session['visits'] = 1
  return "Total visits: {}".format(session.get('visits'))

@app.route('/delete-visits/', methods=["POST"])
def delete_visits():
  session.pop('visits', None) # delete visits
  return 'Visits deleted'

# [[[[[[[[[[[[[[[[[[[[[[[[[ Class and Instance Variables ]]]]]]]]]]]]]]]]]]]]]]]]]

# Class variables are defined directly on the class
from datetime import date


class Book:
  loan_duration = 14  # days

  def __init__(self, title, series, author):
    self._title = title
    self._series = series
    self._author = author
    self._checked_out_on = None

  def checkout(self, checked_out_on=date.today()):
    """
    Method to checkout a book.
    """
    self._checked_out_on = checked_out_on

  def is_overdue(self):
    """
    Method to check if a book is overdue.
    """
    overdue = False

    if self._checked_out_on is not None:
      elapsed_days = (date.today() - self._checked_out_on).days
      overdue = elapsed_days > self.loan_duration

    return overdue

  def __repr__(self):
    return f"{self._title} by {self._author}"

# We have to be careful when setting class variables through an instance. This 
#   will result in shadowing or hiding of the shared class variable
fellowship_of_the_ring = Book(
  "The Fellowship of the Ring",
  "The Lord of the Rings",
  "J.R.R. Tolkien")
grapes_of_wrath = Book(
  "The Grapes of Wrath",
  None,
  "John Steinbeck")

# The `loan_duration` class variable
# can be accessed through any instance.
print(fellowship_of_the_ring.loan_duration)  # 14
print(grapes_of_wrath.loan_duration)  # 14

# Now change the `loan_duration` class variable value
# through the `Book` class.
Book.loan_duration = 7

# The new `loan_duration` class variable value
# is available on each existing instance.
print(fellowship_of_the_ring.loan_duration)  # 7
print(grapes_of_wrath.loan_duration)  # 7

# THIS CODE DOESN'T WORK LIKE YOU'D EXPECT IT TO!
# Attempt to update the `loan_duration` class variable
# through an instance.
fellowship_of_the_ring.loan_duration = 3

# Check to see if the `loan_duration` class variable
# was successfully updated.
print(fellowship_of_the_ring.loan_duration)  # 3
print(grapes_of_wrath.loan_duration)  # 7 <-- Oh oh!

# Hmm... The `loan_duration` class variable
# is still set to `7`.
print(Book.loan_duration)  # 7

# ========================= __slots__ =========================

# The __slots__ variable lets Python speed up instance initialization and prevent 
#   attribute name collisions. It also prevents you from dynamically defining
#   attributes and setting a class variable value through an instance. 

# ========================= Class and Static Methods =========================

# Class and static methods can be defined using the built-in `@classmethod` and 
#   `@staticmethod` class decorators

# Class methods must take `cls` (the entire class definition) as its first 
#   parameter and are commonly used to create instances
@classmethod
def create_series(cls, series, author, *args):
  """
  Factory class method for creating a series of books.
  """
  return [cls(title, series, author) for title in args]

# Static methods are similar to class methods, but dont receive the class 
#   definition as the first parameter. They are commonly used to perform 
#   operations on collections of instances or tasks related to the class
@staticmethod
def get_titles(*args):
  """
  Static method that accepts a variable number
  of Book instances and returns a list of their titles.
  """
  return [book._title for book in args]