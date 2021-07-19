# $$$$$$$$$$$$$$$$$$$$$$$$$ W1D1 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Becoming a Rubyist ]]]]]]]]]]]]]]]]]]]]]]]]] 

# ------------------------- Implicit return -------------------------
# you may omit the word return in the last executable line of code

def getAvg(num1, num2)
  (num1 + num2) / 2.0
end

# ------------------------- Omitting parentheses ------------------------- 

def hiDaniel
  p "Hi Daniel!"
end

# hiDaniel # this is preferred over hiDaniel()

# ------------------------- Use single line conditionals if possible ------------------------- 

# hiDaniel if 2.even?

# ------------------------- Use built-in methods ------------------------- 

2.even? 
["daniel", "dylan", "mom", "dad"].last # or [-1]

# ------------------------- Use enumerables to iterate ------------------------- 

# .each 
# .all? 
# .times 

# [[[[[[[[[[[[[[[[[[[[[[[[[ Common Enumerables ]]]]]]]]]]]]]]]]]]]]]]]]] 

# .all? 
# .none?
# .any? 
# .one?
# .count
# .sum
# .max .min
# .flatten

# [[[[[[[[[[[[[[[[[[[[[[[[[ Symbols ]]]]]]]]]]]]]]]]]]]]]]]]] 

# symbols are denoted with a colon 
# they behave similarly to strings except they are immutable

sym = :hello
sym

# symbols are commonly used as hash keys and can replace the rocket when initializing a hash

my_bootcamp = { name:"App Academy", color:"red", locations:["NY", "SF", "ONLINE"] }
my_bootcamp
my_bootcamp[:color]

# [[[[[[[[[[[[[[[[[[[[[[[[[ Default Arguments ]]]]]]]]]]]]]]]]]]]]]]]]] 

def hiLily(message, num = 1)
    p message * num + " Lily!"
end

# hiLily("wassup")
# hiLily("wassup", 5)

def greeting(person_1, person_2 = nil)
    if person_2.nil?
        p "Hi " + person_1 
    else
        p "Hi " + person_1 + " and " + person_2
    end
end

# greeting("Daniel")
# greeting("Daniel", "Lily")

# [[[[[[[[[[[[[[[[[[[[[[[[[ Option Hashes ]]]]]]]]]]]]]]]]]]]]]]]]] 

# you can omit the curly braces in the arguments for more readability

def repeat(message, hash={ :upper => false, :repeats => 1 })
    message.upcase! if hash[:upper] 
    p message * hash[:repeats]
end

# repeat("hello")
# repeat("bye", :upper=>true, :repeats=>5)

# [[[[[[[[[[[[[[[[[[[[[[[[[ Splat Operator ]]]]]]]]]]]]]]]]]]]]]]]]] !I

# used to accept multiple arguments

def printArgs(arg1, arg2, *args)
  p arg1
  p arg2
  p args 
end

# printArgs("a", "b", "c", "d", "e", "f")

# also used to decompose an array

def sayNames(first, last)
  p "Your name is " + first + " and your last name is " + last
end

names = ["Lily", "Zhu"]
# sayNames(*names) 

#!I
# double splats are used to decompose a hash, 
# BUT THIS ONLY WORKS IF THE KEYS ARE SYMBOLS

old_hash = { a:1, b:2 }
new_hash = { **old_hash, c:3 }
new_hash 

# [[[[[[[[[[[[[[[[[[[[[[[[[ Inject ]]]]]]]]]]]]]]]]]]]]]]]]] 

# inject may use a default accumulator

[4, 3, 7, 8, 5, 2].inject { |accum, ele| accum + ele }        # ==> 29
[4, 3, 7, 8, 5, 2].inject(100) { |accum, ele| accum + ele }   # ==> 129
injection = [4, 3, 7, 8, 5, 2].inject(0) do |accum, ele| 
    if ele.even?
        accum + ele
    else
        accum
    end
end
injection                                                     # ==> 14

# [[[[[[[[[[[[[[[[[[[[[[[[[ Scope ]]]]]]]]]]]]]]]]]]]]]]]]]

# each method will have its own LOCAL SCOPE. variables defined outside of the 
# method cannot be referenced inside the method and vice versa

# Variables starting with $ have a GLOBAL SCOPE
# Uppercase variables also have GLOBAL SCOPE

$bonsai = "tree"        # Global variable
$bonsai = "small tree"
TREE = "plant"          # Constant variable. Cannot be reassigned; is mutable
# TREE = "wood"         # will result in error/warning if you reassign a constant

# if statements DO NOT have their own scope. 
# blocks have "one way scope". you can reference from inside to outside but the opposite

# [[[[[[[[[[[[[[[[[[[[[[[[[ Bubble Sort ]]]]]]]]]]]]]]]]]]]]]]]]]

def bubble_sort(array)
  sorted = false 
  while !sorted 
      sorted = true 
      (0...array.length - 1).each do |i|
          if array[i] > array[i + 1]
              array[i], array[i + 1] = array[i + 1], array[i] 
              sorted = false 
          end
      end
  end
  array 
end

# [[[[[[[[[[[[[[[[[[[[[[[[[ Exceptions ]]]]]]]]]]]]]]]]]]]]]]]]] !I

# https://open.appacademy.io/learn/swe-in-person/software-engineering-foundations/exceptions-notes

def format_name(first, last)
  if !(first.instance_of?(String) && last.instance_of?(String))
      raise "arguments must be strings"           # if error? ->  raise "error"
  end
  first.capitalize + " " + last.capitalize
end

format_name("daniel", "wu")

first_name = 42
last_name = true
begin
  puts format_name(first_name, last_name)
rescue
  # do stuff to rescue the "arguments must be strings" exception...
  puts "there was an exception :("
end

# [[[[[[[[[[[[[[[[[[[[[[[[[ Introduction ]]]]]]]]]]]]]]]]]]]]]]]]]

# why full stack?
# because more is now expected of us. we have to understand the entirety of the app

# what is pair programming?
# an agile software development technique, which involves a driver and a navigator

# park-instructors@appacademy.io
# use this email if you need to contact instructors about something urgent
# i.e missing attendance

# ------------------------- Reports -------------------------
# nightly reports
# weekly reports - THURSDAYS

# [[[[[[[[[[[[[[[[[[[[[[[[[ LECTURE ]]]]]]]]]]]]]]]]]]]]]]]]]

# ------------------------- Inject -------------------------

# does not work on strings
# can be used on arrays, and ranges !I

# ------------------------- Scope -------------------------

# blocks can reference variables initialized outside the block
# but you cannot referrence a variable initialized inside the block from the outside

# ------------------------- Variable References ------------------------- !I

# creating a variable will create a pointer to a location in memory

# reassigning a variable will change it's object ID and the location it's
  # pointing to

# use a block to create a subarray with new references
# Array.new(3) { Array.new(3) }         ==> 3x3 grid

# $$$$$$$$$$$$$$$$$$$$$$$$$ W1D2 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ TDD ]]]]]]]]]]]]]]]]]]]]]]]]]

# Test Driven Development is essentially writing out test cases to test one 
# aspect of the method before moving onto the next aspect and writing more code

# [[[[[[[[[[[[[[[[[[[[[[[[[ RSpec ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/software-engineering-foundations/rspec-notes

# have your terminal open in the parent folder of the rspec
# run command below to install gems
## bundle install
# run command below to run rspec
## bundle exec rspec

# gems are open source libraries which allow you to access other programmers codes

# [[[[[[[[[[[[[[[[[[[[[[[[[ Pry ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/software-engineering-foundations/pry-notes

## ls String 
# lists string methods

## show-doc String#end_with?
# shows how to use .end_with?

## load file.rb
# loads the entire file into pry

## show-source method_name
# shows the code for the method

# [[[[[[[[[[[[[[[[[[[[[[[[[ Byebug ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/software-engineering-foundations/bye-bug-notes

## require "byebug"
# place this at the top of your file

## debugger
# place this before the code you want to debug

## l 2-15
# lists lines 2 to 15 in the debugger

## s
# steps into the method call on the current line
# use s to step into blocks of code

## n
# moves onto the next line of executable code

## break 19
# pauses the code's execution at line 19 to resume debugging

## c 
# resumes execution of code until another breakpoint

## display var
# displays the current value of the variable

# [[[[[[[[[[[[[[[[[[[[[[[[[ Blocks ]]]]]]]]]]]]]]]]]]]]]]]]]

# { } and do...end behave the same

## arr.map { |ele| ele.upcase }  is the same as  arr.map(&:upcase)

# [[[[[[[[[[[[[[[[[[[[[[[[[ Procs ]]]]]]]]]]]]]]]]]]]]]]]]]

# procs are used to store blocks to variables for easy use
# blocks cannot be passed into a method but procs can

doubler = Proc.new { |num| num * 2 }
# initializes and assigns the proc to a variable

# & ampersand may be used to convert a block into a proc in a method parameter
def add_and_proc(num1, num2, &prc)
  prc.call(num1 + num2)
