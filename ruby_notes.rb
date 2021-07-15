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

# ========================= Tree Traversal Algorithms (Search) =========================

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
