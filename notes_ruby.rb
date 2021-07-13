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

# p 2.even? 
# p ["daniel", "dylan", "mom", "dad"].last # or [-1]

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

# symbols are denoted with a colon. they behave similarly to strings except they are immutable

sym = :hello
# p sym

# symbols are commonly used as hash keys and can replace the rocket when initializing a hash

my_bootcamp = { name:"App Academy", color:"red", locations:["NY", "SF", "ONLINE"] }
# p my_bootcamp
# p my_bootcamp[:color]

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

# double splats are used to decompose a hash, BUT THIS ONLY WORKS IF THE KEYS ARE SYMBOLS

old_hash = { a:1, b:2 }
new_hash = { **old_hash, c:3 }
# p new_hash 

# [[[[[[[[[[[[[[[[[[[[[[[[[ Inject ]]]]]]]]]]]]]]]]]]]]]]]]] 

# inject may use a default accumulator

# p [4, 3, 7, 8, 5, 2].inject { |accum, ele| accum + ele }        # ==> 29
# p [4, 3, 7, 8, 5, 2].inject(100) { |accum, ele| accum + ele }   # ==> 129
injection = [4, 3, 7, 8, 5, 2].inject(0) do |accum, ele| 
    if ele.even?
        accum + ele
    else
        accum
    end
end
# p injection                                                     # ==> 14

# [[[[[[[[[[[[[[[[[[[[[[[[[ Scope ]]]]]]]]]]]]]]]]]]]]]]]]]

# each method will have its own LOCAL SCOPE. variables defined outside of the method cannot
# be referenced inside the method and vice versa

# variables starting with $ have a GLOBAL SCOPE. Uppercase variables also have GLOBAL SCOPE

$bonsai = "tree"        # Global variable
$bonsai = "small tree"
TREE = "plant"          # Constant variable. It cannot be reassigned but, you can mutate it
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

# p format_name("daniel", "wu")

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
# it is an agile software development technique, which involves a driver and a navigator

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

# $$$$$$$$$$$$$$$$$$$$$$$$$ W2D2 $$$$$$$$$$$$$$$$$$$$$$$$$

# [[[[[[[[[[[[[[[[[[[[[[[[[ TDD ]]]]]]]]]]]]]]]]]]]]]]]]]

# Test Driven Development is essentially writing out test cases to test one aspect of the method
# before moving onto the next aspect and writing more code

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

p add_and_proc(1, 3) { |num| num * 10 }

# because map needs a block, you can add & in front of a proc like below
p [1, 2, 3].map(&doubler)

# you can use do blocks to initialize a proc but not when passing into a method as an argument

doubler = Proc.new do |n|
    n * 2
end

# cannot use a do block here
p add_and_proc(2, 3) { |n| n / 2.0 }