end

add_and_proc(1, 3) { |num| num * 10 }

# because map needs a block, you can add & in front of a proc like below
[1, 2, 3].map(&doubler)

# you can use do blocks to initialize a proc but not when passing into a method
# as an argument

doubler = Proc.new do |n|
  n * 2
end

# cannot use a do block here
add_and_proc(2, 3) { |n| n / 2.0 }

# [[[[[[[[[[[[[[[[[[[[[[[[[ Why Do We Pair ]]]]]]]]]]]]]]]]]]]]]]]]]

# teamwork building
# talk code
# learn from others
# practice communication

# [[[[[[[[[[[[[[[[[[[[[[[[[ Good Pairing Habits ]]]]]]]]]]]]]]]]]]]]]]]]]

# communication
# open-mindedness
# understanding strengths & weaknesses
# respect, positivity, accountibility
# patience
# studying in order to be prepared

# [[[[[[[[[[[[[[[[[[[[[[[[[ Bad Pairing Habits ]]]]]]]]]]]]]]]]]]]]]]]]]

# backseat driving
# giving up too soon
# self-deprecation
# thinking in silence
# being impatient
# giving out the answer
# being dismissive
# ignoring timer

# [[[[[[[[[[[[[[[[[[[[[[[[[ My Partner Is So Ahead ]]]]]]]]]]]]]]]]]]]]]]]]]

# don't ever feel bad for asking a question
#       you're depriving your partner of a teaching opportunity
# don't get discouraged
# own what you know and don't know

# [[[[[[[[[[[[[[[[[[[[[[[[[ My Partner Is So Behind ]]]]]]]]]]]]]]]]]]]]]]]]]

# be proactive - check in with your partner
# don't make assumptions
# push them up - guide them
# make sure you're thinking aloud

# [[[[[[[[[[[[[[[[[[[[[[[[[ Pairing Exercise Questions ]]]]]]]]]]]]]]]]]]]]]]]]]

# what are you doing well? 
# what can i improve on as a pair? 
# what can you improve on as a pair? 

# $$$$$$$$$$$$$$$$$$$$$$$$$ W2D1 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Classes ]]]]]]]]]]]]]]]]]]]]]]]]]

# how to create cats poorly

cat_1 = {name: "Sennacy", color: "brown", age: 3}
cat_2 = {name: "Whiskers", color: "white", age: 5}
cat_3 = {name: "Garfield", color: "orange", age: 7}

# how to create cats using a CLASS

class Cat 
  def initialize(name, color, age)
    @name = name 
    @color = color
    @age = age 
  end
  # getter methods: can be called on to return desired output
  def name
    @name 
  end

  def color 
    @color 
  end

  def age 
    @age
  end
  # setter methods: allow user to change an instance variable/attribute
  def age=(new_age)
    @age = new_age
  end

  def meow_at(person)
    puts "#{@name} meows at #{person}"
  end
end

cat_4 = Cat.new("Dundun", "orange", 11)
# p cat_4
# puts cat_4.name
cat_4.age = 12          # parentheses around the argument can be omitted
# p cat_4
# cat_4.meow_at "Lily"

# ========================= Instance vs Class Variables =========================

class Car 
  # a class variable initializes attributes that apply to all class instances
  # in this case, # of wheels for all cars
  @@num_wheels = 4
  # a class constant is a class variable that cannot be changed
  NUM_DOORS = 4
  
  def initialize(color)
    @color = color 
  end
  
  def num_wheels 
    @@num_wheels 
  end
  def num_doors 
    NUM_DOORS
  end
  # class methods can change attributes for all current and future classinstances
  def self.upgrade
    @@num_wheels = 0
  end
end

car_1 = Car.new("black")
car_2 = Car.new("red")

# p car_1
# p car_2
# puts "#{car_1.num_wheels} wheels"
# puts "#{car_2.num_wheels} wheels"

Car.upgrade
# puts "called Car.upgrade. cars are now flying"
# puts "#{car_1.num_wheels} wheels"
# puts "#{car_2.num_wheels} wheels"

car_3 = Car.new("silver")

# puts "#{car_3.num_wheels} wheels"
# puts "#{car_3.num_doors} doors"

# ========================= Monkey Patching =========================

# Monkey Patching is adding functionality to an existing class
# Classes: Integer, String, Array, Hash, etc. 

class Integer 
  def prime?
    return false if self < 2
    (2...self).none? { |n| self % n == 0 }
  end
end

11.prime?
15.prime?

# $$$$$$$$$$$$$$$$$$$$$$$$$ W2D2 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Requiring Files ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= Require Relative =========================

# When our code become more complex, we'll need to separate it into different files
# following the principle of "Separation of Concerns"

# If this is our project directory and we're trying to acccess code in the cat.rb file 
# from the pet_hotel.rb file, then we'd add this to the top of our pet_hotel.rb file 

# project_root
#       pet_hotel.rb
#       cat.rb

# require_relative "./cat.rb"

# When using "require_relative" we need to specify a path that is relative to the current file
# A single dot, ./ , denotes the current location of our file
# Two dots, ../ , denotes moving up a directory

# You cannot access variables from other files unless they are constant variables


# ------------------------- Require vs Require Relative -------------------------

# require is used for gems and files ruby knows the locations of
# require_relative is used for files that we write

# [[[[[[[[[[[[[[[[[[[[[[[[[ User Input ]]]]]]]]]]]]]]]]]]]]]]]]]

## gets
# is a built-in method that allows the user to give input
# there will be an added "\n" at the end of the input because the user presses Enter 
# meaning gets will always return a string. so if you're asking for a number, you will
# have to convert it to an integer using .to_i

# p "Enter your name:"
# name = gets 
# puts "Using puts -----"
# puts "Hello #{name}"
# puts "Using p -----"
# p "Hello #{name}"

## .chomp
# is a built-in method that removes record separators, i.e "\n", "\r" 

# p "Who is your wife?"
# wife = gets.chomp
# p "#{wife} is beautiful."

# [[[[[[[[[[[[[[[[[[[[[[[[[ OOP ]]]]]]]]]]]]]]]]]]]]]]]]] !I

# https://open.appacademy.io/learn/swe-in-person/software-engineering-foundations/abstraction-and-encapsulation-notes

# Four Pillars of OOP: Abstraction, Encapsulation, Polymorphism, Inheritance

# ========================= Abstraction =========================

# Abstraction is the process of exposing essential features of a program while hiding 
# the inner workings that aren't necessary to using the program. 

# ========================= Encapsulation =========================

# Encapsulation is the process of giving users access to things that are safe to use

# For example, if we were to initialize a Queue class with an add to end of queue and 
# remove from front of queue features, we wouldn't initialize a getter method to the class
# This is because we don't want users to add people into the line where they don't belong. 

# [[[[[[[[[[[[[[[[[[[[[[[[[ Attr Methods ]]]]]]]]]]]]]]]]]]]]]]]]]

## attr_reader
# creates getter methods, which allow you to read and mutate the object
# attr_reader :name, :age

## attr_writer
# creates setter methods, which allow you to reassign the object

## attr_accessor
# creates getter and setter methods

# [[[[[[[[[[[[[[[[[[[[[[[[[ Syntactic Sugar ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= Operator Methods =========================

# ==, >, +, etc.

class Person
  attr_reader :first_name, :last_name
  
  def initialize(first_name, last_name, age)
    @first_name = first_name
    @last_name = last_name
    @age = age
  end
  
  def ==(other_person)
    self.last_name == other_person.last_name
  end
end

person_1 = Person.new("Jane", "Doe", 20)
person_2 = Person.new("John", "Doe", 18)

## person1.==(person2) is the same as person1 == person2

# ========================= Bracket Methods =========================

class Queue
  def initialize
    @line = []
  end
  
  def [](position)
    @line[position]
  end
  
  def []=(position, ele)
    @line[position] = ele
  end
  
  def add(ele)
    @line << ele # add ele to back of line
    nil
  end
  
  def remove
    @line.shift  # remove front ele of line
  end
end
  
grocery_checkout = Queue.new
grocery_checkout.add("Alan")
grocery_checkout.add("Alonzo")

# ------------------------- #[] -------------------------

## grocery_checkout[0] is the same as grocery_checkout.[](0)

# ------------------------- #[]= -------------------------

## grocery_checkout[0] = "Grace" is the same as grocery_checkout.[]=(0, "Grace")

# $$$$$$$$$$$$$$$$$$$$$$$$$ W2D4 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Recursion ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/software-engineering-foundations/recursion-notes

# Recursion is when a method calls itself. It's used when a problem can be solved
# with smaller versions of the same problem

# All recursive methods need a BASE CASE and a RECURSIVE STEP
# Base case: the condition when we stop the recursion
# Recursive step: where we continue the recursion by calling the method

# Once you figure out the base case, try to figure out the recursive step based 
# on the base case

def countdown(n)
  if n == 0
    puts "Liftoff!"
    return
  end 
  puts n
  countdown(n-1)
