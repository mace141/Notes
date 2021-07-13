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

# [[[[[[[[[[[[[[[[[[[[[[[[[ Splat Operator ]]]]]]]]]]]]]]]]]]]]]]]]] 

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

# [[[[[[[[[[[[[[[[[[[[[[[[[ Exceptions ]]]]]]]]]]]]]]]]]]]]]]]]]

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

# $$$$$$$$$$$$$$$$$$$$$$$$$ LECTURE $$$$$$$$$$$$$$$$$$$$$$$$$

# ------------------------- Inject -------------------------

# does not work on strings
# can be used on arrays, and ranges

# ------------------------- Scope -------------------------

# blocks can reference variables initialized outside the block
# but you cannot referrence a variable initialized inside the block from the outside

# ------------------------- Variable References -------------------------

# reassigning a variable will change it's object ID

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

# [[[[[[[[[[[[[[[[[[[[[[[[[ OOP ]]]]]]]]]]]]]]]]]]]]]]]]]

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

# [[[[[[[[[[[[[[[[[[[[[[[[[ Nil as Falsey ]]]]]]]]]]]]]]]]]]]]]]]]]

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

greet 
greet("Lily")

def call_that_proc(val, &prc)
  prc ||= Proc.new { |data| data.upcase + "!!" }
  prc.call(val)
end

p call_that_proc("hey")                                             # => "HEY!!"
p call_that_proc("programmers") { |data| data * 3 }                 # => "programmersprogrammersprogrammers"
p call_that_proc("code") { |data| "--" + data.capitalize + "--"}    # => "--Code--"

# ------------------------- Lazy Initialization -------------------------

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
p jli           # jli will lack a menu here until called upon
jli.menu 
p jli           # jli will now have a menu

# $$$$$$$$$$$$$$$$$$$$$$$$$ W3D1 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ Non-Technical Overview of Ruby ]]]]]]]]]]]]]]]]]]]]]]]]]

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

# $$$$$$$$$$$$$$$$$$$$$$$$$ Lecture $$$$$$$$$$$$$$$$$$$$$$$$$

## block_given?
# used in byebug, this will return a boolean for whether a block was given or not

## yield ele
# will call the given block on ele whether the method definition has a block 
# parameter or not using yield is NOT best practice

# Conventional Order of Class Methods
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

# [[[[[[[[[[[[[[[[[[[[[[[[[ Common Errors ]]]]]]]]]]]]]]]]]]]]]]]]]

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