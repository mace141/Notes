# [[[[[[[[[[[[[[[[[[[[[[[[[  ]]]]]]]]]]]]]]]]]]]]]]]]]
# =========================  =========================
# -------------------------  -------------------------
# $$$$$$$$$$$$$$$$$$$$$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$

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

p format_name("daniel", "wu")

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