end

countdown(10)

def factorial(n)
  return 1 if n == 1
  n * factorial(n-1)
end

p factorial(5)          # => 120

def fibonacci(n)
  return 1 if n == 1 || n == 2
  fibonacci(n - 1) + fibonacci(n - 2)
end

p fibonacci(6)          # => 8

# [[[[[[[[[[[[[[[[[[[[[[[[[ Spaceship Operator ]]]]]]]]]]]]]]]]]]]]]]]]]

## <=> is used to relatively compare two values
# given a <=> b, it will return 
# -1 if a is less than b
# 0 if a is equal to b
# 1 if a is greater than b

# watch the last few mins of alvin's spaceship operator lecture again to review
# when to use parentheses around method call or assign a method call to a variable

# use parentheses around the (method call and do ... end block) when passing a
  # block into a method call

# [[[[[[[[[[[[[[[[[[[[[[[[[ Nil as Falsey ]]]]]]]]]]]]]]]]]]]]]]]]] !I

# In Ruby, every value can be treated as truthy or falsey. 
# Falsey: nil and false
# Truthy: everything else

val = "a"       # try reassigning val to anything. i.e [], 1, etc.
if val
  p true
else
  p false
end

# ========================= || =========================

## How || OR really works is like so
# given a || b, it will return
# a if a is truthy
# b is a is falsey

# That means || can be used on any values. It is especially useful for default 
  # procs/arguments

def greet(person = nil)
  person ||= "you"    # is the same as person = person || "you"
  p "Hey #{person}"
end

# greet 
# greet("Lily")

def call_that_proc(val, &prc)
  prc ||= Proc.new { |data| data.upcase + "!!" }
  prc.call(val)
end

call_that_proc("hey")                                             # => "HEY!!"
call_that_proc("programmers") { |data| data * 3 }                 # => "programmersprogrammersprogrammers"
call_that_proc("code") { |data| "--" + data.capitalize + "--"}    # => "--Code--"

# ------------------------- Lazy Initialization ------------------------- !I

# This refers to using ||= to delay initializing slow or costly objects until
  # absolutely necessary

class Restaurant
  def initialize(name, chefs)
    @name = name 
    @chefs = chefs 
  end

  def menu
    @menu ||= ["sammies", "big ol' cookies", "bean blankies", "chicky catch", "super water"]
  end
end

jli = Restaurant.new("Jli", "Umarbin")
# p jli           # jli will lack a menu here until called upon
jli.menu 
# p jli           # jli will now have a menu

# $$$$$$$$$$$$$$$$$$$$$$$$$ W3D1 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Non-Technical Overview of Ruby ]]]]]]]]]]]]]]]]]]]]]]]]] !I

# https://open.appacademy.io/learn/swe-in-person/ruby/nontechnical-overview-of-ruby

# Ruby is dynamic, reflective, object-oriented, and multi-paradigm

# ========================= Dynamic =========================

# Ruby can execute many common programming behaviors at runtime that static programming
# languages perform during compilation (when a program/compiler translates high-level
# source code to a lower-level langauge, i.e assembly language or machine code). 

# Dynamic programming languages can compile code at runtime and execute code during 
# compile-time; the compilation and execution times are muddled. 

# Ruby, like most dynamic languages, enforce type constraints at runtime; however, 
# in statically typed langauges, they enforce type constraints at compile-time

# ========================= Reflection =========================

# Type introspection: the ability of a program to examine the type and state of 
  # an object at runtime

# Reflection: the ability of a program to manipulate its own structure and 
  # behavior as data

# In reflective languages, reflection permits not only the examination of classes,
  # modules, and methods, but also instantiation and method invocation

# Reflection allows for much of metaprogramming

# ========================= Object-Oriented =========================

# OOP is a paradigm that privileges objects rather than actions and data rather 
# than functions or logic. Adherents to OOP see programs as a society of objects
# that receive messages that they then use to perform their own discrete operations

# Classes often inherit from other classes in an "is-a-type-of" relationship. 
# The Dog class (child class) may inherit data definitions or methods from the 
# Pet class (parent class). This allows for recycling or the child class may 
# overwrite the definitions/methods and create extensions. 

# ------------------------- Encapsulation ------------------------- 

# Encapsulation dictates the programmer must: 
#1 Place all code concerned with particular set of data in one class
#2 Hide methods and data essential to a class's inner workings
#3 Expose via methods, only what's necessary to a class's relationships with other classes

# ========================= Multi-Paradigm =========================

# OOP and supports procedural and functional programming

# Procedural programming privileges invocations, i.e method calls
# OOP joins data structures and methods into "objects" that operate on themselves

# Functional programming privileges pure functions, those whose return value is 
# only determined by the input, without side effects such as changes in state

# Ruby features anonymous functions, lexical closures (functions that capture 
# variables in the context where they're defined), and higher-order functions 
# (functions that accept other functions as arguments and/or return functions) 

# ========================= Ruby vs. Python =========================

# https://assets.aaonline.io/fullstack/ruby/assets/python_vs_ruby.jpg

#1 Python doesn't support blocks
#2 Python has a richer set of data structures
#3 Python is inflexible: there's one best way of doing things
#4 Whitespace is syntactically significant in Python
#5 Python is less object-oriented than Ruby
#6 Ruby values elegance and "magic" over clarity

# ========================= Vocabulary =========================

# Test-Driven Development (TDD)

# Behavior-Driven Development (BDD)
# An extension of TDD. It structures the testing process through descriptions of
# the user's use of the feature being developed

# Unit Test
# Testing the smallest constituent parts in isolation

# Integration Test
# Testing the units of code and the results of their interactions together

# Test Coverage
# Refers to how much of a software program has been tested. 

# [[[[[[[[[[[[[[[[[[[[[[[[[ Debugging ]]]]]]]]]]]]]]]]]]]]]]]]]

# Always read the error
    # Error type
    # Error message
    # Line on which the error occured
    # Stack trace: chain of methods leading up to the error

# Perform a mental stack trace
    # Keep track of the values of variables and return values

# Write code that's testable
    # Break code into smaller testable methods
    # Keep all your code inside methods when writing a script
    ## if __FILE__ == $PROGRAM_NAME
        # p method_name
    # This lets us invoke a script

# Pay technical debt: compromising well designed code for time/deadlines
    # you will eventually need to pay back time

# Use a REPL (like pry) to isolate the problem
    # once you find a regression (input which produces the wrong output) analyze 
    # the code to fix the bug

# You can type "wtf" in pry to look at the stack trace
    # The first line tells us what what method and line of code was executed when
    # the error occured. The next line tells us what called the method from the 
    # first line

## debugger if (conditional)
# triggers the debugger if the conditional results in true

## where 
# run this command in the debugger to show us the call stack

# [[[[[[[[[[[[[[[[[[[[[[[[[ Common Errors ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/ruby/common-exceptions

# [[[[[[[[[[[[[[[[[[[[[[[[[ Lecture ]]]]]]]]]]]]]]]]]]]]]]]]]

## block_given?
# used in byebug, this will return a boolean for whether a block was given or not

## yield ele
# will call the given block on ele whether the method definition has a block 
# parameter or not using yield is NOT best practice

# Conventional Order of Class Methods !I
#1 Class methods/constants
#2 attrs
#3 initialize 
#4 Instance methods

class Fish
  @@all_fish = [] # class variable. you cannot use attr on class variables

  def self.random_state_of_being
    [true,false].sample
  end

# Factory methods are special class methods used to create a specific type of 
# instance of that class
  def self.make_nemo
    Fish.new("Nemo")
  end

  def self.make_random_fish
    name = ""
    5.times { name << ("a".."z").to_a.sample }
    self.new(name)
  end

  def self.all_fish 
    @@all_fish 
  end

  attr_accessor :name

  def initialize(name)
    @name = name 
    @lost = Fish.random_state_of_being
    @@all_fish << self # self is an instance of Fish inside #initialize 
  end

end

# ========================= Common Errors =========================

# Good ruby code should read like English!

# ------------------------- Naming Variables -------------------------

# variables_names = "snake_case"
# ClassNames = "CamelCase"
# CONSTANTS = "SCREAMING_SNAKE_CASE"

# Blocks

# use the do ... end block for multi-line code
# use the {} for one line code

# Interpolation > Concatenation

# Use ! for mutating methods and ? for boolean methods

# Prefer block parameters over yield

# No overly long single-line code

# No one-letter variable names except for loops

# $$$$$$$$$$$$$$$$$$$$$$$$$ W3D2 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ References ]]]]]]]]]]]]]]]]]]]]]]]]] !I

## x = 4
## x = 5
# creates a reference/pointer to 4 and gives x that reference
# removes the pointer to 4 and creates a pointer to 5

## x = 4
## y = x
## x = 10
# x points to 4, y also points to 4, then x points to 10, but y still points to 4
# y's memory reference does not change

## x = 4
## y = x
## x += 2
# y's memory reference still does not change - y remains 4

# There's nothing you can do to change y by changing x because numbers are 
# immutable objects (integers, floats, & symbols)

# !I
## x = "hello"
## y = x
## x << "daniel"
# x and y both become "hellodaniel" 

# !I
## x = "hello"
## y = x
## x += "daniel"
# x becomes "hellodaniel" because of the assignment operator (=)
# y stays the same, "daniel"

## x = []
## y = x
## x << "hello"
# both x and y become ["hello"]

# In Ruby, variables hold references to objects. 

# !I
## = (assignment operator)
# The = sign does not mutate an object, it simply assigns the variable to a new object

# !I
## << and concat
# These two mutate the object and does not change the object's ID

# [[[[[[[[[[[[[[[[[[[[[[[[[ Scope ]]]]]]]]]]]]]]]]]]]]]]]]] !I

# Blocks have their own scope
# If/While do not have their own scope

# You can reference a variable from outer scope from inside a local scope but not
# the other way around. However, when using methods, classes or modules, we do 
# not have access to any previously defined variables. This is because methods, 
# classes and modules create SCOPE GATES

# [[[[[[[[[[[[[[[[[[[[[[[[[ DRY ]]]]]]]]]]]]]]]]]]]]]]]]]

# Don't repeat yourself

# [[[[[[[[[[[[[[[[[[[[[[[[[ Method Decomposition & Design ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/ruby/method-decomposition---design

# Single Responsibility Principle: each method should do one thing
    # 1-10 lines of code (rarely more than 10)
    # Methods should be SHORT

# Your methods should be easily readable like English!

# Methods should not rely on global state - only on what's passed in

# Don't modify arguments unless told to do so

# [[[[[[[[[[[[[[[[[[[[[[[[[ Refactoring and Code Smells ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/ruby/refactoring-and-code-smells

# Code smell: any symptom in the source code of a program that possibly indicates a deeper problem. 
            # They are usually not bugs and are technically not incorrect/disfunctional, but they indicate 
            # weakness in design. They are drivers for refactoring. 

# Examples below
    # Duplicated/similar code
    # Long methods
    # Too many parameters
    # Data clump: if you see groups of data always being passed around together,
        # you should refactor (start_date & end_date => date_range)
    # Long method chains
        # Law of Demeter: only talk to your neighbors - use only one dot. 
           # bicycle.front_tire.rotate => bicycle.rotate_tires
    # Incident exposure: minimize exposure of your code to the public
    # Speculative generality: dont try to generalize your code for future use 
        # when you aren't even sure you're going to need it.
        # don't solve abstract problems, solve concrete problems
        # YAGNI: You Aint Gonna Need It
    # Dead code: don't leave commented out or unused code in your code base

# $$$$$$$$$$$$$$$$$$$$$$$$$ W3D3 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Recursion ]]]]]]]]]]]]]]]]]]]]]]]]]

# Every recursive problem may be solved iteratively 
# Iteration may be more time efficient but some algorithms are just better solved recursively

def upcase(str)
  return str.upcase if str.length <= 1
  str[0].upcase + upcase(str[1..-1])
end

upcase("daniel")

def reverse(str)
  return str if str.length <= 1
  str[-1] + reverse(str[0..-2])
end

reverse("leinad")

def quick_sort(arr)
  return arr if arr.length <= 1
  # random pivot
  pivot = arr.delete_at(rand(arr.length))
  lesser = arr.select { |num| num < pivot }
  greater = arr.select { |num| num >= pivot }

  # first num as pivot
  # pivot = arr.first
  # lesser = arr.drop(1).select { |num| num < pivot }
  # greater = arr.drop(1).select { |num| num >= pivot }

  quick_sort(lesser) + [pivot] + quick_sort(greater)
end

quick_sort((1..20).to_a.shuffle)

def fibonacci(n)
  case n 
  when 1
      [1]
  when 2
      [1, 1]
  else
      # Always try to assign a recursive call to a variable when you're using the
      # same recursive call
      prev_fib = fibonacci(n-1)
      next_num = prev_fib[-1] + prev_fib[-2]
      prev_fib + [next_num]
  end
end

fibonacci(20)

# In order to get a stack trace, you can paste this to the top of your file
# It will let you intentionally crash your program before the stack overflows

# MAX_STACK_SIZE = 200
# tracer = proc do |event|
#   if event == 'call' && caller_locations.length > MAX_STACK_SIZE
#     fail "Probable Stack Overflow"
#   end
# end
# set_trace_func(tracer)

# [[[[[[[[[[[[[[[[[[[[[[[[[ Lecture ]]]]]]]]]]]]]]]]]]]]]]]]]

# if $PROGRAM_NAME = __FILE__
  # do this code
# end

# $PROGRAM_NAME is where file is run. if the file is run in terminal, the 
  # condition will return true if you load the file in pry, $PROGRAM_NAME will 
  # return "pry" rather than the file name
# __FILE__ is the file name

class Array 
  def my_each(&prc)
      self.length.times { |i| prc.call(self[i]) }
      self # each should always returns the original array
  end

  def my_each_rec(&prc)
      # base case
      return self if self.empty?
      # method dependent logic
      prc.call(self.first)
      # recursive step
      self[1..-1].my_each_rec(&prc)
      self # each should always return the original array
  end
end

# $$$$$$$$$$$$$$$$$$$$$$$$$ W3D4 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Git ]]]]]]]]]]]]]]]]]]]]]]]]] !I

# Git is a Version Control System
# Git keeps track of all changes made to your file and lets you review those 
    # changes before uploading them to an online repository
# It also lets you go back to any checkpoints you may have made. By using git, 
    # several people can work on a project at a time and not affect one another 
    # until their branches are merged with the master branch. 
# Each commit only saves the changes made to the remote repo 

# ========================= Remote Repository =========================

# Github is a webservice that integrates git software behind the scenes
# Allows for hosting of projects

# ========================= Vocab =========================

# untracked: newly created files that are not tracked by out git repo

# unstaged: files in our working directory that are not on the staging area

# staged: files added to our staging area

# commit: files that have been commited to .git

# ========================= Git Commands ========================= !I

# ------------------------- Local Commands -------------------------

## git init
# use this command to set up a repository. this should be done before you write any code

## git status
# this command will let you see the files that have been changed

## git diff
# this command will show you what changes have been made

## git add /folder/file_name.rb
# this command will add the file to the STAGING AREA for you to review and decide
    # whether or not to commit

## gid add -A 
# adds all the files to the STAGING AREA

## git diff --staged 
# lets you see what changes have been made to files in the staging area

## git commit -m "message"
# creates a commit for the currently staged files and then removes them from the
    # staging area always use informative messages

## git log
# shows a log of commits

## git log --graph --decorate --oneline
# shows a shortened log of commits in a graph 

## git branch
# shows all the branches that are currently being worked on

## git branch -d branch_name
# deletes branch

## git co branch_name
# switches to the specified branch

## git co -b branch_name
# creates a new branch AND switches to the branch

## git co commit_hash
# lets you see the files from that commit

## git merge branch_name
# merges the specified branch with the branch you're currently in

## git reset file_name
# will UNSTAGE the specified file from the staging area
# DOES NOT affect the working directory

## git reset
# will UNSTAGE ALL the files on the staging area
# DOES NOT affect the working directory

## git reset --hard
# RESETS ALL files to the last commit
# DOES affect the working directory

# ------------------------- Remote Commands -------------------------

## origin
# keyword referring to default remote repo

## git remote
# command to list remotes

## git remote add remote_name remote_url
# name the remote location (where you are uploading your files) as origin

## git push remote_name branch_name
# moves updates from .git to remote repository

## git push -u remote_name branch_name
# upload the branch_name branch to github at what's named origin
# -u lets you do the same thing everytime you run "git push origin master"

## git push --all
# pushes all files onto the remote repository

## git push -f
# -f is short for force which allows us to push our local repo up to remote 
    # while overriding any conflicts

## git clone remote_url
# copies the remote repo to your local machine

## git fetch
# gets updated info from the remote repo

## git pull remote_name branch_name 
# gets updates AND merges from remote repository

# ========================= Git Workflow =========================

# https://open.appacademy.io/learn/swe-in-person/ruby/git-workflow

## git init
## git remote add origin https://github.com/your_username/your_repo_name 
# use these two commands when starting your project
# git remote accesses git commands that interact with remote repos
# add is a git remote command that adds a remote repo to the current repo
# always use origin for the name unless you have a reason not to
# now you have a local repo (.git directory)

## git add file_name
# adds the file to the staging area

## git add -A
# adds all files to the staging area

## git add .
# adds all files in the current directory (and child directories)

## git diff 
# shows the changes made to the currently staged files from the last commit

## git commit -m "message"
# creates a commit for the currently staged files and then removes them from the
    # staging area always use informative messages

## git push
# pushes our local commits to the remote repo that was set with 
    # "git push -u origin branch_name"

## git branch -M main
# will change the default branch name to main

# [[[[[[[[[[[[[[[[[[[[[[[[[ Non-technical Overview of Agile Development ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/ruby/nontechnical-overview-of-agile-development

# [[[[[[[[[[[[[[[[[[[[[[[[[ Lecture ]]]]]]]]]]]]]]]]]]]]]]]]]

class Array
  def merge_sort(&prc)
      return self if self.count <= 1

      midpoint = self.length / 2
      left = self.take(midpoint)
      right = self.drop(midpoint)

      sorted_left, sorted_right = left.merge_sort(&prc), right.merge_sort(&prc)
      Array.merge(sorted_left, sorted_right, prc)
  end

  private
  def self.merge(left, right, prc)
      prc ||= Proc.new { |a, b| a <=> b }

      return right if left.empty?
      return left if right.empty?

      if prc.call(left.first, right.first) == 1
          [right.first] + Array.merge(left, right.drop(1), prc)
      else
          [left.first] + Array.merge(left.drop(1), right, prc)
      end
  end
end

(1..20).to_a.shuffle.merge_sort

def digital_root(num)
  return num if num < 10
  q, r = num.divmod(10)
  digital_root(digital_root(q) + r)
end

# $$$$$$$$$$$$$$$$$$$$$$$$$ W3D5 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Data Structures ]]]]]]]]]]]]]]]]]]]]]]]]] !I

# Arrays, Strings, Hashes, Classes, & Abstract Data Types (ADTs) are all data structures. 

# ADTs are types of data structures with specific rules

# ========================= Types of ADTs ========================= 

# ------------------------- Set -------------------------
# a type of ADT where all elements are unique 
# allows you to look for inclusion, add, & remove items. 

# ------------------------- Map/Dictionary -------------------------
# a set of keys and values (i.e words and definitions) where all keys are unique
# can set (k,v), get (k), and delete (k)

# ------------------------- Stack -------------------------
# Essential Properties: 
    # LIFO: imagine plates at a buffet that are stacked on one another where the
        #   last one in is the first one out
    # push: add to end of stack and return self to avoid implicitly returning 
        # the entire stack
    # pop: remove off end of stack
# Optional Properties
    # peek: look at the element at the end of the stack without removing it
    # size: returns the current stack size
    # empty?: returns a boolean depending on the stack's emptiness
    # inspect

# ------------------------- Queue -------------------------
# Essential Properties: 
    # FIFO: exactly like a queue for a shop where the first in is first out
    # enqueue: add element to the end of the queue
    # dequeue: remove element from the front of the queue
# Optional Properties
    # show: show a copy of the queue
    # size: 
    # empty?: 

# ------------------------- Trees -------------------------
# Properties:
    # Node: basic unit of a tree. Each node holds a value and references to its
        #   children. (Nodes can optionally have references to their parents)
            # The root note is THE TREE - it is the topmost node/vertex
            # Every other node is a sub-tree. Internal nodes have children & 
                # leaf nodes don't have children
    # Depth: the length of the deepest path of a tree
    # Tree traversal: tree paths

# Binary Tree: imagine a prime factorization tree where each number has AT MOST
    #          one parent and every parent has AT MOST two children
# Ternary Tree: similar to the binary tree except each parent can have 3 children
# Poly/n-ary Tree: tree with any number of children

# Breadth First Search (BFS): Searches each generation of nodes before moving onto
    #                         the next. This requires implementation of a Queue ADT
    # Pseudo code for BFS:
        # initialize the queue with just the root
        # until queue.empty?
            # first = queue.shift (dequeue)
            # check if first satisfies the problem
            # enqueue first's children (maybe each node is a class with a children
                # attribute of an array containing children)

# Depth First Search (DFS): Searches down to the leaf node before going back up
    #                       and down again to a different leaf node
    # Pseudo code for DFS:
        # must be recursive
        # base case
            # return root if root == target
        # inductive step
            # call method on the children to search them using .each to go down one side first
            # store the result of the method call in a variable and return it unless it is nil
        # return nil when whole tree is searched

# ========================= Inspecting Complex Elements =========================

# you may want to extend a class and define an inspect method to show what you want
# to see rather than the entire instance's information
## p essentially accomplishes what inspect does

=begin 
class PolyTreeNode
    def inspect_1
        @value.inspect
    end

    def inspect_2
        { value: @value, parent_value: @parent.value }.inspect
    end
end
=end 

# [[[[[[[[[[[[[[[[[[[[[[[[[ Lecture ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= ADT =========================

class Stack
  def initialize
      @store = []
  end

  def push(value)
      store << value 
      self 
  end

  def pop 
      store.pop 
  end

  def peek 
      store.last 
  end

  def size 
      store.length 
  end 

  def empty? 
      store.empty?
  end

  def inspect 
      "#<Stack:#{self.object_id}"
  end
  
  private 
  attr_reader :store # reader is preferred to direct access to iVar
end

class MyQueue
  def initialize 
      @line = []
  end

  def enqueue(el)
      line.push(el)
      self 
  end

  def dequeue 
      line.shift 
  end

  def show 
      line.dup # returns a copy so it cant be mutated
  end

  def empty? 
      line.empty? 
  end

  private 
  attr_reader :line 
end

class Node 
  attr_reader :value, :children 

  def initialize(value, children = [])
      @value = value 
      @children = children 
  end
end

d = Node.new("d")
e = Node.new("e")
f = Node.new("f")
g = Node.new("g")
c = Node.new("c", [f, g])
b = Node.new("b", [d, e])
a = Node.new("a", [b, c])

# ========================= Algorithms & Methods =========================

# Algorithms: general approach and process to solving operations
# Methods: concrete implementation of an algorithm in a specific language

# ========================= Tree Traversal Algorithms (Search) ========================= !I

# BFS: Breadth First Search

def bfs(root, target)
  queue = [root]
  until queue.empty?
      first = queue.shift
      return first if first == target 
      first.children.each { |child| queue << child }
  end
  nil # returns nil once all nodes have been searched
end

bfs(a, d)

# DFS: Depth First Search

def dfs(root, target)
  return root if root == target 
  # important to use .each so that you go down one child (call the method on the
      # child) before the next
  root.children.each do |child| 
      node = dfs(child, target) 
      return node unless node.nil? # explicitly return the node if it is the target
  end
  nil # returns nil once all nodes have been searched
end

dfs(a, e)

# ========================= Practice Assessment Problems =========================

class String
  # Write a `String#symmetric_substrings` method that returns an array of 
  # substrings that are palindromes, e.g. "cool".symmetric_substrings => ["oo"]
  # Only include substrings of length > 1.

  def symmetric_substrings
      substrings = []

      (0...length).each do |start_pos|
          (2..(length - start_pos)).each do |span|
              sub = self[start_pos...(start_pos + span)]
              substrings << sub if sub == sub.reverse
          end
      end

      substrings
  end
end

"banana".symmetric_substrings

def fibs_sum(n)
  return 0 if n == 0
  return 1 if n == 1

  fibs_sum(n - 1) + fibs_sum(n - 2) + 1
end

fibs_sum(10)

# $$$$$$$$$$$$$$$$$$$$$$$$$ W4D1 $$$$$$$$$$$$$$$$$$$$$$$$$ !I

require "set"

# [[[[[[[[[[[[[[[[[[[[[[[[[ Graph Intro ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/ruby/graph-intro

# A graph is any collection of nodes and edges. 

# Unlike trees, a graph may: 
    # lack a root node (a node that has access to all other nodes)
    # have cycles (a non-empty trail where the first node is also the last node)
    # have any number of edges (directed/undirected links between nodes) leaving a node

# ========================= Graph Class Implementation =========================

# This is an example of how to implement a graph

class GraphNode
    attr_accessor :val, :neighbors

    def initialize(val)
        @val = val 
        @neighbors = [] 
    end
end

a = GraphNode.new('a')
b = GraphNode.new('b')
c = GraphNode.new('c')
d = GraphNode.new('d')
e = GraphNode.new('e')
f = GraphNode.new('f')
a.neighbors = [b, c, e]
c.neighbors = [b, d]
e.neighbors = [a]
f.neighbors = [e]

# The above example implements Graph 3 from the AAO reading
# NB how having a neighbor means having access to that node, but that node doesn't 
# necessarily have access to the other node

# ========================= Adjacency Matrix =========================

# Below is an example of an adjacency matrix where the row denotes the origin node and the
# column denotes the destination node. The booleans denote access from origin to destination

matrix = [
#   A       B       C       D       E       F
  [true,  true,   true,   false,  true,   false], # A
  [false, true,   false,  false,  false,  false], # B
  [false, true,   true,   true,   false,  false], # C
  [false, false,  false,  true,   false,  false], # D
  [true,  false,  false,  false,  true,   false], # E
  [false, false,  false,  false,  true,   true]   # F
]

# Advantages: 
    # Allows us to refer to the entire graph with a 2D array
# Disadvantages:
    # The space required to represent the graph (n^2 for a graph of n nodes), 
    # especially if there are only a few edges (few true elements)

# ========================= Adjacency List =========================

# Seeks to solve the problems with an adjacency matrix.
# Keys represent node labels and values represent the neighbors

graph_list = {
  'a': ['b', 'c', 'e'],
  'b': [],
  'c': ['b', 'd'],
  'd': [],
  'e': ['a'],
  'f': ['e']
}

# [[[[[[[[[[[[[[[[[[[[[[[[[ Graph Traversal ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/ruby/graph-traversal

# ========================= DFS Traversal =========================

# ------------------------- Using GraphNode Class -------------------------

def dfs_class(node, visited = Set.new()) # must require "set" at the top of file
    return nil if visited.include?(node.val)

    puts node.val 
    visited.add(node.val)

    node.neighbors.each do |neighbor|
        dfs_class(neighbor, visited)
    end
end

# puts "dfs_class starting from f"
# p dfs_class(f)

# ------------------------- Using Adjacency List -------------------------

def dfs_list(node, graph_list, visited = Set.new())
    return nil if visited.include?(node.to_sym)
  
    puts node
    visited.add(node.to_sym)

    graph_list[node.to_sym].each do |neighbor|
      dfs_list(neighbor, graph_list, visited)
    end
end

# puts "dfs_list starting from f"
# dfs_list('f', graph_list) 

# starting at 'f' will print out all the nodes, but starting at 'a' would not.
# this can be fixed by using a surrounding loop to iterate through the list to jump between
# disconnected regions of the graph

def dfs_connector(graph_list)
    visited = Set.new()
    graph_list.keys.each do |node|
        dfs_list(node, graph_list, visited)
    end
end

# puts "dfs_connector using adjacency list"
# dfs_connector(graph_list)

# $$$$$$$$$$$$$$$$$$$$$$$$$ W4D2 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Inheritance ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/ruby/inheritance

# Inheritance is a way to establish a subtype from an existing class to reuse the code

# ========================= Code Reuse =========================

class User
  attr_reader :first_name, :last_name

  def initialize(first_name, last_name)
      @first_name, @last_name = first_name, last_name
  end

  def full_name
      "#{first_name} #{last_name}"
  end

  def upvote_article(article)
      article.upvotes += 1
  end
end

class SuperUser < User
  attr_reader :super_powers

  def initialize(first_name, last_name, super_powers)
      super(first_name, last_name)    # SuperUser will call the original initialize
      @super_powers = super_powers
  end

  def upvote_article(article)
      # extra votes
       article.upvotes += 3
  end

  def delete_user(user)
       return unless super_powers.include?(:user_deletion)

      # super user is authorized to delete user
      puts "Goodbye, #{user.full_name}!"
  end
end

## < 
# denotes that SuperUser inherits methods from the User class including attrs

# SuperUser does overwrite some methods from User (initialize, upvote_article)

# ========================= Calling the Super Method =========================

## super
# used to call methods from the parent class. can be called with/out arguments

class Animal
  def make_n_noises(n = 2)
      n.times { print "Growl " }
  end
end

class Liger < Animal
  def make_n_noises(num = 4)
      num.times { print "Roar " }
      # here we'll call super without any arguments. This will pass on `num`
      # implicitly to super. You can think of this call to super as:
      # `super(num)`
      super
  end
end

Liger.new.make_n_noises(3) # => Roar Roar Roar Growl Growl Grow
puts 

class Animal
  attr_reader :species

  def initialize(species)
      @species = species
  end
end

class Human < Animal
  attr_reader :name

  def initialize(name)
      super("Homo Sapiens")   # calling Human.new without this super method won't set the species
      @name = name
  end
end

# [[[[[[[[[[[[[[[[[[[[[[[[[ Exceptions, Error Handling ]]]]]]]]]]]]]]]]]]]]]]]]] !I

## raise
# raises an error. you may call .new on an error class output a more specific message 

def prime?(num)
  unless num >= 2
      raise ArgumentError.new "Cannot check if numbers less than 2 are prime"
  end
  (2...num).none? { |n| num % n == 0 }
end

def main 
  while true 
      puts "Please enter a number"
      num = gets.to_i

      begin 
          puts prime?(num)
      rescue ArgumentError => e   # assigns the error message to a variable
          puts "Cannot check if numbers less than 2 are prime"
          puts "Error was: #{e.message}"
      end
  end
end

## ensure
# ensures some code is executed despite of the error

begin 
  a_dangerous_operation
rescue StandardError => e 
  puts "Something went wrong: #{e}"
ensure
  puts "Get to the choppa!"
end

## retry
# use this to repeat the begin block again

def prompt_name
  puts "Please input a name: "
  name_parts = gets.chomp.split

  raise "Uh-oh, finnicky string" if name_parts.count != 2
  
  name_parts 
end

def echo_name
  fName, lName = prompt_name
  puts "Hello #{fName} of #{lName}"
rescue                                  # use the implicit begin by simple adding rescue if the 
  puts "Please only use two names"    # error handling pertains to the whole method
  retry
end 

# echo_name 

# [[[[[[[[[[[[[[[[[[[[[[[[[ Decompositions Into Objects ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/ruby/decomposition-into-objects

# [[[[[[[[[[[[[[[[[[[[[[[[[ Unified Modeling Language ]]]]]]]]]]]]]]]]]]]]]]]]]

# UML is a visual way of describing relationships between different objects in a system
# UML can describe classes or behavior
#     Classes can be related in many ways, including parent-child and association ("has a") relationships
#         Piece is the parent of Pawn
#         Game has a Board
#     Classes usually have three componenents: name, set of attributes, and set of methods
#         attributes are marked as public (+), private (-), or protected (#)
#         methods are underlined

# [[[[[[[[[[[[[[[[[[[[[[[[[ Lecture ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= Pillars of OOP ========================= !I

# Abstraction, Encapsulation, Inheritance, & Polymorphism

# ------------------------- Abstraction -------------------------

# The act of taking a larger system and breaking it down into smaller components
# and hiding unnecessary information from the user while showing only the essentials

# ------------------------- Encapsulation -------------------------

# Bundling data with methods that operate on data
  # Outside of an instance, can only interact with via public methods
  # Expose limited interface to user
# Allows developer to make atomic methods & change code without changing the interface

# + public
  
# - private
  # private methods can only be implicitly used in classes. Except setters! 
      # (otherwise they'll be seen as a local var)
      # i.e, if a Dog class had an attribute @name, it has to be called implicitly
          # within the class
          # puts "#{name} goes bork!" will work, 
              # but "#{self.name} goes bork!" will not work
  # default to this over protected
  
# # protected
  # protected methods can only be called:
      # within the class
      # explicitly or implicitly - allows us to use it on other instances of the class

# ------------------------- Inheritance -------------------------

# Subclasses inherit methods from other classes

# Modules behave just like classes except they cannot be initialized
  # they are used to add functionality and DRY up our code

# Subclasses have an "is a" relationship with the class, while modules have a 
# "has a" relationship with the class. 

module Walkable     # function is just like a class except you cannot initialize modules
  def walk 
    puts "#{name} is walking"
  end
end

class Mammal 
  include Walkable    # must include the module in order to use its methods
  def initialize(name)
    @name = name 
    @warm_blooded = true 
  end

  def eat(food)
    puts "#{name} eats #{food}"
  end

  private 

  attr_accessor :name 
end

class Dog < Mammal      # Dog class will inhert methods from Mammal
  def initialize(name, size)
    # calls Mammal#initialize while passing in name. without this, dog will not 
        # have a name, nor warm_blood
    super(name)     
    @size = size    
  end

  def noise 
    "bark"
  end

  def fetch(item)
    puts "#{name} excitedly fetches #{item}"
  end
end

class Cat < Mammal 
  def noise 
    "meow"
  end
end

d1 = Dog.new("Spot", "woofer")
# p d1.inspect
# d1.name   # => will result in error because #name is a private method
# d1.walk 

# ------------------------- Polymorphism -------------------------

# Inheritance
  # Different classes can be used with the same methods
      # i.e, all Mammals eat, therefore dog eats too
# Duck-typing
  # "If it walks like a duck and quacks like a duck then it is a duck" 

# $$$$$$$$$$$$$$$$$$$$$$$$$ W4D3 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Inheritance and DRY ]]]]]]]]]]]]]]]]]]]]]]]]]

# Inheritance applies the DRY principle
# Don't create unnecessary subclasses unless they have substantially different behavior

class Fish
  def eat 
      puts "eat eat eat"
  end
end

class Shark < Fish 
end

class Minnow < Fish 
end

# The Sharks and Minnows will inherit Fish methods

# [[[[[[[[[[[[[[[[[[[[[[[[[ Encapsulation/Abstraction ]]]]]]]]]]]]]]]]]]]]]]]]]

# Encapsulation is the principle of preventing data/methods from being accessed outside this code

## - private
# private methods can only be accessed from within the class itself

# Abstraction is the principle of hiding information that isn't necessary for the user

# We always want to minimize the amount of information exposed to the user and only expose 
# certain information with good reason

# [[[[[[[[[[[[[[[[[[[[[[[[[ Modules ]]]]]]]]]]]]]]]]]]]]]]]]]

# A Ruby module is similar to a class except you cant instantiate it. Modules contain methods
# that can be mixed into and shared by many classes to keep our code DRY.

## include
# allows the class to access the module's methods as INSTANCE methods

## extend
# allows the class to access the module's methods as CLASS methods

module Greetable
  def greet 
      "Hello, my name is #{self.name}" 
  end
end

class Human 
  include Greetable       # makes the modules methods available to the class

  def initialize(name)
      @name = name 
  end
  
  def name 
      @name 
  end
end

class Robot 
  include Greetable       
  
  def name
      "Model 3000"
  end
end

daniel = Human.new('Daniel')
p daniel.greet 
jarvis = Robot.new 
p jarvis.greet 

# Modules also serve as namespaces - they prevent name collisions. If two files were to have
# the same method but different functions, you can wrap the two files into two different modules

# [[[[[[[[[[[[[[[[[[[[[[[[[ Load/Require/Require_Relative ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/ruby/load-require-require_relative

## require
# Tells Ruby to look for the file in the $LOAD_PATH (directories that contain the source files
# for Ruby's default library) and then the Gem.path (gem directories) if not found in the $LOAD_PATH

# When using require "./file_name" and ruby lib/file_name.rb, you will run into an error because
# the current directory is where you're running the file from. That's why we use require_relative. 

## -I
# this flag can be used to add a folder to the $LOAD_PATH so we can use require when files are not 
# closely packed together

## load 
# loads the file each time when using pry/irb

# [[[[[[[[[[[[[[[[[[[[[[[[[ Public/Private/Protected ]]]]]]]]]]]]]]]]]]]]]]]]]

# Methods are public be default and do not need to be defined as public

# Private methods cannot be called explicitly on an instance - therefore, can only be called from
# inside the method

# Protected methods are only accessible by the class and subclasses. Access is kept within family

# Access controls are not used for security! Private methods can still be accessed using #send
# Instead, they are used to tell other programmer's what they can ignore and what the interface is

# [[[[[[[[[[[[[[[[[[[[[[[[[ Lecture ]]]]]]]]]]]]]]]]]]]]]]]]]

## to_s
# returns string form of piece for rendering board

## valid_moves
# does not do most of the move logic. #moves does the logic

## symbol
# return unicode symbol of the piece (knight for knight)

## move_dirs
# which direction they can slide in

# Slideable module
  # check each direction a piece can move by iterating outwards by each space and stop iteration
  # in that direction once you reach another one of your pieces, an enemy piece, or the edge

  # #moves returns all possible moves
  # Rook#move_dirs returns directions a piece can move
  # Slideable#move_dirs returns all moves in a direction

# ========================= Error Handling =========================

## raise
# raises an error upon a condition - ends the program

## begin rescue block
# allows error message to be sent while keeping the program running

class WrongPasswordError < StandardError 
end

def enter_password
  puts "Please enter your password."
  wrong_pw_attempts = 0 
  begin
      get_input
  rescue WrongPasswordError => e      # can also add other errors separated by a comma "Error, Error1, Error2"
      wrong_pw_attempts += 1
      puts e.message 
      # puts "Incorrect attempts: #{wrong_pw_attempts}" 
      if wrong_pw_attempts > 2
          puts "Too many attempts. Your account is locked :)"    # will stop the program before reaching retry
          # runtime error
      else
          retry 
      end
  ensure 
      puts "Incorrect attempts: #{wrong_pw_attempts}" 
  end
  puts "Thank you!"
end

def get_input 
  input = gets.chomp 
  raise WrongPasswordError.new("Wrong password!") unless input == "starwars"
end

# enter_password

# $$$$$$$$$$$$$$$$$$$$$$$$$ W4D4 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ RSpec & TDD ]]]]]]]]]]]]]]]]]]]]]]]]]

# https://open.appacademy.io/learn/swe-in-person/ruby/rspec-syntax

# https://github.com/rspec/rspec-core
# https://github.com/rspec/rspec-expectations

# RSpec is distributed in a gem called 'rspec' which is a meta-gem that packs 
# three other gems: rspec-core, rspec-expectations, and rspec-mocks

# files are organized in lib and spec directories
    # my_cool_project
        # lib/
            # hello.rb
        # spec/
            # hello_spec.rb

# each spec file is limited to testing a single file and will need to require
# that file and the rspec file. By default, lib/ folder is included in the path
    # require 'rspec'
    # require 'hello'

# here is an example of a spec

describe "#hello_world" do 
    it "returns 'Hello, World!'" do
        expect(hello_world).to eq("Hello, World!")
    end
end

# here is the method

def hello_world 
   "Hello, World!" 
end

# ========================= Describe & It =========================

## it
# RSpec's most basic test unit. all tests go inside an it block

## describe
# RSpec's unit of organization. It gathers several it blocks into a single unit

# Both describe and it take strings as arguments. Describe can also take constants

## context
# an alias for describe, used for nesting inside describe blocks

## expect
# what does the actual testing. its task is to match between a value and expected value
    # there are positive and negative constructions
        # expect(test).to ...
        # expect(test).to_not ...
# block construction is needed when you expect the output to be an error
    # expect { sqrt(-3) }.to raise_error(ArgumentError)
# expect(test).to eq(expected)
    # test == expected
# expect(test).to be(expected)
    # is test the same object as expected

# ========================= Before & After =========================

describe Chess do
    let(:board) { Board.new }
  
    describe '#checkmate?' do
      context 'when in checkmate' do
        before(:each) do
          board.make_move([3, 4], [2, 3])
          board.make_move([1, 2], [4, 5])
          board.make_move([5, 3], [5, 1])
          board.make_move([6, 3], [2, 4])
        end
  
        it 'should return true' do
          expect(board.checkmate?(:black)).to be true
        end
      end
    end
end

## before(:each)
# refreshes the code and runs the before block before each it block

## before(:all)
# does not refresh the code before each it block and is less preferred 

# there are also after(:each) and after(:all)

# somtimes you may want to write out the each of the specs before testing them.
# to do so, you can leave our the do...end

describe '#valid_move?' do
  it 'should return false for wrong colored pieces'
  it 'should return false for moves that are off the board'
  it 'should return false for moves that put you in check'
end

# ========================= Subject & Let =========================

# https://open.appacademy.io/learn/swe-in-person/ruby/subject-and-let
# https://benscheirman.com/2011/05/dry-up-your-rspec-files-with-subject-let-blocks/

## subject { object_instance }
# used to create an object to pass tests. must be declared outside of the it blocks

describe Robot do
    subject { Robot.new }
  
    it "satisfies some expectation" do
      expect(subject).to # ...
    end
end

# can also be declared with a name 

describe Robot do
    subject(:robot) { Robot.new }
  
    it "position should start at [0, 0]" do
      expect(robot.position).to eq([0, 0])
    end
  
    describe "move methods" do
      it "moves left" do
        robot.move_left
        expect(robot.position).to eq([-1, 0])
      end
    end
end

## let(:name) { assigned_object }
# used to create helper objects to interact with subject

describe Robot do
    subject(:robot) { Robot.new }
    let(:light_item) { double("light_item", :weight => 1) }
    let(:max_weight_item) { double("max_weight_item", :weight => 250) }

    describe "#pick_up" do
    it "does not add item past maximum weight of 250" do
      robot.pick_up(max_weight_item)

      expect do
        robot.pick_up(light_item)
      end.to raise_error(ArgumentError)
    end
  end
end

# let objects do not persist states - meaning it resets between scopes

class Cat
    attr_accessor :name
  
    def initialize(name)
      @name = name
    end
  end
  
  describe "Cat" do
    let(:cat) { Cat.new("Sennacy") }
  
    describe "name property" do
      it "returns something we can manipulate" do
        cat.name = "Rocky"
        expect(cat.name).to eq("Rocky")     # cat is now rocky and spec passes
      end
  
      it "does not persist state" do
        expect(cat.name).to eq("Sennacy")   # cat is back to sennacy and also passes
      end
    end
end

# ========================= Test Doubles (Mock) =========================

# https://open.appacademy.io/learn/swe-in-person/ruby/test-doubles

# Test doubles are used when we want to test a class that has interaction with 
# another class because both classes must be functional in order to pass 

RSpec.describe Order do
    let(:customer) { double("customer") }       # customer is another class in this example
    subject(:order) { Order.new(customer) }     # double creates a blank slate (instance of mock)
                                                # waiting for us to add behavior to it
    it "sends email successfully" do
      (customer).to receive(:email_address).and_return("ned@appacademy.io")
  
      expect do
        order.send_confirmation_email
      end.to_not raise_exception
    end
end

# [[[[[[[[[[[[[[[[[[[[[[[[[ Lecture ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= RSpec Workflow =========================

## bundle init
# use this command to make the Gemfile.rb
  # add gem 'rspec' & gem 'byebug' into the Gemfile

## rspec --init
# create the .rspec file
  # add these lines into the .rspec file:
    # --require spec_helper
    # --format documentation
    # --color

## mkdir lib
# any files in this folder must have matching file_spec.rb in the spec folder

## require "file_name"
# require the corresponding file to the top of the spec file

# Write the tests in the spec files before writing the code. The code must first fail before pass - TDD. 

# ========================= RSpec Docs =========================

# https://relishapp.com/rspec/rspec-expectations/docs

# $$$$$$$$$$$$$$$$$$$$$$$$$ W4D5 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Big-O ]]]]]]]]]]]]]]]]]]]]]]]]]

# Big-O helps determine the efficiency/speed of an algorithm

# ========================= RAM Model of Computation =========================

# RAM model of computation measures the runtime of an algorithm by summing up the number of
# steps needed to execute the algorithm

## +, *, =, if, call, memory access
# these basic operations all take one time step

## loops
# n * # of steps with each iteration

# ========================= Asymptotic Analysis =========================

# Asymptotic analysis graphs the runtime of an algorithm using the input size and the RAM MoC
# and determines the behavior of a line by looking for the most dominant term. 
  # Exponential, logarithmic, & constant slopes are some behaviors of a line

  def chop_add(num1, num2)
    num1 = num1 / 5.0           # 3 steps
    num2 = num2 / 5.0           # 3 steps

    300.times do               # 300(3 + 3) steps
        num1 = num1 / 2
        num2 = num2 / 2
    end

    sum = num1 + num2           # 4 steps

    300.times { sum = sum * 2 } # 300(3) steps

    sum * 5                     # 2 steps
end

def iter_add(num1, num2)
    num1.times { num2 += 1}     # 3n + 1 steps
    num2 
end

# Using asymptotic analysis, we can determine that iter_add will be faster than chop_add up 
# until a certain input size. If we were to find the dominant terms for each method, we would
# remove any constants and end up with 1 for chop_add and n for iter_add. 

# chop_add => 2712 steps            dominant term => 1
# iter_add => 3n + 1 steps          dominant term => n
    # dependent on input (n)

# ========================= The Worst Case =========================

def linear_search(array, target)
    array.each do |ele|
        return ele if ele == target 
    end
    -1
end

# This algorithm has a worst case runtime of n, the array's length & a best case runtime of 1. 
# By knowing the worst case runtime, we can say that the algorithm has an O(n) big-o runtime

# ========================= Big-O Classifications =========================

# Common classifications ordered from fastest to slowest
    # Constant O(1)
        # algorithm operates at the same speed no matter the input size

    # Logarithmic O(log(n))
        # every time the input size increases by n, the number of steps only increases by 1
        # i.e, binary search
            # In math, the default log base is 10
            # In CS, the default log base is 2 
                # log_b(n) = x  => b^x = n 

    # Linear O(n) 
        # enumerables

    # Linearithmic O(n*log(n))
        # i.e merge_sort

    # Quadratic O(n^2) 
        # nested iterations
        # i.e, bubble sort 

    # Polynomial O(n^k)

    # Exponential O(k^n) 
        # i.e, subsets

    # Factorial O(n!)
        # i.e, permutations

# ========================= Set Definition =========================

# O(_) = {f| notation just denotes the set of all functions that do not dominate itself

# O(n^2) = {f| O(n), O(2n^2), O(1), etc

# ========================= Space Complexity =========================

# Similar to time complexity except applies to additional space/memory created by the algorithm. 

# [[[[[[[[[[[[[[[[[[[[[[[[[ Lecture ]]]]]]]]]]]]]]]]]]]]]]]]]

## require 'faker'
# faker is a gem that allows you to generate random objects from a selected theme

# merge_sort can be O(n^2) in the worst case when using .shift
    # a better way to implement the helper method is to use indices to iterate through the array

class Array 
    def merge_sort
        return self if length <= 1

        midpoint = length / 2

        left = take(midpoint).merge_sort 
        right = drop(midpoint).merge_sort 

        Array.merge(left, right)
    end

    def self.merge(left, right)
        merged_array = []
        
        until left.empty? || right.empty?
            merged_array << ((left.first < right.first) ? left.shift : right.shift )
        end

        merged_array + left + right 
    end

    def self.better_merge(left, right)
        merged_array = []
        left_idx = 0
        right_idx = 0

        while left_idx < left.length && right_idx < right.length 
            
        end
    end
end

class Vehicle
    def initialize

    end

    def vroom
        puts "vroom"
    end
end

class Sedan < Vehicle
    def zoom
        puts "zoom"
    end
end

accent = Sedan.new
accent.vroom 
accent.zoom 

=begin

# Object Oriented Programming
    - Given a set of classes, some inheriting from others, correctly identify what methods an instance
      of each class has access to
            A subclass has access to all methods from its superclass. The child's method will 
            overwrite the parent's method. 

    - Given a parent and child class, correctly use the super method, passing only the necessary
      arguments, in the child class initialize method to handle shared initialization logic
            super: passes all arguments to the parent method
            super(): passes no arguments to the parent method
            super(arg1): passes specified arguments to the parent method

    - Implement a class inheritance chain using proper Ruby syntax
            class Child < Parent

    - Explain the difference between public, private, and protected methods
            public: can be accessed from inside and out, explicitly and implicitly
            private: can only be implicitly accessed from the inside 
            protected: can be only be accessed from the inside, explicitly or implicitly

    - Explain the difference between inheriting from a class and including a module
            Subclasses have an "is a" relationship with the superclass while those same classes 
            can have a "has a" relationship with a module. Modules can add interfaces for many
            classes of different families at a time. 

# Big O Analysis
    - Explain what "Big O" is and why we utilize it
            Big O is a mathematical notation that describes the limiting behavior of a function
            in terms of time/space as the input size grows. It is used to determine the efficiency
            of an algorithm. 
    
    - Given an implementation of an algorithm, determine its Big O time complexity

    - Given a description of a problem (such as anagrams or two_sum), implement a solution that runs
      in linear time.

# Data Structures
    - Describe what LIFO and FIFO are and how they relate to the Stack and Queue ADTs, respectively

    - Describe the difference between an Abstract Data Type (ADT) and Data Structure
            An ADT defines the logic/rules of the data type and the data structure implements
            the physical form of the data type

    - Given an ADT, identify what underlying data structures native to Ruby could be used to implement the ADT

    - Given a description of an algorithm, identify what ADTs would be useful in implementing a solution

    - Implement a Stack data structure

    - Implement a Queue data structure

# CSS
    - Given a pre-filled HTML skeleton, write CSS selectors to add specific styles to specific html
      tags, classes, and ids

    - Given an HTML skeleton, utilize the > selector in CSS to select all p elements that are children
      of the element with id index and give them all a font-size of 18px and background color of red
      (or any other basic CSS properties)

    - Use the :last-child selector to give the last item in an ordered list a color of green

    - Use the + selector to select the first sibling element of the h1 tag and give it a 1px solid black border

=end

# $$$$$$$$$$$$$$$$$$$$$$$$$ W5D1 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Set ]]]]]]]]]]]]]]]]]]]]]]]]]

# There cannot be duplicates in a set, there's no order, and there's no indexing
# API: include?
    # insert
    # delete 

# indexing in an array is O(1) because indexing uses pointer arithmetic

# use % to put items into buckets when there are more items than buckets

# increase # of buckets when input size increases to keep time complexity faster
    # Amortization: one expensive operation to lower the cost of the next operations

# pathological input: worst case input

# [[[[[[[[[[[[[[[[[[[[[[[[[ Hashing ]]]]]]]]]]]]]]]]]]]]]]]]]

# Properties of a Hash function: 
    # One-way: input cannot be predicted from the output
    # Deterministic: output will always be the same for the same object
    # Uniformly distributed: 
    # Sensitivity: similar objects cannot have similar hashes

# common hashing functions: cityhash, CRC32, murmurhash (used by Ruby)
    # cryptographic hashing functions: MD3, SHA-2, blowfish
        # cryptographic functions have very low chance of collision

# [[[[[[[[[[[[[[[[[[[[[[[[[ Hash Set ]]]]]]]]]]]]]]]]]]]]]]]]]

# assign objects to buckets by modding the hash of the object. 

# [[[[[[[[[[[[[[[[[[[[[[[[[ Linked Lists ]]]]]]]]]]]]]]]]]]]]]]]]]

# Linked list is basically a unary tree. 
# linked lists can be singly-linked (one-way) or doubly-linked (two-way)
# doubly-linked nodes need access to the previous link

# [[[[[[[[[[[[[[[[[[[[[[[[[ Caches ]]]]]]]]]]]]]]]]]]]]]]]]]

# LRU Caches combine the best parts of a linked list and a hashmap
# ejection: O(1) time
    # remove the link and the key
# insertion: O(1) 
    # add the link and key
# read: O(1) 
    # key on the hash to access the link