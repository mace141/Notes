# [[[[[[[[[[[[[[[[[[[[[[[[[ #1 max value ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, max_value, that takes in list of numbers as an argument. 
# The function should return the largest number in the list.
# Solve this without using any built-in list methods.
# You can assume that the list is non-empty.
#
# test_00:
# max_value([4, 7, 2, 8, 10, 9]) # -> 10
# test_01:
# max_value([10, 5, 40, 40.3]) # -> 40.3
# test_02:
# max_value([-5, -2, -1, -11]) # -> -1
# test_03:
# max_value([42]) # -> 42
# test_04:
# max_value([1000, 8]) # -> 1000
# test_05:
# max_value([1000, 8, 9000]) # -> 9000

def max_value(nums):
  max = float('-inf')
  
  for num in nums:
    if num > max:
      max = num
      
  return max

# [[[[[[[[[[[[[[[[[[[[[[[[[ #2 is prime ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, is_prime, that takes in a number as an argument. The function 
# should return a boolean indicating whether or not the given number is prime.
# A prime number is a number that is only divisible two distinct numbers: 1 and itself.
# For example, 7 is a prime because it is only divisible by 1 and 7. For example, 
# 6 is not a prime because it is divisible by 1, 2, 3, and 6.
# You can assume that the input number is a positive integer.
#
# test_00:
# is_prime(2) # -> true
# test_01:
# is_prime(3) # -> true
# test_02:
# is_prime(4) # -> false
# test_03:
# is_prime(5) # -> true
# test_04:
# is_prime(6) # -> false
# test_05:
# is_prime(7) # -> true
# test_06:
# is_prime(8) # -> false
# test_07:
# is_prime(25) # -> false
# test_08:
# is_prime(31) # -> true
# test_09:
# is_prime(2017) # -> true
# test_10:
# is_prime(2048) # -> false
# test_11:
# is_prime(1) # -> false

from math import floor, sqrt

def is_prime(n):
  if n < 2:
    return False

  for f in range(2, floor(sqrt(n)) + 1):
    if n % f == 0:
      return False

  return True

# [[[[[[[[[[[[[[[[[[[[[[[[[ #3 uncompress ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, uncompress, that takes in a string as an argument. The input 
# string will be formatted into multiple groups according to the following pattern:
# <number><char>
# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 
# 'char' of a group is repeated 'number' times concecutively. You may assume that 
# the input string is well-formed according to the previously mentioned pattern.
#
# test_00:
# uncompress("2c3a1t") # -> 'ccaaat'
# test_01:
# uncompress("4s2b") # -> 'ssssbb'
# test_02:
# uncompress("2p1o5p") # -> 'ppoppppp'
# test_03:
# uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'

def uncompress(str):
  nums = '1234567890'
  times = ''
  result = ''

  for i in range(len(str)):
    if str[i] not in nums:
      result += str[i] * int(times)
      times = ''
    else: 
      times += str[i]
  
  return result

# [[[[[[[[[[[[[[[[[[[[[[[[[ #4 compress ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, compress, that takes in a string as an argument. The function 
# should return a compressed version of the string where consecutive occurences
# of the same characters are compressed into the number of occurences followed 
# by the character. Single character occurences should not be changed.
# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.
#
# test_00:
# compress('ccaaatsss') # -> '2c3at3s'
# test_01:
# compress('ssssbbz') # -> '4s2bz'
# test_02:
# compress('ppoppppp') # -> '2po5p'
# test_03:
# compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'

def compress(s):
  result = ''
  i = 0
  j = 0

  while j < len(s):
    if s[j] != s[j - 1] and j != 0:
      result += s[i] if j - i == 1 else str(j - i) + s[i]
      i = j
    j += 1

  result += s[i] if j - i == 1 else str(j - i) + s[i]

  return result

# [[[[[[[[[[[[[[[[[[[[[[[[[ #5 anagrams ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, anagrams, that takes in two strings as arguments. The 
# function should return a boolean indicating whether or not the strings are
# anagrams. Anagrams are strings that contain the same characters, but in any
# order.
#
# test_00:
# anagrams('restful', 'fluster') # -> true
# test_01:
# anagrams('cats', 'tocs') # -> false
# test_02:
# anagrams('monkeyswrite', 'newyorktimes') # -> true
# test_03:
# anagrams('paper', 'reapa') # -> false
# test_04:
# anagrams('elbow', 'below') # -> true
# test_05:
# anagrams('tax', 'taxi') # -> false

# ========================= My Solution =========================
def anagrams(s1, s2):
  count = {}

  for char in s1:
    if char not in count:
      count[char] = 0
    count[char] += 1

  for char in s2:
    if char not in count:
      count[char] = -1
    count[char] -= 1

  for k, v in count.items():
    if v != 0:
      return False

  return True

# ========================= Alvin's (Dictionaries) =========================
# n = length of string 1, m = length of string 2
# Time: O(n + m), Space: O(n + m)
def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)

def char_count(s):
  count = {}
  
  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1
  
  return count
# ========================= Alvin's (Counters) =========================
# n = length of string 1, m = length of string 2
# Time: O(n + m), Space: O(n + m)
from collections import Counter

def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #6 most frequent char ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, most_frequent_char, that takes in a string as an argument. The
# function should return the most frequent character of the string. If there are 
# ties, return the character that appears earlier in the string.
# You can assume that the input string is non-empty.
#
# test_00:
# most_frequent_char('bookeeper') # -> 'e'
# test_01:
# most_frequent_char('david') # -> 'd'
# test_02:
# most_frequent_char('abby') # -> 'b'
# test_03:
# most_frequent_char('mississippi') # -> 'i'
# test_04:
# most_frequent_char('potato') # -> 'o'
# test_05:
# most_frequent_char('eleventennine') # -> 'e'

from collections import Counter

def most_frequent_char(s):
  count = Counter(s)
  char = None
  for c in s:
    if char is None or count[c] > count[char]:
      char = c 
  return char

# [[[[[[[[[[[[[[[[[[[[[[[[[ #7 pair sum ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, pair_sum, that takes in a list and a target sum as arguments.
# The function should return a tuple containing a pair of indices whose elements
# sum to the given target. The indices returned must be unique.
# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such pair that sums to the target.
#
# test_00:
# pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)
# test_01:
# pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)
# test_02:
# pair_sum([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)
# test_03:
# pair_sum([1, 6, 7, 2], 13) # -> (1, 2)
# test_04:
# pair_sum([9, 9], 18) # -> (0, 1)
# test_05:
# pair_sum([6, 4, 2, 8 ], 12) # -> (1, 3)

def pair_sum(numbers, target_sum):
  differences = {}
  for i, num in enumerate(numbers):
    diff = target_sum - num
    if num in differences:
      return (differences[num], i)
    differences[diff] = i


# [[[[[[[[[[[[[[[[[[[[[[[[[ #8 pair product ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, pair_product, that takes in a list and a target product as 
# arguments. The function should return a tuple containing a pair of indices 
# whose elements multiply to the given target. The indices returned must be 
# unique.
# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such pair whose product is the target.
#
# test_00:
# pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)
# test_01:
# pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
# test_02:
# pair_product([4, 7, 9, 2, 5, 1], 5) # -> (4, 5)
# test_03:
# pair_product([4, 7, 9, 2, 5, 1], 35) # -> (1, 4)
# test_04:
# pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
# test_05:
# pair_product([4, 6, 8, 2], 16) # -> (2, 3)

def pair_product(numbers, target_product):
  quotients = {}
  for i, num in enumerate(numbers):
    quotient = target_product / num
    if num in quotients:
      return (quotients[num], i)
    quotients[quotient] = i

# [[[[[[[[[[[[[[[[[[[[[[[[[ #9 intersection ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, intersection, that takes in two lists, a,b, as arguments. 
# The function should return a new list containing elements that are in both of 
# the two lists.
# You may assume that each input list does not contain duplicate elements.
#
# test_00:
# intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
# test_01:
# intersection([2,4,6], [4,2]) # -> [2,4]
# test_02:
# intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]
# test_03:
# intersection([0,1,2], [10,11]) # -> []
# test_04:
# a = []
# b = []
# for (let i = 0 i < 50000 i += 1) {
#   a.push(i)
#   b.push(i)
# }
# intersection(a, b) # -> [0,1,2,3,..., 49999]

# ========================= My Solution =========================
def intersection(a, b):
  first_set = set(a)
  result = []
  for el in b:
    if el in first_set:
      result.append(el)
  return result

# ========================= Alvin's Solution =========================
def intersection(a, b):
  set_a = set(a)
  return [ item for item in b if item in set_a ]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #10 five sort ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, five_sort, that takes in an list of numbers as an argument.
# The function should rearrange elements of the list such that all 5s appear at 
# the end. Your function should perform this operation in-place by mutating the 
# original list. The function should return the list.
# Elements that are not 5 can appear in any order in the output, as long as all
# 5s are at the end of the list.
#
# test_00
# five_sort([12, 5, 1, 5, 12, 7])
# -> [12, 7, 1, 12, 5, 5] 
# test_01
# five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5])
# -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 
# test_02
# five_sort([5, 5, 5, 1, 1, 1, 4])
# -> [4, 1, 1, 1, 5, 5, 5] 
# test_03
# five_sort([5, 5, 6, 5, 5, 5, 5])
# -> [6, 5, 5, 5, 5, 5, 5] 
# test_04
# five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5])
# -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 

def five_sort(nums):
  i = 0
  j = len(nums) - 1
  while i <= j:
    if nums[j] is 5:
      j -= 1
    elif nums[i] is 5:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
    else:
      i += 1
  return nums

# [[[[[[[[[[[[[[[[[[[[[[[[[ #11 linked list values ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, linked_list_values, that takes in the head of a linked list 
# as an argument. The function should return an list containing all values of 
# the nodes in the linked list.
#
# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# a.next = b
# b.next = c
# c.next = d
# a -> b -> c -> d
# linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]
# test_01:
# x = Node("x")
# y = Node("y")
# x.next = y
# x -> y
# linked_list_values(x) # -> [ 'x', 'y' ]
# test_02:
# q = Node("q")
# q
# linked_list_values(q) # -> [ 'q' ]
# test_03:
# linked_list_values(None) # -> [ ]

def linked_list_values(head):
  result = []
  current = head
  while current is not None:
    result.append(current.val)
    current = current.next
  return result

# [[[[[[[[[[[[[[[[[[[[[[[[[ #12 sum list ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, sum_list, that takes in the head of a linked list containing 
# numbers as an argument. The function should return the total sum of all values 
# in the linked list.
#
# test_00:
# a = Node(2)
# b = Node(8)
# c = Node(3)
# d = Node(-1)
# e = Node(7)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# 2 -> 8 -> 3 -> -1 -> 7
# sum_list(a) # 19
# test_01:
# x = Node(38)
# y = Node(4)
# x.next = y
# 38 -> 4
# sum_list(x) # 42
# test_02:
# z = Node(100)
# 100
# sum_list(z) # 100
# test_03:
# sum_list(None) # 0

# ========================= Iterative =========================
# Time: O(n), Space: O(1)
def sum_list(head):
  sum = 0
  current = head 
  while current is not None:
    sum += current.val
    current = current.next
  return sum

# ========================= Recursive =========================
# Time: O(n), Space: O(n)
def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #13 linked list find ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, linked_list_find, that takes in the head of a linked list and
# a target value. The function should return a boolean indicating whether or not
# the linked list contains the target.
#
# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# a.next = b
# b.next = c
# c.next = d
# a -> b -> c -> d
# linked_list_find(a, "c") # true
# test_01:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# a.next = b
# b.next = c
# c.next = d
# a -> b -> c -> d
# linked_list_find(a, "d") # true
# test_02:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# a.next = b
# b.next = c
# c.next = d
# a -> b -> c -> d
# linked_list_find(a, "q") # false
# test_03:
# node_1 = Node("jason")
# node2 = Node("leneli")
# node_1.next = node2
# jason -> leneli
# linked_list_find(node_1, "jason") # true
# test_04:
# node_1 = Node(42)
# 42
# linked_list_find(node_1, 42) # true
# test_05:
# node_1 = Node(42)
# 42
# linked_list_find(node_1, 100) # false

# ========================= Iterative =========================
# Time: O(n), Space: O(1)
def linked_list_find(head, target):
  current = head
  while current is not None:
    if current.val is target:
      return True 
    current = current.next
  return False

# ========================= Recursive =========================
# Time: O(n), Space: O(n)
def linked_list_find(head, target):
  if head is None:
    return False
  return head.val is target or linked_list_find(head.next, target)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #14 get node value ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, get_node_value, that takes in the head of a linked list and 
# an index. The function should return the value of the linked list at the 
# specified index.
# If there is no node at the given index, then return None.
#
# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# a.next = b
# b.next = c
# c.next = d
# a -> b -> c -> d
# get_node_value(a, 2) # 'c'
# test_01:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# a.next = b
# b.next = c
# c.next = d
# a -> b -> c -> d
# get_node_value(a, 3) # 'd'
# test_02:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# a.next = b
# b.next = c
# c.next = d
# a -> b -> c -> d
# get_node_value(a, 7) # None
# test_03:
# node_1 = Node("banana")
# node2 = Node("mango")
# node_1.next = node2
# banana -> mango
# get_node_value(node_1, 0) # 'banana'
# test_04:
# node_1 = Node("banana")
# node2 = Node("mango")
# node_1.next = node2
# banana -> mango
# get_node_value(node_1, 1) # 'mango'

# ========================= Iterative =========================
# Time: O(n), Space: O(1)
def get_node_value(head, index):
  current = head
  idx = 0
  while current is not None:
    if idx == index:
      return current.val
    current = current.next
    idx += 1
  return None

# ========================= Recursive =========================
# Time: O(n), Space: O(n)
def get_node_value(head, index):
  if head is None:
    return None
  if index is 0:
    return head.val
  return get_node_value(head.next, index - 1)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #15 reverse list ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, reverse_list, that takes in the head of a linked list as an 
# argument. The function should reverse the order of the nodes in the linked 
# list in-place and return the new head of the reversed linked list.
#
# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# a -> b -> c -> d -> e -> f
# reverse_list(a) # f -> e -> d -> c -> b -> a
# test_01:
# x = Node("x")
# y = Node("y")
# x.next = y
# x -> y
# reverse_list(x) # y -> x
# test_02:
# p = Node("p")
# p
# reverse_list(p) # p

# ========================= Iterative =========================
# Time: O(n), Space: O(1)
def reverse_list(head):
  prev = None
  current = head
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

# ========================= Recursive =========================
# Time: O(n), Space: O(n)
def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #16 zipper list ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, zipper_lists, that takes in the head of two linked lists as 
# arguments. The function should zipper the two lists together into single linked 
# list by alternating nodes. If one of the linked lists is longer than the other, 
# the resulting list should terminate with the remaining nodes. The function 
# should return the head of the zippered linked list.
# Do this in-place, by mutating the original Nodes.
# You may assume that both input lists are non-empty.
#
# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# a.next = b
# b.next = c
# a -> b -> c
# x = Node("x")
# y = Node("y")
# z = Node("z")
# x.next = y
# y.next = z
# x -> y -> z
# zipper_lists(a, x)
# a -> x -> b -> y -> c -> z
# test_01:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# a -> b -> c -> d -> e -> f
# x = Node("x")
# y = Node("y")
# z = Node("z")
# x.next = y
# y.next = z
# x -> y -> z
# zipper_lists(a, x)
# a -> x -> b -> y -> c -> z -> d -> e -> f
# test_02:
# s = Node("s")
# t = Node("t")
# s.next = t
# s -> t
# one = Node(1)
# two = Node(2)
# three = Node(3)
# four = Node(4)
# one.next = two
# two.next = three
# three.next = four
# 1 -> 2 -> 3 -> 4
# zipper_lists(s, one)
# s -> 1 -> t -> 2 -> 3 -> 4
# test_03:
# w = Node("w")
# w
# one = Node(1)
# two = Node(2)
# three = Node(3)
# one.next = two
# two.next = three
# 1 -> 2 -> 3 
# zipper_lists(w, one)
# w -> 1 -> 2 -> 3
# test_04:
# one = Node(1)
# two = Node(2)
# three = Node(3)
# one.next = two
# two.next = three
# 1 -> 2 -> 3 
# w = Node("w")
# w
# zipper_lists(one, w)
# 1 -> w -> 2 -> 3

# ========================= Iterative =========================
# Time: O(min(n, m)), Space: O(1)
def zipper_lists(head_1, head_2):
  tail = head_1
  current_1 = head_1.next
  current_2 = head_2
  count = 0
  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
      tail.next = current_2
      current_2 = current_2.next
    else:
      tail.next = current_1
      current_1 = current_1.next
    tail = tail.next
    count += 1

  if current_1 is not None:
    tail.next = current_1
  if current_2 is not None:
    tail.next = current_2

  return head_1

# ========================= Recursive =========================
# Time: O(min(n, m)), Space: O(min(n, m))
def zipper_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1
  next_1 = head_1.next
  next_2 = head_2.next
  head_1.next = head_2
  head_2.next = zipper_lists(next_1, next_2)
  return head_1

# [[[[[[[[[[[[[[[[[[[[[[[[[ #17 merge lists ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, merge_lists, that takes in the head of two sorted linked 
# lists as arguments. The function should merge the two lists together into
# single sorted linked list. The function should return the head of the merged
# linked list.
# Do this in-place, by mutating the original Nodes.
# You may assume that both input lists are non-empty and contain increasing
# sorted numbers.
#
# test_00:
# a = Node(5)
# b = Node(7)
# c = Node(10)
# d = Node(12)
# e = Node(20)
# f = Node(28)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28
# q = Node(6)
# r = Node(8)
# s = Node(9)
# t = Node(25)
# q.next = r
# r.next = s
# s.next = t
# 6 -> 8 -> 9 -> 25
# merge_lists(a, q)
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 
# test_01:
# a = Node(5)
# b = Node(7)
# c = Node(10)
# d = Node(12)
# e = Node(20)
# f = Node(28)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28
# q = Node(1)
# r = Node(8)
# s = Node(9)
# t = Node(10)
# q.next = r
# r.next = s
# s.next = t
# 1 -> 8 -> 9 -> 10
# merge_lists(a, q)
# 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28 
# test_02:
# h = Node(30)
# 30
# p = Node(15)
# q = Node(67)
# p.next = q
# 15 -> 67
# merge_lists(h, p)
# 15 -> 30 -> 67

class Node:
  def __init__(self, val):
    self.val = val 
    self.next = None
# ========================= Iterative =========================
# Time: O(min(n, m)), Space: O(1)
def merge_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  current_1 = head_1
  current_2 = head_2

  while current_1 is not None and current_2 is not None:
    if current_1.val < current_2.val:
      tail.next = current_1
      current_1 = current_1.next
    else:
      tail.next = current_2
      current_2 = current_2.next
    tail = tail.next
  
  if current_1 is None:
    tail.next = current_2
  if current_2 is None:
    tail.next = current_1

  return dummy_head.next

# ========================= Recursive =========================
# Time: O(min(n, m)), Space: O(min(n, m))
def merge_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1
  
  if head_1.val < head_2.val:
    next_1 = head_1.next
    head_1.next = merge_lists(next_1, head_2)
    return head_1
  else:
    next_2 = head_2.next
    head_2.next = merge_lists(head_1, next_2)
    return head_2

# [[[[[[[[[[[[[[[[[[[[[[[[[ #18 is univalue list ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, is_univalue_list, that takes in the head of a linked list as 
# an argument. The function should return a boolean indicating whether or not the 
# linked list contains exactly one unique value.
# You may assume that the input list is non-empty.
#
# test_00:
# a = Node(7)
# b = Node(7)
# c = Node(7)
# a.next = b
# b.next = c
# 7 -> 7 -> 7
# is_univalue_list(a) # true
# test_01:
# a = Node(7)
# b = Node(7)
# c = Node(4)
# a.next = b
# b.next = c
# 7 -> 7 -> 4
# is_univalue_list(a) # false
# test_02:
# u = Node(2)
# v = Node(2)
# w = Node(2)
# x = Node(2)
# y = Node(2)
# u.next = v
# v.next = w
# w.next = x
# x.next = y
# 2 -> 2 -> 2 -> 2 -> 2
# is_univalue_list(u) # true
# test_03:
# u = Node(2)
# v = Node(2)
# w = Node(3)
# x = Node(3)
# y = Node(2)
# u.next = v
# v.next = w
# w.next = x
# x.next = y
# 2 -> 2 -> 3 -> 3 -> 2
# is_univalue_list(u) # false
# test_04:
# z = Node('z')
# z
# is_univalue_list(z) # true

# ========================= Iterative =========================
# Time: O(n), Space: O(1)
def is_univalue_list(head):
  current = head 
  while current is not None:
    if current.val is not head.val:
      return False
    current = current.next
  return True

# ========================= Recursive =========================
# Time: O(n), Space: O(n)
def is_univalue_list(head, prev = None):
  if head is None:
    return True
  
  if prev is None or head.val is prev:
    return is_univalue_list(head.next, head.val)
  else:
    return False

# [[[[[[[[[[[[[[[[[[[[[[[[[ #19 longest streak ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, longest_streak, that takes in the head of a linked list as 
# an argument. The function should return the length of the longest consecutive 
# streak of the same value within the list.
# 
#
# test_00:
# a = Node(5)
# b = Node(5)
# c = Node(7)
# d = Node(7)
# e = Node(7)
# f = Node(6)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# 5 -> 5 -> 7 -> 7 -> 7 -> 6
# longest_streak(a) # 3
# test_01:
# a = Node(3)
# b = Node(3)
# c = Node(3)
# d = Node(3)
# e = Node(9)
# f = Node(9)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# 3 -> 3 -> 3 -> 3 -> 9 -> 9
# longest_streak(a) # 4
# test_02:
# a = Node(9)
# b = Node(9)
# c = Node(1)
# d = Node(9)
# e = Node(9)
# f = Node(9)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# 9 -> 9 -> 1 -> 9 -> 9 -> 9
# longest_streak(a) # 3
# test_03:
# a = Node(5)
# b = Node(5)
# a.next = b
# 5 -> 5
# longest_streak(a) # 2
# test_04:
# a = Node(4)
# 4
# longest_streak(a) # 1
# test_05:
# longest_streak(None) # 0

# ========================= Iterative =========================
# Time: O(n), Space: O(1)
def longest_streak(head):
  count = 0
  max = 0
  current = head
  last = head
  while current is not None:
    if current.val is last.val:
      count += 1
    else:
      last.val = current.val
      count = 1
    if max < count:
      max = count
    current = current.next
  return max

# [[[[[[[[[[[[[[[[[[[[[[[[[ #20 remove node ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, remove_node, that takes in the head of a linked list and a 
# target value as arguments. The function should delete the node containing the 
# target value from the linked list and return the head of the resulting linked 
# list. If the target appears multiple times in the linked list, only remove the 
# first instance of the target in the list.
# Do this in-place.
# You may assume that the input list is non-empty.
#
# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# a -> b -> c -> d -> e -> f
# remove_node(a, "c")
# a -> b -> d -> e -> f
# test_01:
# x = Node("x")
# y = Node("y")
# z = Node("z")
# x.next = y
# y.next = z
# x -> y -> z
# remove_node(x, "z")
# x -> y
# test_02:
# q = Node("q")
# r = Node("r")
# s = Node("s")
# q.next = r
# r.next = s
# q -> r -> s
# remove_node(q, "q")
# r -> s
# test_03:
# node_1 = Node("h")
# node2 = Node("i")
# node3 = Node("j")
# node4 = Node("i")
# node_1.next = node2
# node2.next = node3
# node3.next = node4
# h -> i -> j -> i
# remove_node(node_1, "i")
# h -> j -> i
# test_04:
# t = Node("t")
# t
# remove_node(t, "t")
# None

# ========================= Iterative =========================
# Time: O(n), Space: O(1)
def remove_node(head, target_val):
  dummy_head = Node(None)
  dummy_head.next = head 
  prev = dummy_head
  current = head 

  while current is not None:
    if current.val is target_val:
      prev.next = current.next
      break
    prev = current
    current = current.next

  return dummy_head.next

# ========================= Recursive =========================
# Time: O(n), Space: O(n)
def remove_node(head, target_val):
  if head is None:
    return None
  if head.val == target_val:
    return head.next

  head.next = remove_node(head.next, target_val)
  return head

# [[[[[[[[[[[[[[[[[[[[[[[[[ #21 insert node ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, insert_node, that takes in the head of a linked list, a 
# value, and an index. The function should insert a new node with the value into 
# the list at the specified index. Consider the head of the linked list as index 
# 0. The function should return the head of the resulting linked list.
# Do this in-place.
# You may assume that the input list is non-empty and the index is not greater 
# than the length of the input list.
#
# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# a.next = b
# b.next = c
# c.next = d
# a -> b -> c -> d
# insert_node(a, 'x', 2)
# a -> b -> x -> c -> d
# test_01:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# a.next = b
# b.next = c
# c.next = d
# a -> b -> c -> d
# insert_node(a, 'v', 3)
# a -> b -> c -> v -> d
# test_02:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# a.next = b
# b.next = c
# c.next = d
# a -> b -> c -> d
# insert_node(a, 'm', 4)
# a -> b -> c -> d -> m
# test_03:
# a = Node("a")
# b = Node("b")
# a.next = b
# a -> b
# insert_node(a, 'z', 0)
# z -> a -> b 

# ========================= Iterative =========================
# Time: O(n), Space: O(1)
def insert_node(head, value, index):
  node = Node(value)
  if index == 0:
    node.next = head 
    return node
  
  count = 0
  current = head
  while count < index:
    if count == index - 1:
      next_node = current.next
      current.next = node
      node.next = next_node
    current = current.next
    count += 1
  return head

# ========================= My Solution (Recursive) =========================
# Time: O(n), Space: O(n)
def insert_node(head, value, index, count = 0):
  if count == index:
    node = Node(value)
    node.next = head
    return node

  if head is None:
    return None

  head.next = insert_node(head.next, value, index, count + 1)
  return head

# ========================= Alvin's Solution (Recursive) =========================
def insert_node(head, value, index, count = 0):
  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head

  if head is None:
    return None

  if count == index - 1:
      temp = head.next
      head.next = Node(value)
      head.next.next = temp
      return 

  insert_node(head.next, value, index, count + 1)
  return head

# [[[[[[[[[[[[[[[[[[[[[[[[[ #22 create linked list ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, create_linked_list, that takes in an list of values as an 
# argument. The function should create a linked list containing each element of 
# the list as the values of the nodes. The function should return the head of 
# the linked list.
#
# test_00:
# create_linked_list(["h", "e", "y"])
# h -> e -> y
# test_01:
# create_linked_list([1, 7, 1, 8])
# 1 -> 7 -> 1 -> 8
# test_02:
# create_linked_list(["a"])
# a
# test_03:
# create_linked_list([])
# None

# ========================= Iterative =========================
# Time: O(n), Space: O(n)
def create_linked_list(values):
  if len(values) == 0:
    return None 
  
  head = Node(values[0])
  current = head
  for i in range(1, len(values)):
    node = Node(values[i])
    current.next = node 
    current = current.next
  
  return head

# ========================= Alvin's Solution (Iterative) =========================
# Time: O(n), Space: O(n)
def create_linked_list(values):
  dummy_head = Node(None)
  tail = dummy_head
  for val in values:
    tail.next = Node(val)
    tail = tail.next
  return dummy_head.next

# ========================= Recursive =========================
# Time: O(n), Space: O(n)
def create_linked_list(values, i = 0):
  if i == len(values):
    return None
  node = Node(values[i])
  node.next = create_linked_list(values, i + 1)
  return node

# [[[[[[[[[[[[[[[[[[[[[[[[[ #23 add lists ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, addLists, that takes in the head of two linked lists, each 
# representing a number. The nodes of the linked lists contain digits as values. 
# The nodes in the input lists are reversed this means that the least significant 
# digit of the number is the head. The function should return the head of a new 
# linked listed representing the sum of the input lists. The output list should 
# have it's digits reversed as well.
# Say we wanted to compute 621 + 354 normally. The sum is 975:
#    621
#  + 354
#  -----
#    975
# Then, the reversed linked list format of this problem would appear as:
#     1 -> 2 -> 6
#  +  4 -> 5 -> 3
#  --------------
#     5 -> 7 -> 9
#
# test_00:
#   621
# + 354
# -----
#   975
# a1 = Node(1)
# a2 = Node(2)
# a3 = Node(6)
# a1.next = a2
# a2.next = a3
# 1 -> 2 -> 6
# b1 = Node(4)
# b2 = Node(5)
# b3 = Node(3)
# b1.next = b2
# b2.next = b3
# 4 -> 5 -> 3
# addLists(a1, b1)
# 5 -> 7 -> 9
# test_01:
#  7541
# +  32
# -----
#  7573
# a1 = Node(1)
# a2 = Node(4)
# a3 = Node(5)
# a4 = Node(7)
# a1.next = a2
# a2.next = a3
# a3.next = a4
# 1 -> 4 -> 5 -> 7
# b1 = Node(2)
# b2 = Node(3)
# b1.next = b2
# 2 -> 3 
# addLists(a1, b1)
# 3 -> 7 -> 5 -> 7
# test_02:
#   39
# + 47
# ----
#   86
# a1 = Node(9)
# a2 = Node(3)
# a1.next = a2
# 9 -> 3
# b1 = Node(7)
# b2 = Node(4)
# b1.next = b2
# 7 -> 4
# addLists(a1, b1)
# 6 -> 8
# test_03:
#   89
# + 47
# ----
#  136
# a1 = Node(9)
# a2 = Node(8)
# a1.next = a2
# 9 -> 8
# b1 = Node(7)
# b2 = Node(4)
# b1.next = b2
# 7 -> 4
# addLists(a1, b1)
# 6 -> 3 -> 1
# test_04:
#   999
#  +  6
#  ----
#  1005
# a1 = Node(9)
# a2 = Node(9)
# a3 = Node(9)
# a1.next = a2
# a2.next = a3
# 9 -> 9 -> 9
# b1 = Node(6)
# 6
# addLists(a1, b1)
# 5 -> 0 -> 0 -> 1

# ========================= Iterative =========================
# Time: O(min(n, m)), Space: O(min(n, m))
def add_lists(head_1, head_2):
  puppet_head = Node(None)
  tail = puppet_head

  carry = 0
  current_1 = head_1
  current_2 = head_2 
  while current_1 is not None or current_2 is not None or carry == 1:
    val_1 = 0 if current_1 is None else current_1.val
    val_2 = 0 if current_2 is None else current_2.val
    sum = val_1 + val_2 + carry
    digit = sum % 10
    carry = 1 if sum > 9 else 0

    tail.next = Node(digit)
    tail = tail.next
    current_1 = current_1.next if current_1 is not None else None
    current_2 = current_2.next if current_2 is not None else None
  
  return puppet_head.next

# ========================= Recursive =========================
# Time: O(min(n, m)), Space: O(min(n, m))
def add_lists(head_1, head_2, carry = 0):
  if head_1 is None and head_2 is None and carry == 0:
    return None

  val_1 = 0 if head_1 is None else head_1.val
  val_2 = 0 if head_2 is None else head_2.val
  sum = val_1 + val_2 + carry
  digit = sum % 10
  carry = 1 if sum > 9 else 0

  node = Node(digit)
  next_1 = head_1.next if head_1 is not None else None
  next_2 = head_2.next if head_2 is not None else None
  node.next = add_lists(next_1, next_2, carry)

  return node

# [[[[[[[[[[[[[[[[[[[[[[[[[ #24 depth first values ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, depth_first_values, that takes in the root of a binary tree. 
# The function should return an list containing all values of the tree in 
# depth-first order.
#
# test_00:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# depth_first_values(a) 
#    -> ['a', 'b', 'd', 'e', 'c', 'f']
# test_01:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g
# depth_first_values(a) 
#    -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
# test_02:
# a = Node('a')
#      a
# depth_first_values(a) 
#    -> ['a']
# test_03:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# a.right = b
# b.left = c
# c.right = d
# d.right = e
#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e
# depth_first_values(a) 
#    -> ['a', 'b', 'c', 'd', 'e']
# test_04:
# howHigh(None) 
#    -> []

# ========================= Iterative =========================
# Time: O(n), Space: O(n)
def depth_first_values(root):
  if not root:
    return []

  values = []
  stack = [root]
  while stack:
    current = stack.pop()
    values.append(current.val)
    if current.right is not None:
      stack.append(current.right)
    if current.left is not None:
      stack.append(current.left)
  return values

# ========================= Recursive =========================
# Time: O(n), Space: O(n)
def depth_first_values(root):
  if root is None:
    return []
    
  left_values = depth_first_values(root.left)
  right_values = depth_first_values(root.right)
  return [root.val, *left_values, *right_values]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #25 breadth first values ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, breadth_first_values, that takes in the root of a binary tree.
# The function should return an list containing all values of the tree in 
# breadth-first order.
#
# test_00:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# breadth_first_values(a) 
#    -> ['a', 'b', 'c', 'd', 'e', 'f']
# test_01:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# h = Node('h')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
# breadth_first_values(a) 
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# test_02:
# a = Node('a')
#      a
# breadth_first_values(a) 
#    -> ['a']
# test_03:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# x = Node('x')
# a.right = b
# b.left = c
# c.left = x
# c.right = d
# d.right = e
#      a
#       \
#        b
#       /
#      c
#    /  \
#   x    d
#         \
#          e
# breadth_first_values(a) 
#    -> ['a', 'b', 'c', 'x', 'd', 'e']
# test_04:
# howHigh(None) 
#    -> []

# ========================= Breadth First =========================
# Time: O(n), Space: O(n)
from collections import deque

def breadth_first_values(root):
  if root is None:
    return []

  values = []
  queue = deque([root])
  while queue:
    current = queue.popleft()
    values.append(current.val)
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return values

# [[[[[[[[[[[[[[[[[[[[[[[[[ #26 tree includes ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, tree_includes, that takes in the root of a binary tree and 
# a target value. The function should return a boolean indicating whether or 
# not the value is contained in the tree.
#
# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# tree_includes(a, "e") # -> true
# test_01:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# tree_includes(a, "a") # -> true
# test_02:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# tree_includes(a, "n") # -> false
# test_03:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# g = Node("g")
# h = Node("h")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
# tree_includes(a, "f") # -> true
# test_04:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# g = Node("g")
# h = Node("h")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
# tree_includes(a, "p") # -> false
# test_05:
# tree_includes(None, "b") # -> false

# ========================= Breadth First =========================
# Time: O(n), Space: O(n)
from collections import deque

def tree_includes(root, target):
  if root is None:
    return False
  
  queue = deque([root])
  while queue:
    current = queue.popleft()
    if current.val is target:
      return True
    
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
  return False

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def tree_includes(root, target):
  if root is None:
    return False
  if root.val is target:
    return True
  
  left_inclusion = tree_includes(root.left, target)
  right_inclusion = tree_includes(root.right, target)
  return left_inclusion or right_inclusion

# [[[[[[[[[[[[[[[[[[[[[[[[[ #27 tree sum ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, treeSum, that takes in the root of a binary tree that 
# contains number values. The function should return the total sum of all values
# in the tree.
#
# test_00:
# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
# treeSum(a) # -> 21
# test_01:
# a = Node(1)
# b = Node(6)
# c = Node(0)
# d = Node(3)
# e = Node(-6)
# f = Node(2)
# g = Node(2)
# h = Node(2)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h
#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2
# treeSum(a) # -> 10
# test_02:
# treeSum(None) # -> 0

# ========================= Breadth First =========================
# Time: O(n), Space: O(n)
def tree_sum(root):
  if root is None:
    return 0
  
  sum = 0
  queue = deque([root])
  while queue:
    node = queue.popleft()
    sum += node.val
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return sum

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def tree_sum(root):
  if root is None:
    return 0
  
  return root.val + tree_sum(root.left) + tree_sum(root.right)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #28 tree min value ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, treeMinValue, that takes in the root of a binary tree that 
# contains number values. The function should return the minimum value within 
# the tree.
# You may assume that the input tree is non-empty.
#
# test_00:
# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
# treeMinValue(a) # -> -2
# test_01:
# a = Node(5)
# b = Node(11)
# c = Node(3)
# d = Node(4)
# e = Node(14)
# f = Node(12)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#       5
#    /    \
#   11     3
#  / \      \
# 4   15     12
# treeMinValue(a) # -> 3
# test_02:
# a = Node(-1)
# b = Node(-6)
# c = Node(-5)
# d = Node(-3)
# e = Node(-4)
# f = Node(-13)
# g = Node(-2)
# h = Node(-2)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     /       \
#    -2       -2
# tree_min_value(a) # -> -13
# test_03:
# a = Node(42)
#        42
# tree_min_value(a) # -> 42

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def tree_min_value(root):
  if root == None:
    return float('inf')

  left = tree_min_value(root.left)
  right = tree_min_value(root.right)
  return min(root.val, left, right)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #29 max path sum ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, max_path_sum, that takes in the root of a binary tree that 
# contains number values. The function should return the maximum sum of any root
# to leaf path within the tree.
# You may assume that the input tree is non-empty.
#
# test_00:
# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      3
#    /   \
#   11    4
#  / \     \
# 4   -2    1
# max_path_sum(a) # -> 18
# test_01:
# a = Node(5)
# b = Node(11)
# c = Node(54)
# d = Node(20)
# e = Node(15)
# f = Node(1)
# g = Node(3)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# e.left = f
# e.right = g
#       5
#     /   \
#    11   54
#  /   \
# 20   15
#      / \
#     1  3
# max_path_sum(a) # -> 59
# test_02:
# a = Node(-1)
# b = Node(-6)
# c = Node(-5)
# d = Node(-3)
# e = Node(0)
# f = Node(-13)
# g = Node(-1)
# h = Node(-2)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   0    -13
#     /       \
#    -1       -2
# max_path_sum(a) # -> -8
# test_03:
# a = Node(42)
#        42
# max_path_sum(a) # -> 42

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def max_path_sum(root):
  if root is None:
    return float('-inf')
  if root.left is None and root.right is None:
    return root.val
  
  left = max_path_sum(root.left)
  right = max_path_sum(root.right)
  return root.val + max(left, right)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #30 path finder ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, path_finder, that takes in the root of a binary tree and a 
# target value. The function should return an list representing a path to the 
# target value. If the target value is not found in the tree, then return None.
# You may assume that the tree contains unique values.
#
# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]
# test_01:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# path_finder(a, 'p') # -> None
# test_02:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# g = Node("g")
# h = Node("h")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
# path_finder(a, "c") # -> ['a', 'c']
# test_03:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# g = Node("g")
# h = Node("h")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
# path_finder(a, "h") # -> ['a', 'c', 'f', 'h']
# test_04:
# x = Node("x")
#      x
# path_finder(x, "x") # -> ['x']
# test_05:
# path_finder(None, "x") # -> None
# test_06:
# root = Node(0)
# let curr = root
# for (let i = 1 i <= 6000 i += 1) {
#   curr.right = Node(i)
#   curr = curr.right
# }
#      0
#       \
#        1
#         \
#          2
#           \
#            3
#             .
#              .
#               .
#              5999
#                \
#                6000
# path_finder(root, 3451) # -> [0, 1, 2, 3, ..., 3450, 3451]

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def path_finder(root, target):
  path = _path_finder(root, target)
  if path is not None:
    return path[::-1]
  return None

def _path_finder(root, target):
  if root is None:
    return None
  if root.val == target:
    return [root.val]

  left_path = _path_finder(root.left, target)
  if left_path is not None:
    left_path.append(root.val)
    return left_path

  right_path = _path_finder(root.right, target)
  if right_path is not None:
    right_path.append(root.val)
    return right_path

  return None

# [[[[[[[[[[[[[[[[[[[[[[[[[ #31 tree value count ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, tree_value_count, that takes in the root of a binary tree and
# a target value. The function should return the number of times that the target
# occurs in the tree.
#
# test_00:
# a = Node(12)
# b = Node(6)
# c = Node(6)
# d = Node(4)
# e = Node(6)
# f = Node(12)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#     12
#    /  \
#   6    6
#  / \    \
# 4   6    12
# tree_value_count(a,  6) # -> 3
# test_01:
# a = Node(12)
# b = Node(6)
# c = Node(6)
# d = Node(4)
# e = Node(6)
# f = Node(12)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#     12
#    /  \
#   6    6
#  / \    \
# 4   6    12
# tree_value_count(a,  12) # -> 2
# test_02:
# a = Node(7)
# b = Node(5)
# c = Node(1)
# d = Node(1)
# e = Node(8)
# f = Node(7)
# g = Node(1)
# h = Node(1)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h
#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1
# tree_value_count(a, 1) # -> 4
# test_03:
# a = Node(7)
# b = Node(5)
# c = Node(1)
# d = Node(1)
# e = Node(8)
# f = Node(7)
# g = Node(1)
# h = Node(1)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h
#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1
# tree_value_count(a, 9) # -> 0
# test_04:
# tree_value_count(None, 42) # -> 0

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def tree_value_count(root, target):
  if root is None:
    return 0
  
  count = 0
  if root.val == target:
    count += 1
  
  return count + tree_value_count(root.left) + tree_value_count(root.right)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #32 how high ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, how_high, that takes in the root of a binary tree. The 
# function should return a number representing the height of the tree.
# The height of a binary tree is defined as the maximal number of edges from 
# the root node to any leaf node.
# If the tree is empty, return -1.
#
# test_00:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# how_high(a) # -> 2
# test_01:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g
# how_high(a) # -> 3
# test_02:
# a = Node('a')
# c = Node('c')
# a.right = c
#      a
#       \
#        c
# how_high(a) # -> 1
# test_03:
# a = Node('a')
#      a
# how_high(a) # -> 0

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def how_high(root, i = 0):
  if root is None:
    return i - 1
  
  left = how_high(root.left, i + 1)
  right = how_high(root.right, i + 1)
  return max(left, right)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #33 bottom right value ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, bottom_right_value, that takes in the root of a binary tree. 
# The function should return the right-most value in the bottom-most level of 
# the tree.
# You may assume that the input tree is non-empty.
#
# test_00:
# a = Node(3)
# b = Node(11)
# c = Node(10)
# d = Node(4)
# e = Node(-2)
# f = Node(1)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#       3
#    /    \
#   11     10
#  / \      \
# 4   -2     1
# bottom_right_value(a) # -> 1
# test_01:
# a = Node(-1)
# b = Node(-6)
# c = Node(-5)
# d = Node(-3)
# e = Node(-4)
# f = Node(-13)
# g = Node(-2)
# h = Node(6)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# e.right = h
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \       
#    -2  6
# bottom_right_value(a) # -> 6
# test_02:
# a = Node(-1)
# b = Node(-6)
# c = Node(-5)
# d = Node(-3)
# e = Node(-4)
# f = Node(-13)
# g = Node(-2)
# h = Node(6)
# i = Node(7)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# e.right = h
# f.left = i
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \    /   
#    -2  6  7 
# bottom_right_value(a) # -> 7
# test_03
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# a.left = b
# a.right = c
# b.right = d
# d.left = e
# e.right = f
#      a
#    /   \ 
#   b     c
#    \
#     d
#    /
#   e
#  /
# f
#       
# bottom_right_value(a) # -> 'f'
# test_04
# a = Node(42)
#      42
# bottom_right_value(a) # -> 42

# ========================= Breadth First =========================
# Time: O(n), Space: O(1)
from collections import deque

def bottom_right_value(root):
  result = None
  queue = deque([root])
  while queue:
    node = queue.popleft()
    result = node
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return result.val

# [[[[[[[[[[[[[[[[[[[[[[[[[ #34 all tree paths ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, all_tree_paths, that takes in the root of a binary tree. The
# function should return a 2-Dimensional list where each sublist represents a
# root-to-leaf path in the tree.
# The order within an individual path must start at the root and end at the leaf,
# but the relative order of among paths in the outer list does not matter.
# You may assume that the input tree is non-empty.
#
# test_00:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# all_tree_paths(a) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e' ], 
#   [ 'a', 'c', 'f' ] 
# ] 
# test_01:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# h = Node('h')
# i = Node('i')
# a.l#eft = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# e.right = h
# f.left = i
#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /   
#     g  h   i 
# all_tree_paths(a) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e', 'g' ], 
#   [ 'a', 'b', 'e', 'h' ], 
#   [ 'a', 'c', 'f', 'i' ] 
# ] 
# test_02:
# q = Node('q')
# r = Node('r')
# s = Node('s')
# t = Node('t')
# u = Node('u')
# v = Node('v')
# q.left = r
# q.right = s
# r.right = t
# t.left = u
# u.right = v
#      q
#    /   \ 
#   r     s
#    \
#     t
#    /
#   u
#  /
# v
# all_tree_paths(q) # ->
# [ 
#   [ 'q', 'r', 't', 'u', 'v' ], 
#   [ 'q', 's' ] 
# ] 
# test_03:
# z = Node('z')
#      z
# all_tree_paths(z) # -> 
# [
#   ['z']
# ]

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def all_tree_paths(root):
  if root is None:
    return []
  if root.left is None and root.right is None:
    return [[root.val]]
  
  paths = []

  left_paths = all_tree_paths(root.left)
  for path in left_paths:
    paths.append([root.val, *path])

  right_paths = all_tree_paths(root.right)
  for path in right_paths:
    paths.append([root.val, *path])

  return paths


# [[[[[[[[[[[[[[[[[[[[[[[[[ #35 tree levels ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, tree_levels, that takes in the root of a binary tree. The 
# function should return a 2-Dimensional list where each sublist represents a
# level of the tree.
#
# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]
# test_01:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# g = Node("g")
# h = Node("h")
# i = Node("i")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# e.right = h
# f.left = i
#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /
#     g  h   i
# tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f'],
#   ['g', 'h', 'i']
# ]
# test_02:
# q = Node("q")
# r = Node("r")
# s = Node("s")
# t = Node("t")
# u = Node("u")
# v = Node("v")
# q.left = r
# q.right = s
# r.right = t
# t.left = u
# u.right = v
#      q
#    /   \
#   r     s
#    \
#     t
#    /
#   u
#  /
# v
# tree_levels(q) #->
# [
#   ['q'],
#   ['r', 's'],
#   ['t'],
#   ['u'],
#   ['v']
# ]
# test_03:
# tree_levels(None) # -> []

# ========================= Breadth First =========================
# Time: O(n), Space: O(n)
from collections import deque

def tree_levels(root):
  if root is None:
    return []

  levels = []
  queue = deque([(root, 0)])
  while queue:
    node, level = queue.popleft()

    if len(levels) == level:
      levels.append([ node.val ])
    else:
      levels[level].append(node.val)
    
    if node.left:
      queue.append((node.left, level + 1))
    if node.right:
      queue.append((node.right, level + 1))
  
  return levels

# [[[[[[[[[[[[[[[[[[[[[[[[[ #36 level averages ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, level_averages, that takes in the root of a binary tree that
# contains number values. The function should return an list containing the 
# average value of each level.
#
# test_00:
# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
# level_averages(a) # -> [ 3, 7.5, 1 ] 
# test_01:
# a = Node(5)
# b = Node(11)
# c = Node(54)
# d = Node(20)
# e = Node(15)
# f = Node(1)
# g = Node(3)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# e.left = f
# e.right = g
#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3
# level_averages(a) # -> [ 5, 32.5, 17.5, 2 ] 
# test_02:
# a = Node(-1)
# b = Node(-6)
# c = Node(-5)
# d = Node(-3)
# e = Node(0)
# f = Node(45)
# g = Node(-1)
# h = Node(-2)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   0     45
#     /       \
#    -1       -2
# level_averages(a) # -> [ -1, -5.5, 14, -1.5 ]
# test_03:
# q = Node(13)
# r = Node(4)
# s = Node(2)
# t = Node(9)
# u = Node(2)
# v = Node(42)
# q.left = r
# q.right = s
# r.right = t
# t.left = u
# u.right = v
#        13
#      /   \
#     4     2
#      \
#       9
#      /
#     2
#    /
#   42
# level_averages(q) # -> [ 13, 3, 9, 2, 42 ]
# test_04:
# level_averages(None) # -> [ ]

# ========================= Breadth First =========================
# Time: O(n), Space: O(n)
from collections import deque
from statistics import mean

def level_averages(root):
  if root is None:
    return []

  levels = tree_levels(root)
  for i in range(len(levels)):
    levels[i] = mean(levels[i])

  return levels 

def tree_levels(root):
  if root is None:
    return []

  levels = []
  queue = deque([(root, 0)])
  while queue:
    node, level = queue.popleft()

    if len(levels) == level:
      levels.append([ node.val ])
    else:
      levels[level].append(node.val)
    
    if node.left:
      queue.append((node.left, level + 1))
    if node.right:
      queue.append((node.right, level + 1))
  
  return levels

# [[[[[[[[[[[[[[[[[[[[[[[[[ #37 leaf list ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, leaf_list, that takes in the root of a binary tree and 
# returns an list containing the values of all leaf nodes in left-to-right order.
#
# test_00:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# leaf_list(a) # -> [ 'd', 'e', 'f' ] 
# test_01:
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
# g = Node("g")
# h = Node("h")
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
# leaf_list(a) # -> [ 'd', 'g', 'h' ]
# test_02:
# a = Node(5)
# b = Node(11)
# c = Node(54)
# d = Node(20)
# e = Node(15)
# f = Node(1)
# g = Node(3)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# e.left = f
# e.right = g
#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3
# leaf_list(a) # -> [ 20, 1, 3, 54 ]
# test_03:
# x = Node('x')
#      x
# leaf_list(x) # -> [ 'x' ]
# test_04:
# leaf_list(None) # -> [ ]

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def leaf_list(root, values = []):
  if root is None:
    return values 
  
  if root.left is None and root.right is None:
    values.append(root.val)

  leaf_list(root.left, values)
  leaf_list(root.right, values)

  return values

# [[[[[[[[[[[[[[[[[[[[[[[[[ #38 has path ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, has_path, that takes in an object representing the adjacency
# list of a directed acyclic graph and two nodes (src, dst). The function should
# return a boolean indicating whether or not there exists a directed path between
# the source and destination nodes.
#
# test_00:
# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }
# has_path(graph, 'f', 'k') # true
# test_01:
# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }
# has_path(graph, 'f', 'j') # false
# test_02:
# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }
# has_path(graph, 'i', 'h') # true
# test_03:
# graph = {
#   'v': ['x', 'w'],
#   'w': [],
#   'x': [],
#   'y': ['z'],
#   'z': [],  
# }
# has_path(graph, 'v', 'w') # true
# test_04:
# graph = {
#   'v': ['x', 'w'],
#   'w': [],
#   'x': [],
#   'y': ['z'],
#   'z': [],  
# }
# has_path(graph, 'v', 'z') # false

# ========================= Depth First =========================
# Time: O(e), Space: O(n)
def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for node in graph[src]:
    if has_path(graph, node, dst):
      return True
  
  return False

# [[[[[[[[[[[[[[[[[[[[[[[[[ #39 undirected path ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, undirected_path, that takes in an list of edges for an 
# undirected graph and two nodes (nodeA, nodeB). The function should return a 
# boolean indicating whether or not there exists a path between nodeA and nodeB.
#
# test_00:
# edges = [
#   ['i', 'j'],
#   ['k', 'i'],
#   ['m', 'k'],
#   ['k', 'l'],
#   ['o', 'n']
# ]
# undirected_path(edges, 'j', 'm') # -> true
# test_01:
# edges = [
#   ['i', 'j'],
#   ['k', 'i'],
#   ['m', 'k'],
#   ['k', 'l'],
#   ['o', 'n']
# ]
# undirected_path(edges, 'm', 'j') # -> true
# test_02:
# edges = [
#   ['i', 'j'],
#   ['k', 'i'],
#   ['m', 'k'],
#   ['k', 'l'],
#   ['o', 'n']
# ]
# undirected_path(edges, 'l', 'j') # -> true
# test_03:
# edges = [
#   ['i', 'j'],
#   ['k', 'i'],
#   ['m', 'k'],
#   ['k', 'l'],
#   ['o', 'n']
# ]
# undirected_path(edges, 'k', 'o') # -> false
# test_04:
# edges = [
#   ['i', 'j'],
#   ['k', 'i'],
#   ['m', 'k'],
#   ['k', 'l'],
#   ['o', 'n']
# ]
# undirected_path(edges, 'i', 'o') # -> false
# test_05:
# edges = [
#   ['b', 'a'],
#   ['c', 'a'],
#   ['b', 'c'],
#   ['q', 'r'],
#   ['q', 's'],
#   ['q', 'u'],
#   ['q', 't'],
# ]
# undirected_path(edges, 'a', 'b') # -> true
# test_06:
# edges = [
#   ['b', 'a'],
#   ['c', 'a'],
#   ['b', 'c'],
#   ['q', 'r'],
#   ['q', 's'],
#   ['q', 'u'],
#   ['q', 't'],
# ]
# undirected_path(edges, 'a', 'c') # -> true
# test_07:
# edges = [
#   ['b', 'a'],
#   ['c', 'a'],
#   ['b', 'c'],
#   ['q', 'r'],
#   ['q', 's'],
#   ['q', 'u'],
#   ['q', 't'],
# ]
# undirected_path(edges, 'r', 't') # -> true
# test_08:
# edges = [
#   ['b', 'a'],
#   ['c', 'a'],
#   ['b', 'c'],
#   ['q', 'r'],
#   ['q', 's'],
#   ['q', 'u'],
#   ['q', 't'],
# ]
# undirected_path(edges, 'r', 'b') # -> false

# ========================= Depth First =========================
# Time: O(e), Space: O(n)
def undirected_path(edges, node_A, node_B, visited = set()):
  graph = build_graph(edges)

  if node_A in visited:
    return False
  if node_A == node_B:
    return True

  visited.add(node_A)
  for node in graph[node_A]:
    if undirected_path(edges, node, node_B):
      return True

  return False

def build_graph(edges):
  graph = {}
  for edge in edges:
    src, dst = edge
    if src not in graph:
      graph[src] = []
    if dst not in graph:
      graph[dst] = []
    graph[src].append(dst)
    graph[dst].append(src)
  return graph

# [[[[[[[[[[[[[[[[[[[[[[[[[ #40 connected components count ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, connected_components_count, that takes in the adjacency list 
# of an undirected graph. The function should return the number of connected 
# components within the graph.
#
# test_00:
# connected_components_count({
#   0: [8, 1, 5],
#   1: [0],
#   5: [0, 8],
#   8: [0, 5],
#   2: [3, 4],
#   3: [2, 4],
#   4: [3, 2]
# }) # -> 2
# test_01:
# connected_components_count({
#   1: [2],
#   2: [1,8],
#   6: [7],
#   9: [8],
#   7: [6, 8],
#   8: [9, 7, 2]
# }) # -> 1
# test_02:
# connected_components_count({
#   3: [],
#   4: [6],
#   6: [4, 5, 7, 8],
#   8: [6],
#   7: [6],
#   5: [6],
#   1: [2],
#   2: [1]
# }) # -> 3
# test_03:
# connected_components_count({}) # -> 0
# test_04:
# connected_components_count({
#   0: [4,7],
#   1: [],
#   2: [],
#   3: [6],
#   4: [0],
#   6: [3],
#   7: [0],
#   8: []
# }) # -> 5

# ========================= Depth First =========================
# Time: O(e), Space: O(n)
def connected_components_count(graph):
  count = 0
  visited = set()

  for node in graph:
    if node not in visited:
      count += 1
      traverse(graph, node, visited)
  return count

def traverse(graph, node, visited):
  if node in visited:
    return

  visited.add(node)
  for neighbor in graph[node]:
    traverse(graph, neighbor, visited)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #41 largest component ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, largest_component, that takes in the adjacency list of an 
# undirected graph. The function should return the size of the largest connected
# component in the graph.
#
# test_00:
# largest_component({
#   0: ['8', '1', '5'],
#   1: ['0'],
#   5: ['0', '8'],
#   8: ['0', '5'],
#   2: ['3', '4'],
#   3: ['2', '4'],
#   4: ['3', '2']
# }) # -> 4
# test_01:
# largest_component({
#   1: ['2'],
#   2: ['1','8'],
#   6: ['7'],
#   9: ['8'],
#   7: ['6', '8'],
#   8: ['9', '7', '2']
# }) # -> 6
# test_02:
# largest_component({
#   3: [],
#   4: ['6'],
#   6: ['4', '5', '7', '8'],
#   8: ['6'],
#   7: ['6'],
#   5: ['6'],
#   1: ['2'],
#   2: ['1']
# }) # -> 5
# test_03:
# largest_component({}) # -> 0
# test_04:
# largest_component({
#   0: ['4','7'],
#   1: [],
#   2: [],
#   3: ['6'],
#   4: ['0'],
#   6: ['3'],
#   7: ['0'],
#   8: []
# }) # -> 3

# ========================= Depth First =========================
# Time: O(e), Space: O(n)
def largest_component(graph):
  visited = set()
  largest = 0

  for node in graph:
    if node not in visited:
      size = component_size(graph, node, visited)
      largest = largest if largest > size else size
  return largest

def component_size(graph, node, visited):
  if node in visited:
    return 0

  visited.add(node)
  size = 1
  for neighbor in graph[node]:
    size += component_size(graph, neighbor, visited)

  return size

# [[[[[[[[[[[[[[[[[[[[[[[[[ #42 shortest path ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, shortest_path, that takes in an list of edges for an 
# undirected graph and two nodes (nodeA, nodeB). The function should return the
# length of the shortest path between A and B. Consider the length as the number
# of edges in the path, not the number of nodes. If there is no path between A 
# and B, then return -1.
#
# test_00:
# edges = [
#   ['w', 'x'],
#   ['x', 'y'],
#   ['z', 'y'],
#   ['z', 'v'],
#   ['w', 'v']
# ]
# shortest_path(edges, 'w', 'z') # -> 2
# test_01:
# edges = [
#   ['w', 'x'],
#   ['x', 'y'],
#   ['z', 'y'],
#   ['z', 'v'],
#   ['w', 'v']
# ]
# shortest_path(edges, 'y', 'x') # -> 1
# test_02:
# edges = [
#   ['a', 'c'],
#   ['a', 'b'],
#   ['c', 'b'],
#   ['c', 'd'],
#   ['b', 'd'],
#   ['e', 'd'],
#   ['g', 'f']
# ]
# shortest_path(edges, 'a', 'e') # -> 3
# test_03:
# edges = [
#   ['a', 'c'],
#   ['a', 'b'],
#   ['c', 'b'],
#   ['c', 'd'],
#   ['b', 'd'],
#   ['e', 'd'],
#   ['g', 'f']
# ]
# shortest_path(edges, 'e', 'c') # -> 2
# test_04:
# edges = [
#   ['a', 'c'],
#   ['a', 'b'],
#   ['c', 'b'],
#   ['c', 'd'],
#   ['b', 'd'],
#   ['e', 'd'],
#   ['g', 'f']
# ]
# shortest_path(edges, 'b', 'g') # -> -1
# test_05:
# edges = [
#   ['c', 'n'],
#   ['c', 'e'],
#   ['c', 's'],
#   ['c', 'w'],
#   ['w', 'e'],
# ]
# shortest_path(edges, 'w', 'e') # -> 1
# test_06:
# edges = [
#   ['c', 'n'],
#   ['c', 'e'],
#   ['c', 's'],
#   ['c', 'w'],
#   ['w', 'e'],
# ]
# shortest_path(edges, 'n', 'e') # -> 2
# test_07:
# edges = [
#   ['m', 'n'],
#   ['n', 'o'],
#   ['o', 'p'],
#   ['p', 'q'],
#   ['t', 'o'],
#   ['r', 'q'],
#   ['r', 's']
# ]
# shortest_path(edges, 'm', 's') # -> 6

# ========================= Depth First =========================
# Time: O(e), Space: O(e)
from collections import deque

def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)

  queue = deque([ (node_A, 0) ])
  while queue:
    node, length = queue.popleft()
    if node == node_B:
      return length
    for neighbor in graph[node]:
      queue.append((neighbor, length + 1))
    
  return -1

def build_graph(edges):
  graph = {}

  for edge in edges:
    a, b = edge
    if a not in graph:
      a = []
    if b not in graph:
      b = []
    graph[a].append(b)
    graph[b].append(a)

  return graph

# [[[[[[[[[[[[[[[[[[[[[[[[[ #43 island count ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, island_count, that takes in a grid containing Ws and Ls. W 
# represents water and L represents land. The function should return the number
# of islands on the grid. An island is a vertically or horizontally connected 
# region of land.
#
# test_00:
# grid = [
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'W', 'W', 'L', 'W'],
#   ['W', 'W', 'L', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['L', 'L', 'W', 'W', 'W'],
# ]
# island_count(grid) # -> 3
# test_01:
# grid = [
#   ['L', 'W', 'W', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['W', 'L', 'W', 'L', 'W'],
#   ['W', 'W', 'W', 'W', 'W'],
#   ['W', 'W', 'L', 'L', 'L'],
# ]
# island_count(grid) # -> 4
# test_02:
# grid = [
#   ['L', 'L', 'L'],
#   ['L', 'L', 'L'],
#   ['L', 'L', 'L'],
# ]
# island_count(grid) # -> 1
# test_03:
# grid = [
#   ['W', 'W'],
#   ['W', 'W'],
#   ['W', 'W'],
# ]
# island_count(grid) # -> 0

# ========================= Depth First =========================
# Time: O(rc), Space: O(rc)
def island_count(grid):
  visited = set()
  count = 0

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      pos = (r, c)
      if pos not in visited and grid[r][c] == 'L':
        count += 1
        traverse_land(grid, r, c, visited)
  
  return count

def traverse_land(grid, r, c, visited):
  if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]):
    return
  if grid[r][c] == 'W' or (r, c) in visited:
    return

  visited.add((r, c))
  traverse_land(grid, r + 1, c, visited)
  traverse_land(grid, r, c + 1, visited)
  traverse_land(grid, r - 1, c, visited)
  traverse_land(grid, r, c - 1, visited)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #44 minimum island ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, minimum_island, that takes in a grid containing Ws and Ls. 
# W represents water and L represents land. The function should return the size
# of the smallest island. An island is a vertically or horizontally connected 
# region of land.
# You may assume that the grid contains at least one island.
#
# test_00:
# grid = [
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'W', 'W', 'L', 'W'],
#   ['W', 'W', 'L', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['L', 'L', 'W', 'W', 'W'],
# ]
# minimum_island(grid) # -> 2
# test_01:
# grid = [
#   ['L', 'W', 'W', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['W', 'L', 'W', 'L', 'W'],
#   ['W', 'W', 'W', 'W', 'W'],
#   ['W', 'W', 'L', 'L', 'L'],
# ]
# minimum_island(grid) # -> 1
# test_02:
# grid = [
#   ['L', 'L', 'L'],
#   ['L', 'L', 'L'],
#   ['L', 'L', 'L'],
# ]
# minimum_island(grid) # -> 9
# test_03:
# grid = [
#   ['W', 'W'],
#   ['L', 'L'],
#   ['W', 'W'],
#   ['W', 'L']
# ]
# minimum_island(grid) # -> 1

# ========================= Depth First =========================
# Time: O(rc), Space: O(rc)
def minimum_island(grid):
  visited = set()
  min_size = float('inf')

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if (r, c) not in visited and grid[r][c] == 'L':
        size = land_size(grid, r, c, visited)
        min_size = min_size if min_size < size else size

  return min_size

def land_size(grid, r, c, visited):
  if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]):
    return 0
  if grid[r][c] == 'W' or (r, c) in visited:
    return 0

  size = 1
  visited.add((r, c))
  size += land_size(grid, r + 1, c, visited)
  size += land_size(grid, r, c + 1, visited)
  size += land_size(grid, r - 1, c, visited)
  size += land_size(grid, r, c - 1, visited)
  return size
  
# [[[[[[[[[[[[[[[[[[[[[[[[[ #45 closest carrot ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, closest_carrot, that takes in a grid, a starting row, and a 
# starting column. In the grid, 'X's are walls, 'O's are open spaces, and 'C's 
# are carrots. The function should return a number representing the length of 
# the shortest path from the starting position to a carrot. You may move up, 
# down, left, or right, but cannot pass through walls (X). If there is no 
# possible path to a carrot, then return -1.
# 
# test_00:
# grid = [
#   ['O', 'O', 'O', 'O', 'O'],
#   ['O', 'X', 'O', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['O', 'X', 'C', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['C', 'O', 'O', 'O', 'O'],
# ]
# closest_carrot(grid, 1, 2) # -> 4
# test_01:
# grid = [
#   ['O', 'O', 'O', 'O', 'O'],
#   ['O', 'X', 'O', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['O', 'X', 'C', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['C', 'O', 'O', 'O', 'O'],
# ]
# closest_carrot(grid, 0, 0) # -> 5
# test_02:
# grid = [
#   ['O', 'O', 'X', 'X', 'X'],
#   ['O', 'X', 'X', 'X', 'C'],
#   ['O', 'X', 'O', 'X', 'X'],
#   ['O', 'O', 'O', 'O', 'O'],
#   ['O', 'X', 'X', 'X', 'X'],
#   ['O', 'O', 'O', 'O', 'O'],
#   ['O', 'O', 'C', 'O', 'O'],
#   ['O', 'O', 'O', 'O', 'O'],
# ]
# closest_carrot(grid, 3, 4) # -> 9
# test_03:
# grid = [
#   ['O', 'O', 'X', 'O', 'O'],
#   ['O', 'X', 'X', 'X', 'O'],
#   ['O', 'X', 'C', 'C', 'O'],
# ]
# closest_carrot(grid, 1, 4) # -> 2
# test_04:
# grid = [
#   ['O', 'O', 'X', 'O', 'O'],
#   ['O', 'X', 'X', 'X', 'O'],
#   ['O', 'X', 'C', 'C', 'O'],
# ]
# closest_carrot(grid, 2, 0) # -> -1

# ========================= Breadth First =========================
# Time: O(rc), Space: O(rc)
from collections import deque

def closest_carrot(grid, row, col):
  visited = set()
  deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  queue = deque([[row, col, 0]])
  while queue:
    r, c, dst = queue.popleft()
    visited.add((r, c))
    if grid[r][c] == 'C':
      return dst
    for delta in deltas:
      delta_y, delta_x = delta
      new_row = r + delta_y
      new_col = c + delta_x
      valid_row =_row >= 0 and new_row < len(grid)
      valid_col =_col >= 0 and new_col < len(grid[0])
      valid_pos = valid_row and valid_col
      visited_pos = (new_row, new_col) in visited
      if valid_pos and grid[new_row][new_col] != 'X' and not visited_pos:
        queue.append([new_row, new_col, dst + 1])

  return -1

# [[[[[[[[[[[[[[[[[[[[[[[[[ #46 longest path ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, longest_path, that takes in an adjacency list for a directed
# acyclic graph. The function should return the length of the longest path 
# within the graph. A path may start and end at any two nodes. The length of a
# path is considered the number of edges in the path, not the number of nodes.
#
# test_00:
# graph = {
#   'a': ['c', 'b'],
#   'b': ['c'],
#   'c': []
# }
# longest_path(graph) # -> 2
# test_01:
# graph = {
#   'a': ['c', 'b'],
#   'b': ['c'],
#   'c': [],
#   'q': ['r'],
#   'r': ['s', 'u', 't'],
#   's': ['t'],
#   't': ['u'],
#   'u': []
# }
# longest_path(graph) # -> 4
# test_02:
# graph = {
#   'h': ['i', 'j', 'k'],
#   'g': ['h'],
#   'i': [],
#   'j': [],
#   'k': [],
#   'x': ['y'],
#   'y': []
# }
# longest_path(graph) # -> 2
# test_03:
# graph = {
#   'a': ['b'],
#   'b': ['c'],
#   'c': [],
#   'e': ['f'],
#   'f': ['g'],
#   'g': ['h'],
#   'h': []
# }
# longest_path(graph) # -> 3

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def longest_path(graph):
  longest = float('-inf')
  for node in graph:
    length = traverse(graph, node)
    longest = length if longest < length else longest
  return longest

def traverse(graph, node):
  if not graph[node]:
    return 0
  max = 0
  for neighbor in graph[node]:
    length = traverse(graph, neighbor)
    max = max if max > length else length
  return 1 + max

# [[[[[[[[[[[[[[[[[[[[[[[[[ #47 semesters required ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, semesters_required, that takes in a number of courses (n) and
# a list of prerequisites as arguments. Courses have ids ranging from 0 through
# n - 1. A single prerequisite of [A, B] means that course A must be taken 
# before course B. Return the minimum number of semesters required to complete
# all n courses. There is no limit on how many courses you can take in a single
# semester, as long the prerequisites of a course are satisfied before taking it.
# Note that given prerequisite [A, B], you cannot take course A and course B
# concurrently in the same semester. You must take A in some semester before B.
# You can assume that it is possible to eventually complete all courses.
#
# test_00:
# num_courses = 6
# prereqs = [
#   [1, 2],
#   [2, 4],
#   [3, 5],
#   [0, 5],
# ]
# semesters_required(num_courses, prereqs) # -> 3
# test_01:
# num_courses = 7
# prereqs = [
#   [4, 3],
#   [3, 2],
#   [2, 1],
#   [1, 0],
#   [5, 2],
#   [5, 6],
# ]
# semesters_required(num_courses, prereqs) # -> 5
# test_02:
# num_courses = 5
# prereqs = [
#   [1, 0],
#   [3, 4],
#   [1, 2],
#   [3, 2],
# ]
# semesters_required(num_courses, prereqs) # -> 2
# test_03:
# num_courses = 12
# prereqs = []
# semesters_required(num_courses, prereqs) # -> 1
# test_04:
# num_courses = 3
# prereqs = [
#   [0, 2],
#   [0, 1],
#   [1, 2],
# ]
# semesters_required(num_courses, prereqs) # -> 3
# test_05:
# num_courses = 6
# prereqs = [
#   [3, 4],
#   [3, 0],
#   [3, 1],
#   [3, 2],
#   [3, 5],
# ]
# semesters_required(num_courses, prereqs) # -> 2

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def semesters_required(num_courses, prereqs):
  graph = build_graph(num_courses, prereqs)
  semesters = 1
  for course in graph:
    length = longest_education(graph, course)
    semesters = length if length > semesters else semesters
  return semesters

def build_graph(num_courses, prereqs):
  graph = {}
  for num in range(num_courses):
    graph[num] = []
  for pair in prereqs:
    prereq, course = pair
    graph[prereq].append(course)
  return graph

def longest_education(graph, course):
  if not graph[course]:
    return 1
  max = 0
  for next_course in graph[course]:
    length = longest_education(graph, next_course)
    max = length if length > max else max
  return max

# [[[[[[[[[[[[[[[[[[[[[[[[[ #48 best bridge ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, best_bridge, that takes in a grid as an argument. The grid 
# contains water (W) and land (L). There are exactly two islands in the grid. 
# An island is a vertically or horizontally connected region of land. Return 
# the minimum length bridge needed to connect the two islands. A bridge does not
# need to form a straight line.
#
# test_00:
# grid = [
#   ["W", "W", "W", "L", "L"],
#   ["L", "L", "W", "W", "L"],
#   ["L", "L", "L", "W", "L"],
#   ["W", "L", "W", "W", "W"],
#   ["W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W"],
# ]
# best_bridge(grid) # -> 1
# test_01:
# grid = [
#   ["W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W"],
#   ["L", "L", "W", "W", "L"],
#   ["W", "L", "W", "W", "L"],
#   ["W", "W", "W", "L", "L"],
#   ["W", "W", "W", "W", "W"],
# ]
# best_bridge(grid) # -> 2
# test_02:
# grid = [
#   ["W", "W", "W", "W", "W"],
#   ["W", "W", "W", "L", "W"],
#   ["L", "W", "W", "W", "W"],
# ]
# best_bridge(grid) # -> 3
# test_03:
# grid = [
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "L", "W", "W"],
#   ["W", "W", "W", "W", "L", "L", "W", "W"],
#   ["W", "W", "W", "W", "L", "L", "L", "W"],
#   ["W", "W", "W", "W", "W", "L", "L", "L"],
#   ["L", "W", "W", "W", "W", "L", "L", "L"],
#   ["L", "L", "L", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
# ]
# best_bridge(grid) # -> 3
# test_04:
# grid = [
#   ["L", "L", "L", "L", "L", "L", "L", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "L", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "W", "W", "W", "W", "W", "W", "L"],
#   ["L", "L", "L", "L", "L", "L", "L", "L"],
# ]
# best_bridge(grid) # -> 2
# test_05:
# grid = [
#   ["W", "L", "W", "W", "W", "W", "W", "W"],
#   ["W", "L", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W", "W", "L", "W"],
#   ["W", "W", "W", "W", "W", "W", "L", "L"],
#   ["W", "W", "W", "W", "W", "W", "W", "L"],
# ]
# best_bridge(grid) # -> 8

from collections import deque

def best_bridge(grid):
  first_island = set()
  land_positions = []
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 'L':
        scope_out_land(grid, land_positions, first_island, r, c)
        break
    else:
      continue 
    break

  bridge_length = float('inf')
  for pos in land_positions:
    y, x = pos
    length = bridge(grid, first_island, y, x)
    bridge_length = length if length < bridge_length else bridge_length
  return bridge_length

def scope_out_land(grid, land_positions, first_island, r, c):
  if (r, c) in first_island or grid[r][c] == 'W':
    return
  first_island.add((r, c))
  land_positions.append([r, c])
  deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  for delta in deltas:
    [new_row, new_col], valid_pos = in_bounds(grid, delta, r, c)
    if valid_pos:
      scope_out_land(grid, land_positions, first_island, new_row, new_col)

def bridge(grid, first_island, row, col):
  deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  visited = set()
  queue = deque([[row, col, -1]])
  while queue:
    y, x, dst = queue.popleft()
    if grid[y][x] == 'L' and (y, x) not in first_island:
      return dst
    visited.add((y, x))
    for delta in deltas:
      [new_row, new_col], valid_pos = in_bounds(grid, delta, y, x)
      pos = (new_row, new_col)
      if valid_pos and pos not in visited and pos not in first_island:
        queue.append([new_row, new_col, dst + 1])
  return float('inf')

def in_bounds(grid, delta, row, col):
  delta_y, delta_x = delta
  new_row = row + delta_y
  new_col = col + delta_x
  valid_row =_row >= 0 and new_row < len(grid)
  valid_col =_col >= 0 and new_col < len(grid[0])
  return [[new_row, new_col], valid_row and valid_col]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #49 has cycle ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, has_cycle, that takes in an object representing the adjacency
# list of a directed graph. The function should return a boolean indicating 
# whether or not the graph contains a cycle.
#
# test_00:
# has_cycle({
#   a: ["b"],
#   b: ["c"],
#   c: ["a"],
# }) # -> true
# test_01:
# has_cycle({
#   a: ["b", "c"],
#   b: ["c"],
#   c: ["d"],
#   d: [],
# }) # -> false
# test_02:
# has_cycle({
#   a: ["b", "c"],
#   b: [],
#   c: [],
#   e: ["f"],
#   f: ["e"],
# }) # -> true
# test_03:
# has_cycle({
#   q: ["r", "s"],
#   r: ["t", "u"],
#   s: [],
#   t: [],
#   u: [],
#   v: ["w"],
#   w: [],
#   x: ["w"],
# }) # -> false
# test_04:
# has_cycle({
#   a: ["b"],
#   b: ["c"],
#   c: ["a"],
#   g: [],
# }) # -> true

# ========================= White-gray-black (DFS) =========================
# Time: O(e), Space: O(n)
def has_cycle(graph):
  visited = set()
  for node in graph:
    if in_cycle(graph, node, visited, set()):
      return True
  return False

def in_cycle(graph, node, visited, visiting):
  if node in visited:
    return False
  if node in visiting:
    return True

  visiting.add(node)
  for neighbor in graph[node]:
    if in_cycle(graph, neighbor, visited, visiting):
      return True
  visiting.remove(node)
  visited.add(node)
  
  return False

# [[[[[[[[[[[[[[[[[[[[[[[[[ #50 prereqs possible ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, prereqs_possible, that takes in a number of courses (n) and
# prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A
# single prerequisite of [A, B] means that course A must be taken before course
# B. The function should return a boolean indicating whether or not it is
# possible to complete all courses.
# 
# test_00:
# num_courses = 6
# prereqs = [
#   [0, 1],
#   [2, 3],
#   [0, 2],
#   [1, 3],
#   [4, 5],
# ]
# prereqs_possible(num_courses, prereqs) # -> true
# test_01:
# num_courses = 6
# prereqs = [
#   [0, 1],
#   [2, 3],
#   [0, 2],
#   [1, 3],
#   [4, 5],
#   [3, 0],
# ]
# prereqs_possible(num_courses, prereqs) # -> false
# test_02:
# num_courses = 5
# prereqs = [
#   [2, 4],
#   [1, 0],
#   [0, 2],
#   [0, 4],
# ]
# prereqs_possible(num_courses, prereqs) # -> true
# test_03:
# num_courses = 6
# prereqs = [
#   [2, 4],
#   [1, 0],
#   [0, 2],
#   [0, 4],
#   [5, 3],
#   [3, 5],
# ]
# prereqs_possible(num_courses, prereqs) # -> false
# test_04:
# num_courses = 8
# prereqs = [
#   [1, 0],
#   [0, 6],
#   [2, 0],
#   [0, 5],
#   [3, 7],
#   [4, 3],
# ]
# prereqs_possible(num_courses, prereqs) # -> true
# test_05:
# num_courses = 8
# prereqs = [
#   [1, 0],
#   [0, 6],
#   [2, 0],
#   [0, 5],
#   [3, 7],
#   [7, 4],
#   [4, 3],
# ]
# prereqs_possible(num_courses, prereqs) # -> false
# test_06:
# num_courses = 42
# prereqs = [[6, 36]]
# prereqs_possible(num_courses, prereqs) # -> true

# ========================= White-gray-black (DFS) =========================
# Time: O(e), Space: O(n)
def prereqs_possible(num_courses, prereqs):
  graph = build_graph(num_courses, prereqs)
  visited = set()
  for course in graph:
    if in_cycle(graph, course, visited, set()):
      return False 
  return True

def build_graph(num_courses, prereqs):
  graph = {}
  for num in range(num_courses):
    graph[num] = []
  for pair in prereqs:
    pre, post = pair
    graph[pre].append(post)
  return graph

def in_cycle(graph, node, visited, visiting):
  if node in visited:
    return False
  if node in visiting:
    return True

  visiting.add(node)
  for neighbor in graph[node]:
    if in_cycle(graph, neighbor, visited, visiting):
      return True
  visiting.remove(node)
  visited.add(node)

  return False

# [[[[[[[[[[[[[[[[[[[[[[[[[ #51 fib ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function fib that takes in a number argument, n, and returns the n-th
# number of the Fibonacci sequence.
# The 0-th number of the sequence is 0.
# The 1-st number of the sequence is 1.
# To generate further numbers of the sequence, calculate the sum of previous two numbers.
# Solve this recursively.
#
# test_00:
# fib(0) # -> 0
# test_01:
# fib(1) # -> 1
# test_02:
# fib(2) # -> 1
# test_03:
# fib(3) # -> 2
# test_04:
# fib(4) # -> 3
# test_05:
# fib(5) # -> 5
# test_06:
# fib(35) # -> 9227465
# test_07:
# fib(46) # -> 1836311903

# ========================= Memoization =========================
# Time: O(n), Space: O(n)
def fib(n, memo = {}):
  if n == 0 or n == 1:
    return n 
  if n in memo:
    return memo[n]
  memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
  return memo[n]

# ========================= Tabulation =========================
# Time: O(n), Space: O(1)
def fib(n):
  if n == 0 or n == 1:
    return n
  
  nums = [0, 1]
  count = 1
  while count < n:
    next = sum(nums)
    nums[0] = nums[1]
    nums[1] = next
    count += 1
  return nums[-1]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #52 tribonacci ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function tribonacci that takes in a number argument, n, and returns
# the n-th number of the Tribonacci sequence.
# The 0-th and 1-st numbers of the sequence are both 0.
# The 2-nd number of the sequence is 1.
# To generate further numbers of the sequence, calculate the sum of previous three numbers.
# Solve this recursively.
#
# test_00:
# tribonacci(0) # -> 0
# test_01:
# tribonacci(1) # -> 0
# test_02:
# tribonacci(2) # -> 1
# test_03:
# tribonacci(5) # -> 4
# test_04:
# tribonacci(7) # -> 13
# test_05:
# tribonacci(14) # -> 927
# test_06:
# tribonacci(20) # -> 35890
# test_07:
# tribonacci(37) # -> 1132436852

def tribonacci(n, memo = {}):
  if n in memo:
    return memo[n]
  if n == 0 or n == 1:
    return 0
  if n == 2:
    return 1

  memo[n] = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)
  return memo[n]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #53 sum possible ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function sum_possible that takes in an amount and an list of positive
# numbers. The function should return a boolean indicating whether or not it is
# possible to create the amount by summing numbers of the list. You may reuse
# numbers of the list as many times as necessary.
# You may assume that the target amount is non-negative.
#
# test_00:
# sum_possible(8, [5, 12, 4]) # -> true, 4 + 4
# test_01:
# sum_possible(15, [6, 2, 10, 19]) # -> false
# test_02:
# sum_possible(13, [6, 2, 1]) # -> true
# test_03:
# sum_possible(103, [6, 20, 1]) # -> true
# test_04:
# sum_possible(12, []) # -> false
# test_05:
# sum_possible(12, [12]) # -> true
# test_06:
# sum_possible(0, []) # -> true
# test_07:
# sum_possible(271, [10, 8, 265, 24]) # -> false
# test_08:
# sum_possible(2017, [4, 2, 10]) # -> false

# ========================= Memoization =========================
# Time: O(a*n), Space: O(a)
def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]
  if amount == 0:
    return True

  memo[amount] = False
  for num in numbers:
    if num <= amount and _sum_possible(amount - num, numbers, memo):
      memo[amount] = True 
      return True
  return memo[amount]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #54 min change ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function min_change that takes in an amount and an list of coins. The
# function should return the minimum number of coins required to create the
# amount. You may use each coin as many times as necessary.
# If it is not possible to create the amount, then return -1.
#
# test_00:
# min_change(8, [1, 5, 4, 12]) # -> 2, because 4+4 is the minimum coins possible
# test_01:
# min_change(13, [1, 9, 5, 14, 30]) # -> 5
# test_02:
# min_change(23, [2, 5, 7]) # -> 4
# test_03:
# min_change(102, [1, 5, 10, 25]) # -> 6
# test_04:
# min_change(200, [1, 5, 10, 25]) # -> 8
# test_05:
# min_change(2017, [4, 2, 10]) # -1
# test_06:
# min_change(271, [10, 8, 265, 24]) # -1
# test_07:
# min_change(0, [4, 2, 10]) # 0
# test_08:
# min_change(0, []) # 0

# ========================= Memoization =========================
# Time: O(a*c), Space: O(a)
def min_change(num, coins):
  min = _min_change(num, coins, {})
  return -1 if min == float('inf') else min

def _min_change(num, coins, memo):
  if num in memo:
    return memo[num]
  if num == 0:
    return 0

  min = float('inf')
  for c in coins:
    if c <= num:
      count = 1 + _min_change(num - c, coins, memo)
      if count < min:
        min = count

  memo[num] = min
  return memo[num]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #55 count paths ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, count_paths, that takes in a grid as an argument. In the grid,
# 'X' represents walls and 'O' represents open spaces. You may only move down or
# to the right and cannot pass through walls. The function should return the
# number of ways possible to travel from the top-left corner of the grid to the
# bottom-right corner.
#
# test_00:
# grid = [
#   ["O", "O"],
#   ["O", "O"],
# ]
# count_paths(grid) # -> 2
# test_01:
# grid = [
#   ["O", "O", "X"],
#   ["O", "O", "O"],
#   ["O", "O", "O"],
# ]
# count_paths(grid) # -> 5
# test_02:
# grid = [
#   ["O", "O", "O"],
#   ["O", "O", "X"],
#   ["O", "O", "O"],
# ]
# count_paths(grid) # -> 3
# test_03:
# grid = [
#   ["O", "O", "O"],
#   ["O", "X", "X"],
#   ["O", "O", "O"],
# ]
# count_paths(grid) # -> 1
# test_04:
# grid = [
#   ["O", "O", "X", "O", "O", "O"],
#   ["O", "O", "X", "O", "O", "O"],
#   ["X", "O", "X", "O", "O", "O"],
#   ["X", "X", "X", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O"],
# ]
# count_paths(grid) # -> 0
# test_05:
# grid = [
#   ["O", "O", "X", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "X"],
#   ["X", "O", "O", "O", "O", "O"],
#   ["X", "X", "X", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O"],
# ]
# count_paths(grid) # -> 42
# test_06:
# grid = [
#   ["O", "O", "X", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "X"],
#   ["X", "O", "O", "O", "O", "O"],
#   ["X", "X", "X", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "X"],
# ]
# count_paths(grid) # -> 0
# test_07:
# grid = [
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
# ]
# count_paths(grid) # -> 40116600
# test_08:
# grid = [
#   ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
#   ["X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
#   ["X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
#   ["X", "X", "X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
# ]
# count_paths(grid) # -> 3190434

# ========================= Memoization =========================
# Time: O(r*c), Space: O(r*c)
def count_paths(grid):
  return _count_paths(grid, 0, 0, {})

def _count_paths(grid, r, c, memo):
  if (r, c) in memo:
    return memo[(r, c)]
  if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
    return 0
  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return 1
  
  count = 0
  count += _count_paths(grid, r + 1, c, memo)
  count += _count_paths(grid, r, c + 1, memo)

  memo[(r, c)] = count
  return memo[(r, c)] 

# [[[[[[[[[[[[[[[[[[[[[[[[[ #56 max path sum ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, max_path_sum, that takes in a grid as an argument. The
# function should return the maximum sum possible by traveling a path from the
# top-left corner to the bottom-right corner. You may only travel through the
# grid by moving down or right.
#
# test_00:
# grid = [
#   [1, 3, 12],
#   [5, 1, 1],
#   [3, 6, 1],
# ]
# max_path_sum(grid) # -> 18
# test_01:
# grid = [
#   [1, 2, 8, 1],
#   [3, 1, 12, 10],
#   [4, 0, 6, 3],
# ]
# max_path_sum(grid) # -> 36
# test_02:
# grid = [
#   [1, 2, 8, 1],
#   [3, 10, 12, 10],
#   [4, 0, 6, 3],
# ]
# max_path_sum(grid) # -> 39
# test_03:
# grid = [
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]
# max_path_sum(grid) # -> 27
# test_04:
# grid = [
#   [1, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 2, 1, 1, 6, 1, 1, 5, 1, 1, 0, 0, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 5, 1, 1, 1, 1, 0, 1, 1, 1, 1],
#   [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [2, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1],
#   [2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]
# max_path_sum(grid) # -> 56

# ========================= Memoization =========================
# Time: O(r*c), Space: O(r*c)
def max_path_sum(grid):
  return _max_path_sum(grid, 0, 0, {})
  
def _max_path_sum(grid, r, c, memo):
  if (r, c) in memo:
    return memo[(r, c)]
  if r == len(grid) or c == len(grid[0]):
    return 0

  sum = grid[r][c]
  sum += max(
    _max_path_sum(grid, r + 1, c, memo),
    _max_path_sum(grid, r, c + 1, memo)
  )

  memo[(r, c)] = sum
  return sum

# [[[[[[[[[[[[[[[[[[[[[[[[[ #57 non adjacent sum ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, non_adjacent_sum, that takes in an list of numbers as an
# argument. The function should return the maximum sum of non-adjacent elements
# in the list. There is no limit on how many elements can be taken into the sum
# as long as they are not adjacent.
# For example, given:
# [2, 4, 5, 12, 7]
# The maximum non-adjacent sum is 16, because 4 + 12. 
# 4 and 12 are not adjacent in the list.
#
# test_00:
# nums = [2, 4, 5, 12, 7]
# non_adjacent_sum(nums) # -> 16
# test_01:
# nums = [7, 5, 5, 12]
# non_adjacent_sum(nums) # -> 19
# test_02:
# nums = [7, 5, 5, 12, 17, 29]
# non_adjacent_sum(nums) # -> 48
# test_03:
# nums = [
#   72, 62, 10,  6, 20, 19, 42,
#   46, 24, 78, 30, 41, 75, 38,
#   23, 28, 66, 55, 12, 17, 9,
#   12, 3, 1, 19, 30, 50, 20
# ]
# non_adjacent_sum(nums) # -> 488
# test_04:
# nums = [
#   72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
#   30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
#   83, 80, 56, 68,  6, 22, 56, 96, 77, 98,
#   61, 20,  0, 76, 53, 74,  8, 22, 92, 37,
#   30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
#   72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
#   42
# ]
# non_adjacent_sum(nums) # -> 1465

# ========================= Memoization =========================
# Time: O(n), Space: O(n)
def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, 0, {})

def _non_adjacent_sum(nums, i, memo):
  if i in memo:
    return memo[i]
  if i >= len(nums):
    return 0

  sum = max(
    nums[i] + _non_adjacent_sum(nums, i + 2, memo),
    _non_adjacent_sum(nums, i + 1, memo)
  )
  memo[i] = sum
  return sum

# [[[[[[[[[[[[[[[[[[[[[[[[[ #58 summing squares ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, summing_squares, that takes a target number as an argument.
# The function should return the minimum number of perfect squares that sum to
# the target. A perfect square is a number of the form (i*i) where i >= 1.
# For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.
# Given 12:
# summing_squares(12) -> 3
# The minimum squares required for 12 is three, by doing 4 + 4 + 4.
# Another way to make 12 is 9 + 1 + 1 + 1, but that requires four perfect squares.
#
# test_00:
# summing_squares(8) # -> 2
# test_01:
# summing_squares(9) # -> 1
# test_02:
# summing_squares(12) # -> 3
# test_03:
# summing_squares(1) # -> 1
# test_04:
# summing_squares(31) # -> 4
# test_05:
# summing_squares(50) # -> 2
# test_06:
# summing_squares(68) # -> 2
# test_07:
# summing_squares(87) # -> 4

# ========================= Memoization =========================
# Time: O(n*sqrt(n)), Space: O(n)
import math

def summing_squares(num, memo = {}):
  if num in memo:
    return memo[num]
  if num == 0:
    return 0

  min = float('inf')
  for x in range(math.floor(math.sqrt(num)), 0 ,-1):
    square = x**2
    count = 1 + summing_squares(num - square, memo)
    min = count if count < min else min 
  memo[num] = min
  return min

# [[[[[[[[[[[[[[[[[[[[[[[[[ #59 counting change ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, counting_change, that takes in an amount and an list of
# coins. The function should return the number of different ways it is possible
# to make change for the given amount using the coins.
# You may reuse a coin as many times as necessary.
# For example,
# counting_change(4, [1,2,3]) -> 4
# There are four different ways to make an amount of 4:
# 1. 1 + 1 + 1 + 1
# 2. 1 + 1 + 2
# 3. 1 + 3
# 4. 2 + 2
#
# test_00:
# counting_change(4, [1, 2, 3]) # -> 4
# test_01:
# counting_change(8, [1, 2, 3]) # -> 10
# test_02:
# counting_change(24, [5, 7, 3]) # -> 5
# test_03:
# counting_change(13, [2, 6, 12, 10]) # -> 0
# test_04:
# counting_change(512, [1, 5, 10, 25]) # -> 20119
# test_05:
# counting_change(1000, [1, 5, 10, 25]) # -> 142511
# test_06:
# counting_change(240, [1, 2, 3, 4, 5, 6, 7, 8, 9]) # -> 1525987916

# ========================= Memoization =========================
# Time: O(a*c), Space: O(a*c)
def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
  if (amount, i) in memo:
    return memo[(amount, i)]
  if amount == 0:
    return 1
  if i == len(coins):
    return 0
  
  coin = coins[i]
  count = 0
  for qty in range(1, (amount // coin) + 1):
    remainder = amount - qty * coin
    count += _counting_change(remainder, coins, i + 1, memo)
  memo[(amount, i)] = count
  return count

# [[[[[[[[[[[[[[[[[[[[[[[[[ #60 array stepper ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, array_stepper, that takes in an list of numbers as an
# argument. You start at the first position of the list. The function should
# return a boolean indicating whether or not it is possible reach the last
# position of the list. When situated at some position of the list, you may
# take a maximum number of steps based on the number at that position.
# For example, given:
#     idx =  0  1  2  3  4  5
# numbers = [2, 4, 2, 0, 0, 1]
# The answer is true.
# We start at idx 0, we could take 1 step or 2 steps forward.
# The correct choice is to take 1 step to idx 1.
# Then take 4 steps forward to the end at idx 5.
#
# test_00:
# array_stepper([2, 4, 2, 0, 0, 1]) # -> true
# test_01:
# array_stepper([2, 3, 2, 0, 0, 1]) # -> false
# test_02:
# array_stepper([3, 1, 3, 1, 0, 1]) # -> true
# test_03:
# array_stepper([4, 1, 5, 1, 1, 1, 0, 4]) # -> true
# test_04:
# array_stepper([4, 1, 2, 1, 1, 1, 0, 4]) # -> false
# test_05:
# array_stepper([1, 1, 1, 1, 1, 0]) # -> true
# test_06:
# array_stepper([1, 1, 1, 1, 0, 0]) # -> false
# test_07:
# array_stepper([ 
#   31, 30, 29, 28, 27,
#   26, 25, 24, 23, 22,
#   21, 20, 19, 18, 17,
#   16, 15, 14, 13, 12,
#   11, 10, 9, 8, 7, 6,
#   5, 3, 2, 1, 0, 0, 0
# ]) # -> false

# ========================= Memoization =========================
# Time: O(n^2), Space: O(n)
def array_stepper(numbers):
  return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, i, memo):
  if i in memo:
    return memo[i]
  if i >= len(numbers) - 1:
    return True
  if numbers[i] == 0:
    return False
  
  for x in range(1, numbers[i] + 1):
    if _array_stepper(numbers, i + x, memo):
      memo[i] = True
      return True
  memo[i] = False
  return False


# [[[[[[[[[[[[[[[[[[[[[[[[[ #61 max palin subsequence ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, max_palin_subsequence, that takes in a string as an argument.
# The function should return the length of the longest subsequence of the string
# that is also a palindrome.
# A subsequence of a string can be created by deleting any characters of the
# string, while maintaining the relative order of characters.
#
# test_00:
# max_palin_subsequence("luwxult") # -> 5
# test_01:
# max_palin_subsequence("xyzaxxzy") # -> 6
# test_02:
# max_palin_subsequence("lol") # -> 3
# test_03:
# max_palin_subsequence("boabcdefop") # -> 3
# test_04:
# max_palin_subsequence("z") # -> 1
# test_05:
# max_palin_subsequence("chartreusepugvicefree") # -> 7
# test_06:
# max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty") # -> 15
# test_07:
# max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe") # -> 31

# ========================= Memoization =========================
# Time: O(n^2), Space: O(n^2)
def max_palin_subsequence(string):
  return _helper(string, 0, len(string), {})

def _helper(string, i, j, memo):
  key = (i, j)

  if key in memo:
    return memo[key]
  if i == j:
    return 1
  if i > j:
    return 0
  
  if string[i] == string[j]:
    memo[key] = 2 + _helper(string, i + 1, j - 1, memo)
  else:
    memo[key] = max(
      _helper(string, i + 1, j, memo),
      _helper(string, i, j - 1, memo)
    )
  
  return memo[key]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #62 overlap subsequence ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, overlap_subsequence, that takes in two strings as arguments.
# The function should return the length of the longest overlapping subsequence.
# A subsequence of a string can be created by deleting any characters of the
# string, while maintaining the relative order of characters.
#
# test_00:
# overlap_subsequence("dogs", "daogt") # -> 3
# test_01:
# overlap_subsequence("xcyats", "criaotsi") # -> 4
# test_02:
# overlap_subsequence("xfeqortsver", "feeeuavoeqr") # -> 5
# test_03:
# overlap_subsequence("kinfolklivemustache", "bespokekinfolksnackwave") # -> 11
# test_04:
# overlap_subsequence(
#   "mumblecorebeardleggingsauthenticunicorn",
#   "succulentspughumblemeditationlocavore"
# ) # -> 15

# ========================= Memoization =========================
# Time: O(nm), Space: O(nm)
def overlap_subsequence(string_1, string_2):
  return _helper(string_1, string_2, 0, 0, {})

def _helper(string_1, string_2, i, j, memo):
  key = (i, j)
  if key in memo:
    return memo[key]
  if i == len(string_1) or j == len(string_2):
    return 0
  
  if string_1[i] == string_2[j]:
    memo[key] = 1 + _helper(string_1, string_2, i + 1, j + 1, memo)
  else:
    memo[key] = max(
      _helper(string_1, string_2, i + 1, j, memo),
      _helper(string_1, string_2, i, j + 1, memo)
    )
  return memo[key]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #63 can concat ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, can_concat, that takes in a string and an list of words as
# arguments. The function should return boolean indicating whether or not it is
# possible to concatenate words of the list together to form the string.
# You may reuse words of the list as many times as needed.
#
# test_00:
# can_concat("oneisnone", ["one", "none", "is"]) # -> true
# test_01:
# can_concat("oneisnone", ["on", "e", "is"]) # -> false
# test_02:
# can_concat("oneisnone", ["on", "e", "is", "n"]) # -> true
# test_03:
# can_concat("foodisgood", ["is", "g", "ood", "f"]) # -> true
# test_04:
# can_concat("santahat", ["santah", "hat"]) # -> false
# test_05:
# can_concat("santahat", ["santah", "san", "hat", "tahat"]) # -> true
# test_06:
# can_concat("rrrrrrrrrrrrrrrrrrrrrrrrrrx", ["r", "rr", "rrr", "rrrr", "rrrrr", "rrrrrr"]) # -> false

# ========================= Memoization =========================
# Time: ~O(sw), Space: O(s)
def can_concat(s, words):
  return _helper(s, words, {})

def _helper(s, words, memo):
  if s in memo:
    return memo[s]
  if len(s) == 0:
    return True
  
  for word in words:
    if s.startswith(word) and _helper(s[len(word):], words):
      memo[s] = True
      return True
  memo[s] = False
  return False


# [[[[[[[[[[[[[[[[[[[[[[[[[ #64 quickest concat ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, quickest_concat, that takes in a string and an list of words
# as arguments. The function should return the minimum number of words needed to
# build the string by concatenating the words.
# You may use words of the list as many times as needed.
#
# test_00:
# quickest_concat('caution', ['ca', 'ion', 'caut', 'ut']) # -> 2
# test_01:
# quickest_concat('caution', ['ion', 'caut', 'caution']) # -> 1
# test_02:
# quickest_concat('respondorreact', ['re', 'or', 'spond', 'act', 'respond']) # -> 4
# test_03:
# quickest_concat('simchacindy', ['sim', 'simcha', 'acindy', 'ch']) # -> 3
# test_04:
# quickest_concat('simchacindy', ['sim', 'simcha', 'acindy']) # -> -1
# test_05:
# quickest_concat('uuuuuu', ['u', 'uu', 'uuu', 'uuuu']) # -> 2
# test_06:
# quickest_concat('rongbetty', ['wrong', 'bet']) # -> -1
# test_07:
# quickest_concat('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', ['u', 'uu', 'uuu', 'uuuu', 'uuuuu']) # -> 7

# ========================= Memoization =========================
# Time: ~O(sw), Space: O(s)
def quickest_concat(s, words):
  num = _quickest_concat(s, words, {})
  return num if num != float('inf') else -1

def _quickest_concat(s, words, memo):
  if s in memo: 
    return memo[s]
  if len(s) == 0:
    return 0
  
  min_words = float('inf')
  for w in words:
    if s.startswith(w):
      count = 1 + _quickest_concat(s[len(w):], words, memo)
      min_words = min(min_words, count)
  memo[s] = min_words
  return memo[s]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #65 paired parentheses ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, paired_parentheses, that takes in a string as an argument.
# The function should return a boolean indicating whether or not the string has
# well-formed parentheses.
# You may assume the string contains only alphabetic characters, '(', or ')'.
#
# test_00:
# paired_parentheses("(david)((abby))") # -> true
# test_01:
# paired_parentheses("()rose(jeff") # -> false
# test_02:
# paired_parentheses(")(") # -> false
# test_03:
# paired_parentheses("()") # -> true
# test_04:
# paired_parentheses("(((potato())))") # -> true
# test_05:
# paired_parentheses("(())(water)()") # -> true
# test_06:
# paired_parentheses("(())(water()()") # -> false
# test_07:
# paired_parentheses("") # -> true

def paired_parentheses(s):
  count = 0
  for char in s:
    if char == '(':
      count += 1
    elif char == ')':
      if count > 0:
        count -= 1
      else:
        return False
  return count == 0

# [[[[[[[[[[[[[[[[[[[[[[[[[ #66 befitting brackets ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, befitting_brackets, that takes in a string as an argument.
# The function should return a boolean indicating whether or not the string
# contains correctly matched brackets.
# You may assume the string contains only characters: ( ) [ ] { }
#
# test_00:
# befitting_brackets('(){}[](())') # -> true
# test_01:
# befitting_brackets('({[]})') # -> true
# test_02:
# befitting_brackets('[][}') # -> false
# test_03:
# befitting_brackets('{[]}({}') # -> false
# test_04:
# befitting_brackets('[]{}(}[]') # -> false
# test_05:
# befitting_brackets('[]{}()[]') # -> true
# test_06:
# befitting_brackets(']{}') # -> false
# test_07:
# befitting_brackets('') # -> true

def befitting_brackets(s):
  match = {
    ')': '(',
    ']': '[',
    '}': '{'
  }
  open = set(['(', '[', '{'])
  stack = []
  for char in s:
    if char in open:
      stack.append(char)
    elif char in match:
      if len(stack) > 0 and stack[-1] == match[char]:
        stack.pop()
      else:
        return False
  return len(stack) == 0

# [[[[[[[[[[[[[[[[[[[[[[[[[ #67 decompress braces ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, decompress_braces, that takes in a compressed string as an
# argument. The function should return the string decompressed.
# The compression format of the input string is 'n{subString}', where the
# subString within braces should be repeated n times.
# You may assume that every number n is guaranteed to be an integer between 1
# through 9.
# You may assume that the input is valid and the decompressed string will only
# contain alphabetic characters.
#
# test_00:
# decompress_braces("2{q}3{tu}v") 
# -> qqtututuv 
# test_01:
# decompress_braces("ch3{ao}") 
# -> chaoaoao
# test_02:
# decompress_braces("2{y3{o}}s") 
# -> yoooyooos
# test_03:
# decompress_braces("z3{a2{xy}b}") 
# -> zaxyxybaxyxybaxyxyb 
# test_04:
# decompress_braces("2{3{r4{e}r}io}") 
# -> reeeerreeeerreeeerioreeeerreeeerreeeerio 
# test_05:
# decompress_braces("go3{spinn2{ing}s}") 
# -> gospinningingsspinningingsspinningings 
# test_06:
# decompress_braces("2{l2{if}azu}l") 
# -> lififazulififazul 
# test_07:
# decompress_braces("3{al4{ec}2{icia}}") 
# -> alececececiciaiciaalececececiciaiciaalececececiciaicia 

# ========================= Using a stack =========================
# m: number of brace pairs, s: length of string
# Time: O(9^m * s), Space: O(9^m * s)
def decompress_braces(string):
  nums = '123456789'
  stack = []
  for char in string:
    if char in nums:
      stack.append(int(char))
    else:
      if char == '}':
        substr = ''
        while isinstance(stack[-1], str):
          substr = stack.pop() + substr
        num = stack.pop()
        stack.append(substr * num)
      elif char != '{':
        stack.append(char)
  return ''.join(stack)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #68 nesting score ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, nesting_score, that takes in a string of brackets as an
# argument. The function should return the score of the string according to the
# following rules:
# [] is worth 1 point
# XY is worth m + n points where X, Y are substrings of well-formed brackets and m, n are their respective scores
# [S] is worth 2 * k points where S is a substring of well-formed brackets and k is the score of that substring
# You may assume that the input only contains well-formed square brackets.
#
# test_00:
# nesting_score("[]") # -> 1
# test_01:
# nesting_score("[][][]") # -> 3
# test_02:
# nesting_score("[[]]") # -> 2
# test_03:
# nesting_score("[[][]]") # -> 4
# test_04:
# nesting_score("[[][][]]") # -> 6
# test_05:
# nesting_score("[[][]][]") # -> 5
# test_06:
# nesting_score("[][[][]][[]]") # -> 7
# test_07:
# nesting_score("[[[[[[[][]]]]]]][]") # -> 129

# ========================= Using a stack =========================
# Time: O(s), Space: O(s)
def nesting_score(string):
  stack = [0]
  for char in string:
    if char == ']':
      popped = stack.pop()
      if popped == 0:
        stack[-1] += 1
      else: 
        stack[-1] = popped * 2
    else:
      stack.append(0)
  return stack[0]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #69 subsets ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, subsets, that takes in an list an argument. The function
# should return a 2D list where each sublist represents one of the possible
# subsets of the list.
# The elements within the subsets and the subsets themselves may be returned in any order.
# You may assume that the input list contains unique elements.
#
# test_00:
# subsets(['a', 'b']) # ->
# [ 
#   [], 
#   [ 'b' ], 
#   [ 'a' ], 
#   [ 'a', 'b' ] 
# ]
# test_01:
# subsets(['a', 'b', 'c']) # ->
# [
#   [],
#   [ 'c' ],
#   [ 'b' ],
#   [ 'b', 'c' ],
#   [ 'a' ],
#   [ 'a', 'c' ],
#   [ 'a', 'b' ],
#   [ 'a', 'b', 'c' ]
# ]
# test_02:
# subsets(['x']) # ->
# [ 
#   [], 
#   [ 'x' ] 
# ]
# test_03:
# subsets([]) # ->
# [ 
#   []
# ]
# test_04:
# subsets(['q', 'r', 's', 't']) # ->
# [
#   [],
#   [ 't' ],
#   [ 's' ],
#   [ 's', 't' ],
#   [ 'r' ],
#   [ 'r', 't' ],
#   [ 'r', 's' ],
#   [ 'r', 's', 't' ],
#   [ 'q' ],
#   [ 'q', 't' ],
#   [ 'q', 's' ],
#   [ 'q', 's', 't' ],
#   [ 'q', 'r' ],
#   [ 'q', 'r', 't' ],
#   [ 'q', 'r', 's' ],
#   [ 'q', 'r', 's', 't' ]
# ]

# ========================= Recursive =========================
# Time: O(2^n), Space: O(2^n)
def subsets(elements):
  if len(elements) == 0:
    return [[]]

  first = elements[0]
  subs_without_first = subsets(elements[1:])
  subs_with_first = []
  for sub in subs_without_first:
    subs_with_first.append([first, *sub])
  
  return subs_with_first + subs_without_first

# [[[[[[[[[[[[[[[[[[[[[[[[[ #70 permutations ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, permutations, that takes in an list an argument. The
# function should return a 2D list where each sublist represents one of the
# possible permutations of the list.
# The sublists may be returned in any order.
# You may assume that the input list contains unique elements.
#
# test_00:
# permutations(['a', 'b', 'c']) # -> 
# [ 
#   [ 'a', 'b', 'c' ], 
#   [ 'b', 'a', 'c' ], 
#   [ 'b', 'c', 'a' ], 
#   [ 'a', 'c', 'b' ], 
#   [ 'c', 'a', 'b' ], 
#   [ 'c', 'b', 'a' ] 
# ] 
# test_01:
# permutations(['red', 'blue']) # ->
# [ 
#   [ 'red', 'blue' ], 
#   [ 'blue', 'red' ] 
# ]
# test_02:
# permutations([8, 2, 1, 4]) # ->
# [ 
#   [ 8, 2, 1, 4 ], [ 2, 8, 1, 4 ], 
#   [ 2, 1, 8, 4 ], [ 2, 1, 4, 8 ], 
#   [ 8, 1, 2, 4 ], [ 1, 8, 2, 4 ], 
#   [ 1, 2, 8, 4 ], [ 1, 2, 4, 8 ], 
#   [ 8, 1, 4, 2 ], [ 1, 8, 4, 2 ], 
#   [ 1, 4, 8, 2 ], [ 1, 4, 2, 8 ], 
#   [ 8, 2, 4, 1 ], [ 2, 8, 4, 1 ], 
#   [ 2, 4, 8, 1 ], [ 2, 4, 1, 8 ], 
#   [ 8, 4, 2, 1 ], [ 4, 8, 2, 1 ], 
#   [ 4, 2, 8, 1 ], [ 4, 2, 1, 8 ], 
#   [ 8, 4, 1, 2 ], [ 4, 8, 1, 2 ], 
#   [ 4, 1, 8, 2 ], [ 4, 1, 2, 8 ] 
# ] 
# test_03:
# permutations([]) # ->
# [
#  [ ]
# ]

# ========================= Recursive =========================
# Time: O(n!), Space: O(n!)
def permutations(items):
  if len(items) == 0:
    return [[]]

  first = items[0]
  full_perm = []
  old_perm = permutations(items[1:])
  for perm in old_perm:
    for i in range(len(perm) + 1):
      full_perm.append(perm[:i] + [first] + perm[i:])
  return full_perm

# [[[[[[[[[[[[[[[[[[[[[[[[[ #71 create combinations ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, create_combinations, that takes in an list and a length as
# arguments. The function should return a 2D list representing all of the
# combinations of the specifized length.
# The items within the combinations and the combinations themselves may be
# returned in any order.
# You may assume that the input list contains unique elements and 
# 1 <= k <= len(items).
#
# test_00:
# create_combinations(["a", "b", "c"], 2) # ->
# [
#   [ 'a', 'b' ],
#   [ 'a', 'c' ],
#   [ 'b', 'c' ]
# ]
# test_01:
# create_combinations(["q", "r", "s", "t"], 2) # ->
# [
#   [ 'q', 'r' ],
#   [ 'q', 's' ],
#   [ 'q', 't' ],
#   [ 'r', 's' ],
#   [ 'r', 't' ],
#   [ 's', 't' ]
# ]
# test_02:
# create_combinations(['q', 'r', 's', 't'], 3)) # ->
# [
#   [ 'q', 'r', 's' ],
#   [ 'q', 'r', 't' ],
#   [ 'q', 's', 't' ],
#   [ 'r', 's', 't' ]
# ]
# test_03:
# create_combinations([1, 28, 94], 3) # ->
# [
#   [ 1, 28, 94 ]
# ]

# ========================= Recursive =========================
# Time: O(n! / k!(n-k)!), Space: O(n! / k!(n-k)!)
# "n choose k" = binomial coefficient
def create_combinations(items, k):
  if k == 0:
    return [[]]
  if k > len(items):
    return []
  if len(items) == k:
    return [items]
  
  first = items[0]
  smaller_combo = create_combinations(items[1:], k - 1)
  combo_without_first = create_combinations(items[1:], k)
  combos = []
  for combo in smaller_combo:
    combos.append(combo + [first])
  return combos + combo_without_first

# [[[[[[[[[[[[[[[[[[[[[[[[[ #72 parenthetical possibilities ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, parenthetical_possibilities, that takes in a string as an
# argument. The function should return an list containing all of the strings
# that could be generated by expanding all parentheses of the string into its
# possibilities.
# For example, the possibilities for 'x(mn)yz' are 'xmyz', 'xnyz'.
#
# test_00:
# parenthetical_possibilities('x(mn)yz') # -> 
# [ 'xmyz', 'xnyz' ]
# test_01:
# parenthetical_possibilities("(qr)ab(stu)c") # ->
# [ 'qabsc', 'qabtc', 'qabuc', 'rabsc', 'rabtc', 'rabuc' ]
# test_02:
# parenthetical_possibilities("taco") # ->
# ['taco']
# test_03:
# parenthetical_possibilities("") # ->
# ['']
# test_04:
# parenthetical_possibilities("(etc)(blvd)(cat)") # ->
# [
#  'ebc', 'eba', 'ebt', 'elc', 'ela',
#  'elt', 'evc', 'eva', 'evt', 'edc',
#  'eda', 'edt', 'tbc', 'tba', 'tbt',
#  'tlc', 'tla', 'tlt', 'tvc', 'tva',
#  'tvt', 'tdc', 'tda', 'tdt', 'cbc',
#  'cba', 'cbt', 'clc', 'cla', 'clt',
#  'cvc', 'cva', 'cvt', 'cdc', 'cda',
#  'cdt'
# ]

# ========================= Recursive =========================
# n: length of longest substring, m: number of parenthetical pairs
# Time: O(n^m), Space: O(n^m)
def parenthetical_possibilities(s):
  if len(s) == 0:
    return ['']
  
  remaining, chars = get_options(s)
  options = parenthetical_possibilities(remaining)
  possibilities = []
  for char in chars:
    possibilities += [char + suffix for suffix in options]
  return possibilities

def get_options(s):
  if s[0] == '(':
    idx = s.index(')')
    chars = s[1:idx]
    remaining = s[idx + 1:]
    return (remaining, chars)
  else:
    return (s[1:], s[0])

# [[[[[[[[[[[[[[[[[[[[[[[[[ #73 substitute synonyms ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, substitute_synonyms, that takes in a sentence and an object
# as arguments. The object contains words as keys whose values are lists
# containing synonyms. The function should return an list containing all
# possible sentences that can be formed by substituting words of the sentence
# with their synonyms.
# You may return the possible sentences in any order, as long as you return
# all of them.
#
# test_00:
# sentence = "follow the yellow brick road"
# synonyms = {
#   follow: ["chase", "pursue"],
#   yellow: ["gold", "amber", "lemon"],
# }
# substitute_synonyms(sentence, synonyms)
# [
#   'chase the gold brick road',
#   'chase the amber brick road',
#   'chase the lemon brick road',
#   'pursue the gold brick road',
#   'pursue the amber brick road',
#   'pursue the lemon brick road'
# ]
# test_01:
# sentence = "I think it's gonna be a long long time"
# synonyms = {
#   think: ["believe", "reckon"],
#   long: ["lengthy", "prolonged"],
# }
# substitute_synonyms(sentence, synonyms)
# [
#   "I believe it's gonna be a lengthy lengthy time",
#   "I believe it's gonna be a lengthy prolonged time",
#   "I believe it's gonna be a prolonged lengthy time",
#   "I believe it's gonna be a prolonged prolonged time",
#   "I reckon it's gonna be a lengthy lengthy time",
#   "I reckon it's gonna be a lengthy prolonged time",
#   "I reckon it's gonna be a prolonged lengthy time",
#   "I reckon it's gonna be a prolonged prolonged time"
# ]
# test_02:
# sentence = "palms sweaty knees weak arms heavy"
# synonyms = {
#   palms: ["hands", "fists"],
#   heavy: ["weighty", "hefty", "burdensome"],
#   weak: ["fragile", "feeble", "frail", "sickly"],
# }
# substitute_synonyms(sentence, synonyms)
# [
#   'hands sweaty knees fragile arms weighty',
#   'hands sweaty knees fragile arms hefty',
#   'hands sweaty knees fragile arms burdensome',
#   'hands sweaty knees feeble arms weighty',
#   'hands sweaty knees feeble arms hefty',
#   'hands sweaty knees feeble arms burdensome',
#   'hands sweaty knees frail arms weighty',
#   'hands sweaty knees frail arms hefty',
#   'hands sweaty knees frail arms burdensome',
#   'hands sweaty knees sickly arms weighty',
#   'hands sweaty knees sickly arms hefty',
#   'hands sweaty knees sickly arms burdensome',
#   'fists sweaty knees fragile arms weighty',
#   'fists sweaty knees fragile arms hefty',
#   'fists sweaty knees fragile arms burdensome',
#   'fists sweaty knees feeble arms weighty',
#   'fists sweaty knees feeble arms hefty',
#   'fists sweaty knees feeble arms burdensome',
#   'fists sweaty knees frail arms weighty',
#   'fists sweaty knees frail arms hefty',
#   'fists sweaty knees frail arms burdensome',
#   'fists sweaty knees sickly arms weighty',
#   'fists sweaty knees sickly arms hefty',
#   'fists sweaty knees sickly arms burdensome'
# ]

# ========================= Recursive =========================
# n: num words in string, m: max num of synonyms for a word
# Time: O(m^n), Space: O(m^n)
def substitute_synonyms(sentence, synonyms):
  substitutions = _substitute_synonyms(sentence.split(' '), synonyms)
  return substitutions

def _substitute_synonyms(words, synonyms):
  if len(words) == 0:
    return ['']

  replacements = [words[0]]
  if words[0] in synonyms:
    replacements = synonyms[words[0]]
  
  substitutions = _substitute_synonyms(words[1:], synonyms)
  result = []
  for word in replacements:
    for sub in substitutions:
      if sub != '':
        result.append(word + ' ' + sub)
      else:
        result.append(word)

  return result

# ========================= Alvin's Solution =========================
def substitute_synonyms(sentence, synonyms):
  words = sentence.split(' ')
  subarrays = generate(words, synonyms)
  return [ ' '.join(subarray) for subarray in subarrays ]

def generate(words, synonyms):
  if len(words) == 0:
    return [[]]
  
  first_word = words[0]
  remaining_words = words[1:]
  
  subarrays = generate(remaining_words, synonyms)
  
  if first_word in synonyms:
    result = []
    for synonym in synonyms[first_word]:
      result += [ [synonym, *subarray] for subarray in subarrays ]
    return result
  else:
    return [ [first_word, *subarray] for subarray in subarrays ] 

# [[[[[[[[[[[[[[[[[[[[[[[[[ #74 linked palindrome ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, linked_palindrome, that takes in the head of a linked list
# as an argument. The function should return a boolean indicating whether or
# not the linked list is a palindrome. A palindrome is a sequence that is the
# same both forwards and backwards.
#
# test_00:
# a = Node(3)
# b = Node(2)
# c = Node(7)
# d = Node(7)
# e = Node(2)
# f = Node(3)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# 3 -> 2 -> 7 -> 7 -> 2 -> 3
# linked_palindrome(a) # true
# test_01:
# a = Node(3)
# b = Node(2)
# c = Node(4)
# a.next = b
# b.next = c
# 3 -> 2 -> 4
# linked_palindrome(a) # false
# test_02:
# a = Node(3)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c
# 3 -> 2 -> 3
# linked_palindrome(a) # true
# test_03:
# a = Node(0)
# b = Node(1)
# c = Node(0)
# d = Node(1)
# e = Node(0)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# 0 -> 1 -> 0 -> 1 -> 0
# linked_palindrome(a) # true
# test_04:
# a = Node(0)
# b = Node(1)
# c = Node(0)
# d = Node(1)
# e = Node(1)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# 0 -> 1 -> 0 -> 1 -> 1
# linked_palindrome(a) # false
# test_05:
# a = Node(5)
# 5
# linked_palindrome(a) # true
# test_06:
# linked_palindrome(None) # true

# Time: O(n), Space: O(n)
def linked_palindrome(head):
  values = []
  current = head 
  while current is not None:
    values.append(current.val)
    current = current.next
  return values == values[::-1]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #75 middle value ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, middle_value, that takes in the head of a linked list as an
# argument. The function should return the value of the middle node in the
# linked list. If the linked list has an even number of nodes, then return the
# value of the second middle node.
# You may assume that the input list is non-empty.
#
# test_00:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# a -> b -> c -> d -> e
# middle_value(a) # c
# test_01:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# a -> b -> c -> d -> e -> f
# middle_value(a) # d
# test_02:
# x = Node('x')
# y = Node('y')
# z = Node('z')
# x.next = y
# y.next = z
# x -> y -> z
# middle_value(x) # y
# test_03:
# x = Node('x')
# y = Node('y')
# x.next = y
# x -> y 
# middle_value(x) # y
# test_04:
# q = Node('q')
# q
# middle_value(q) # q

# ========================= List =========================
# Time: O(n), Space: O(n)
def middle_value(head):
  values = []
  current = head 
  while current is not None:
    values.append(current)
    current = current.next
  middle = len(values) // 2
  return values[middle]

# ========================= Two Pointers =========================
# Time: O(n), Space: O(1)
def middle_value(head):
  slow = head 
  fast = head 
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
  return slow.val

# [[[[[[[[[[[[[[[[[[[[[[[[[ #76 linked list cycle ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, linked_list_cycle, that takes in the head of a linked list 
# as an argument. The function should return a boolean indicating whether or not 
# the linked list contains a cycle.
#
# test_00:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# a.next = b
# b.next = c
# c.next = d
# d.next = b # cycle
#         _______
#       /        \
# a -> b -> c -> d 
# linked_list_cycle(a)  # True
# test_01:
# q = Node('q')
# r = Node('r')
# s = Node('s')
# t = Node('t')
# u = Node('u')
# q.next = r
# r.next = s
# s.next = t
# t.next = u
# u.next = q # cycle
#    ________________
#  /                 \
# q -> r -> s -> t -> u 
# linked_list_cycle(q)  # True
# test_02
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# a.next = b
# b.next = c
# c.next = d

# a -> b -> c -> d 
# linked_list_cycle(a)  # False
# test_03:
# q = Node('q')
# r = Node('r')
# s = Node('s')
# t = Node('t')
# u = Node('u')
# q.next = r
# r.next = s
# s.next = t
# t.next = u
# u.next = t # cycle
#                   __
#                 /   \
# q -> r -> s -> t -> u 
# linked_list_cycle(q)  # True
# test_04:
# p = Node('p')
# p
# linked_list_cycle(p) # False
# test_05:
# linked_list_cycle(None) # False

# ========================= Set =========================
# Time: O(n), Space: O(n)
def linked_list_cycle(head):
  visited = set()
  current = head 
  while current is not None:
    if current.val in visited:
      return True
    visited.add(current.val)
    current = current.next
  return False

# ========================= Two Pointers =========================
# Time: O(n), Space: O(1)
def linked_list_cycle(head):
  first_iteration = True
  slow = head 
  fast = head 
  while fast is not None and fast.next is not None:
    if slow is fast and not first_iteration:
      return True
    first_iteration = False
    slow = slow.next
    fast = fast.next.next
  return False

# [[[[[[[[[[[[[[[[[[[[[[[[[ #77 lowest common ancestor ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, lowest_common_ancestor, that takes in the root of a binary
# tree and two values. The function should return the value of the lowest common
# ancestor of the two values in the tree.
# You may assume that the tree values are unique and the tree is non-empty.
# Note that a node may be considered an ancestor of itself.
# Example Tree:
# const a = Node('a');
# const b = Node('b');
# const c = Node('c');
# const d = Node('d');
# const e = Node('e');
# const f = Node('f');
# const g = Node('g');
# const h = Node('h');
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# e.right = h;
#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h
#
# test_00
# lowest_common_ancestor(a, 'd', 'h'); # b
# test_01
# lowest_common_ancestor(a, 'd', 'g'); # b
# test_02
# lowest_common_ancestor(a, 'g', 'c'); # a
# test_03
# lowest_common_ancestor(a, 'b', 'g'); # b
# test_04
# lowest_common_ancestor(a, 'f', 'c'); # c
# example tree
# const l = Node('l');
# const m = Node('m');
# const n = Node('n');
# const o = Node('o');
# const p = Node('p');
# const q = Node('q');
# const r = Node('r');
# const s = Node('s');
# const t = Node('t');
# l.left = m;
# l.right = n;
# n.left = o;
# n.right = p;
# o.left = q;
# o.right = r;
# p.left = s;
# p.right = t;
#        l
#     /     \
#    m       n
#         /    \
#         o     p
#        / \   / \
#       q   r s   t
# test_05
# lowest_common_ancestor(l, 'r', 'p'); # n
# test_06
# lowest_common_ancestor(l, 'm', 'o'); # l
# test_07
# lowest_common_ancestor(l, 't', 'q'); # n
# test_08
# lowest_common_ancestor(l, 's', 'p'); # p

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def lowest_common_ancestor(root, val1, val2):
  path1 = build_path(root, val1)  
  path2 = build_path(root, val2)
  set1 = set(path1)

  for val in path2:
    if val in set1:
      return val

def build_path(root, val):
  if root is None:
    return None
  if root.val == val:
    return [root.val]
  
  left_path = build_path(root.left, val)
  if left_path is not None:
    left_path.append(root.val)
    return left_path
  
  right_path = build_path(root.right, val)
  if right_path is not None:
    right_path.append(root.val)
    return right_path

  return None

# [[[[[[[[[[[[[[[[[[[[[[[[[ #78 flip tree ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, flip_tree, that takes in the root of a binary tree. The
# function should flip the binary tree, turning left subtrees into right
# subtrees and vice-versa. This flipping should occur in-place by modifying the
# original tree. The function should return the root of the tree.
#
# test_00
# const a = Node("a");
# const b = Node("b");
# const c = Node("c");
# const d = Node("d");
# const e = Node("e");
# const f = Node("f");
# const g = Node("g");
# const h = Node("h");
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# e.right = h;
#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h
# flip_tree(a); 
#       a
#    /    \
#   c      b
#  /     /   \
# f     e    d
#     /  \
#    h    g
# test_01
# const u = Node("u");
# const t = Node("t");
# const s = Node("s");
# const r = Node("r");
# const q = Node("q");
# const p = Node("p");
# u.left = t;
# u.right = s;
# s.right = r;
# r.left = q;
# r.right = p;
#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p
# flip_tree(u);
#           u
#        /    \
#       s      t
#      /
#     r
#    / \
#   p  q
# test_02
# const l = Node("l");
# const m = Node("m");
# const n = Node("n");
# const o = Node("o");
# const p = Node("p");
# const q = Node("q");
# const r = Node("r");
# const s = Node("s");
# const t = Node("t");
# l.left = m;
# l.right = n;
# n.left = o;
# n.right = p;
# o.left = q;
# o.right = r;
# p.left = s;
# p.right = t;
#        l
#     /     \
#    m       n
#         /    \
#         o     p
#        / \   / \
#       q   r s   t
# flip_tree(l);
#             l
#         /      \
#        n        m
#      /  \
#    p     o
#  / \    / \
# t   s  r   q
# test_03
# const n = Node("n");
# const y = Node("y");
# const c = Node("c");
# n.left = y;
# n.right = c;
#       n
#     /   \
#    y     c
# flip_tree(n);
#       n
#     /   \
#    c     y

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def flip_tree(root):
  if root is None:
    return None
  right = root.right
  left = root.left
  root.left = flip_tree(right)
  root.right = flip_tree(left)
  return root

# [[[[[[[[[[[[[[[[[[[[[[[[[ #79 lefty nodes ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, lefty_nodes, that takes in the root of a binary tree. The
# function should return an list containing the left-most value on every level
# of the tree. The list must be ordered in a top-down fashion where the root
# is the first element.
#
# test_00
# const a = Node('a');
# const b = Node('b');
# const c = Node('c');
# const d = Node('d');
# const e = Node('e');
# const f = Node('f');
# const g = Node('g');
# const h = Node('h');
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# e.right = h;
#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h
# lefty_nodes(a); # [ 'a', 'b', 'd', 'g' ]
# test_01
# const u = Node('u');
# const t = Node('t');
# const s = Node('s');
# const r = Node('r');
# const q = Node('q');
# const p = Node('p');
# u.left = t;
# u.right = s;
# s.right = r;
# r.left = q;
# r.right = p;
#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p
# lefty_nodes(u); # [ 'u', 't', 'r', 'q' ]
# test_02
# const l = Node('l');
# const m = Node('m');
# const n = Node('n');
# const o = Node('o');
# const p = Node('p');
# const q = Node('q');
# const r = Node('r');
# const s = Node('s');
# const t = Node('t');
# l.left = m;
# l.right = n;
# n.left = o;
# n.right = p;
# o.left = q;
# o.right = r;
# p.left = s;
# p.right = t;
#        l
#     /     \
#    m       n
#         /    \
#         o     p
#        / \   / \
#       q   r s   t
# lefty_nodes(l); # [ 'l', 'm', 'o', 'q' ]
# test_03
# const n = Node('n');
# const y = Node('y');
# const c = Node('c');
# n.left = y;
# n.right = c;
#       n
#     /   \
#    y     c
# lefty_nodes(n); # [ 'n', 'y' ]
# test_04
# const i = Node('i');
# const n = Node('n');
# const s = Node('s');
# const t = Node('t');
# i.right = n;
# n.left = s;
# n.right = t;
#       i
#        \
#         n
#        / \
#       s   t
# lefty_nodes(i); # [ 'i', 'n', 's' ]
# test_05
# lefty_nodes(None); # [ ]

# ========================= Breadth First =========================
# Time: O(n), Space: O(n)
def lefty_nodes(root):
  leftys = []
  if root is None:
    return []
  queue = deque([(root, 0)])
  while len(queue):
    node, level = queue.popleft()
    if len(leftys) == level:
      leftys.append(node.val)
    if node.left:
      queue.append((node.left, level + 1))
    if node.right:
      queue.append((node.right, level + 1))
  return leftys

# ========================= Depth First =========================
# Time: O(n), Space: O(n)
def lefty_nodes(root):
  values = []
  traverse(root, values, 0)
  return values

def traverse(root, values, level):
  if root is None:
    return 
  
  if len(values) == level:
    values.append(root.val)

  traverse(root.left, values, level + 1)
  traverse(root.right, values, level + 1)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #80 can color ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, can_color, that takes in a dictionary representing the 
# adjacency list of an undirected graph. The function should return a boolean 
# indicating whether or not it is possible to color nodes of the graph using two 
# colors in such a way that adjacent nodes are always different colors.
# For example, given this graph:
# x-y-z
# It is possible to color the nodes by using red for x and z, 
# then use blue for y. So the answer is True.
# For example, given this graph:
#     q
#    / \
#   s - r
# It is not possible to color the nodes without making two 
# adjacent nodes the same color. So the answer is False.

# test_00:
# can_color({
#   "x": ["y"],
#   "y": ["x","z"],
#   "z": ["y"]
# }) # -> True
# test_01:
# can_color({
#   "q": ["r", "s"],
#   "r": ["q", "s"],
#   "s": ["r", "q"]
# }) # -> False
# test_02:
# can_color({
#   "a": ["b", "c", "d"],
#   "b": ["a"],
#   "c": ["a"],
#   "d": ["a"],
# }) # -> True
# test_03:
# can_color({
#   "a": ["b", "c", "d"],
#   "b": ["a"],
#   "c": ["a", "d"],
#   "d": ["a", "c"],
# }) # -> False
# test_04:
# can_color({
#   "h": ["i", "k"],
#   "i": ["h", "j"],
#   "j": ["i", "k"],
#   "k": ["h", "j"],
# }) # -> True
# test_05:
# can_color({
#   "z": []
# }) # -> True
# test_06:
# can_color({
#   "h": ["i", "k"],
#   "i": ["h", "j"],
#   "j": ["i", "k"],
#   "k": ["h", "j"],
#   "q": ["r", "s"],
#   "r": ["q", "s"],
#   "s": ["r", "q"]
# }) # -> False

# ========================= Depth First =========================
# Time: O(n^2), Space: O(n)
def can_color(graph):
  colors = {}

  for node in graph:
    if node not in colors:
      if not colorable(graph, node, True, colors):
        return False 

  return True

def colorable(graph, node, red, colors):
  if node in colors:
    return colors[node] == red
  
  colors[node] = red
  for neighbor in graph[node]:
    if not colorable(graph, neighbor, (not red), colors):
      return False

  return True

# [[[[[[[[[[[[[[[[[[[[[[[[[ #81 tolerant teams ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, tolerant_teams, that takes in a list of rivalries as an 
# argument. A rivalry is a pair of people who should not be placed on the same 
# team. The function should return a boolean indicating whether or not it is 
# possible to separate people into two teams, without rivals being on the same 
# team. The two teams formed do not have to be the same size.
#
# test_00:
# tolerant_teams([
#   ('philip', 'seb'),
#   ('raj', 'nader')
# ]) # -> True
# test_01:
# tolerant_teams([
#   ('philip', 'seb'),
#   ('raj', 'nader'),
#   ('raj', 'philip'),
#   ('seb', 'raj')
# ]) # -> False
# test_02:
# tolerant_teams([
#   ('cindy', 'anj'),
#   ('alex', 'matt'),
#   ('alex', 'cindy'),
#   ('anj', 'matt'),
#   ('brando', 'matt')
# ]) # -> True
# test_03:
# tolerant_teams([
#   ('alex', 'anj'),
#   ('alex', 'matt'),
#   ('alex', 'cindy'),
#   ('anj', 'matt'),
#   ('brando', 'matt')
# ]) # -> False
# test_04:
# tolerant_teams([
#   ('alan', 'jj'),
#   ('betty', 'richard'),
#   ('jj', 'simcha'),
#   ('richard', 'christine')
# ]) # -> True
# test_05:
# tolerant_teams([
#   ('alan', 'jj'),
#   ('betty', 'richard'),
#   ('jj', 'simcha'),
#   ('richard', 'christine')
# ]) # -> True
# test_06:
# tolerant_teams([
#   ('alan', 'jj'),
#   ('jj', 'richard'),
#   ('betty', 'richard'),
#   ('jj', 'simcha'),
#   ('richard', 'christine')
# ]) # -> True
# test_07:
# tolerant_teams([
#   ('alan', 'jj'),
#   ('betty', 'richard'),
#   ('betty', 'christine'),
#   ('jj', 'simcha'),
#   ('richard', 'christine')
# ]) # -> False

# ========================= Depth First =========================
# Time: O(n^2), Space: O(n)
def tolerant_teams(rivalries):
  graph = build_graph(rivalries)

  tolerance = {}
  for node in graph:
    if node not in tolerance:
      if not tolerable(graph, node, tolerance, True):
        return False
  
  return True

def build_graph(rivalries):
  graph = {}

  for rivalry in rivalries:
    rival1, rival2 = rivalry

    if rival1 not in graph:
      graph[rival1] = []
    if rival2 not in graph:
      graph[rival2] = []

    graph[rival1].append(rival2)
    graph[rival2].append(rival1)
  
  return graph

def tolerable(graph, node, tolerance, team):
  if node in tolerance:
    return tolerance[node] == team
  
  tolerance[node] = team 
  for neighbor in graph[node]:
    if not tolerable(graph, neighbor, tolerance, not team):
      return False 

  return True

# [[[[[[[[[[[[[[[[[[[[[[[[[ #82 rare routing ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, rare_routing, that takes in a number of cities (n) and a list 
# of tuples where each tuple represents a direct road that connects a pair of 
# cities. The function should return a boolean indicating whether or not there 
# exists a unique route for every pair of cities. A route is a sequence of roads 
# that does not visit a city more than once.
# Cities will be numbered 0 to n - 1.
# You can assume that all roads are two-way roads. This means if there is a road 
# between A and B, then you can use that road to go from A to B or go from B to A.
# For example, given these roads:
# 0 --- 1
# | \
# |  \
# |   \
# 2    3
# There is a unique route for between every pair of cities.
# So the answer is True.
# For example, given these roads:
# 0 --- 1
# | \
# |  \
# |   \
# 2 -- 3
# There are two routes that can be used to travel from city 1 to city 2:
# - first route:  1, 0, 2
# - second route: 1, 0, 3, 2 
# The answer is False, because routes should be unique.
#
# test_00:
# rare_routing(4, [
#   (0, 1),
#   (0, 2),
#   (0, 3)
# ]) # -> True
# test_01:
# rare_routing(4, [
#   (0, 1),
#   (0, 2),
#   (0, 3),
#   (3, 2)
# ]) # -> False
# test_02:
# rare_routing(6, [
#   (1, 2),
#   (5, 4),
#   (3, 0),
#   (0, 1),
#   (0, 4),
# ]) # -> True

# ========================= Depth First =========================
# Time: O(n^2), Space: O(n)
def rare_routing(n, roads):
  graph = build_graph(n, roads)
  visited = set()
  valid = rare_route(graph, 0, visited, None)
  return valid and len(visited) == n

def rare_route(graph, node, visited, last_node):
  if node in visited:
    return False
  
  visited.add(node)
  for neighbor in graph[node]:
    if neighbor != last_node and not rare_route(graph, neighbor, visited, node):
      return False
  
  return True

def build_graph(n, roads):
  graph = {}

  for i in range(n):
    graph[i] = []

  for city1, city2 in roads:
    graph[city1].append(city2)
    graph[city2].append(city1)
  
  return graph

# [[[[[[[[[[[[[[[[[[[[[[[[[ #83 max increasing subseq ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, max_increasing_subseq, that takes in a list of numbers as an 
# argument. The function should return the length of the longest subsequence of 
# strictly increasing numbers.
# A subsequence of a list can be created by deleting any items of the list, while 
# maintaining the relative order of items.
#
# test_00:
# numbers = [4, 18, 20, 10, 12, 15, 19]
# max_increasing_subseq(numbers) # -> 5
# test_01:
# numbers = [12, 9, 2, 5, 4, 32, 90, 20]
# max_increasing_subseq(numbers) # -> 4
# test_02:
# numbers = [42, 50, 51, 60, 55, 70, 4, 5, 70]
# max_increasing_subseq(numbers) # -> 5
# test_03:
# numbers = [7, 14, 10, 12]
# max_increasing_subseq(numbers) # -> 3
# test_04:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# max_increasing_subseq(numbers) # -> 21
# test_05:
# numbers = [
#   1, 2, 3, 4, 5, 12, 6, 30, 7, 8, 9, 10, 11, 12, 13, 10, 18, 14, 15, 16, 17, 18, 19, 20, 21, 100,
#   104,
# ]
# max_increasing_subseq(numbers) # -> 23
# test_06:
# numbers = [
#   1, 2, 300, 3, 4, 305, 5, 12, 6, 30, 7, 8, 9, 10, 10, 10, 15, 11, 12, 13, 10, 18, 14, 15, 16,
#   17, 18, 19, 20, 21, 100,101 ,102, 103, 104, 105
# ]
# max_increasing_subseq(numbers) # -> 27

# ========================= Memoization =========================
# Time: O(n^2), Space: O(n^2)
def max_increasing_subseq(numbers):
  return _max_increasing_subseq(numbers, 0, float('-inf'), {})

def _max_increasing_subseq(numbers, i, lastNum, memo):
  key = (i, lastNum)
  if key in memo:
    return memo[key]
  if i == len(numbers):
    return 0
  
  options = []
  without_first = _max_increasing_subseq(numbers, i + 1, lastNum, memo)
  options.append(without_first)
  
  first = numbers[i]
  if first > lastNum:
    with_first = 1 + _max_increasing_subseq(numbers, i + 1, first, memo)
    options.append(with_first)
    
  memo[key] = max(options)
  return memo[key]

# [[[[[[[[[[[[[[[[[[[[[[[[[ #84 positioning plants ]]]]]]]]]]]]]]]]]]]]]]]]] 
# You've been hired to plant flowers in a garden with n different positions. 
# There are m different flower types. The prices of flowers types vary depending 
# on which position they are planted. Your bosses are picky, they tell you to 
# never plant two of the same flower type right next to each other. What is the 
# minimum cost we need to plant a flower in each position of the garden?
# Write a function, positioningPlants, that takes in a 2D list with dimensions 
# n * m. Each row of the list represents the costs of the flower types at that 
# position. This means that costs[i][j] represents the cost of planting flower 
# type j at position i. For example:
# Given these costs,
# costs = [
#   [4, 3, 7],
#   [6, 1, 9],
#   [2, 5, 3]
# ]
# The costs of plants at position 1 are $6, $1, and $9.
# The cost of planting flower type 0 at position 1 is $6.
# The cost of planting flower type 2 at position 1 is $9.
# The function should return the minimum cost of planting flowers without placing the same flower type in adjacent positions.
#
# test_00:
# positioning_plants([
#   [4, 3, 7],
#   [6, 1, 9],
#   [2, 5, 3]
# ]) # -> 7, by doing 4 + 1 + 2.
# test_01:
# positioning_plants([
#   [12, 14, 5],
#   [6, 3, 2]
# ]) # -> 8
# test_02:
# positioning_plants([
#   [12, 14, 5],
#   [6, 3, 2],
#   [4, 2, 7],
#   [4, 8, 4],
#   [1, 13, 5],
#   [8, 6, 7],
# ]) # -> 23
# test_03:
# positioning_plants([
#   [12, 14, 5, 13],
#   [6, 3, 20, 3],
#   [24, 12, 7, 2],
#   [4, 80, 45, 3],
#   [104, 13, 5, 14],
#   [38, 19, 7, 6],
#   [12, 2, 1, 2],
# ]) # -> 26
# test_04:
# positioning_plants([
#   [12, 14, 50, 12],
#   [6, 3, 20, 3],
#   [24, 12, 7, 2],
#   [4, 80, 45, 3],
#   [104, 13, 5, 14],
#   [38, 19, 7, 6],
#   [1, 20, 1, 2],
#   [13, 12, 5, 13],
#   [60, 32, 20, 3],
#   [24, 12, 7, 2],
#   [4, 80, 44, 1],
#   [104, 13, 5, 14],
#   [38, 19, 76, 6],
#   [12, 23, 12, 20],
#   [1, 3, 1, 1],
#   [1, 2, 12, 5],
# ]) # -> 74
# test_05:
# positioning_plants([
#   [12, 14, 50, 12, 13],
#   [6, 3, 20, 3, 16],
#   [24, 12, 7, 2, 74],
#   [4, 80, 45, 3, 100],
#   [104, 13, 5, 14, 3],
#   [38, 19, 7, 6, 24],
#   [1, 20, 1, 2, 31],
#   [13, 12, 5, 13, 9],
#   [60, 32, 20, 3, 2],
#   [24, 12, 7, 2, 42],
#   [4, 80, 44, 1, 23],
#   [104, 13, 5, 14, 28],
#   [38, 19, 76, 6, 12],
#   [12, 23, 12, 20, 13],
#   [1, 3, 1, 1, 50],
#   [1, 2, 12, 5, 36],
#   [6, 2, 3, 12, 20],
#   [4, 6, 4, 11, 15],
# ]) # -> 75

# ========================= Memoization =========================
# n: num rows, m: num cols
# Time: O(nm), Space: O(nm)
def positioning_plants(costs):
  return plant_cost(costs, 0, None, {})

def plant_cost(costs, r, c, memo):
  print((r, c))
  if r == len(costs):
    return 0
  if (r, c) in memo:
    return memo[(r, c)]
  
  min_cost = float('inf')
  for i, cost in enumerate(costs[r]):
    if i != c:
      total = cost + plant_cost(costs, r + 1, i, memo)
      min_cost = min(total, min_cost)

  memo[(r, c)] = min_cost
  return min_cost

# [[[[[[[[[[[[[[[[[[[[[[[[[ #85 breaking boundaries ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, breaking_boundaries, that takes in 5 arguments: a number of 
# rows (m), a number of columns (n), a number of moves (k), a starting row (r), 
# and a starting column (c). Say you were situated in a grid with dimensions 
# m * n. If you had to start at position (r,c), in how many different ways could 
# you move out of bounds if you could take at most k moves. A single move is 
# moving one space up, down, left, or right. During a path you may revisit a 
# position.
# For example:
# Given m, n, k, r, c:
# 3, 4, 2, 0, 0
# This input asks us to count the numbers of ways
# to move out of bounds in a 3 by 4 grid, starting at
# position (0, 0) if we could take at most 2 moves.
# The answer is 4 because of these 4 distinct ways:
#  1. left
#  2. up
#  3. right, up
#  4. down, left
# The function should return a number representing how many ways you can move out 
# of bounds.
#
# test_00:
# breaking_boundaries(3, 4, 2, 0, 0) # -> 4
# test_01:
# breaking_boundaries(2, 2, 2, 1, 1) # -> 6
# test_02:
# breaking_boundaries(3, 4, 3, 0, 0) # -> 11
# test_03:
# breaking_boundaries(4, 4, 5, 2, 1) # -> 160
# test_04:
# breaking_boundaries(5, 6, 9, 2, 5) # -> 11635
# test_05:
# breaking_boundaries(6, 6, 12, 3, 4) # -> 871065
# test_06:
# breaking_boundaries(6, 6, 15, 3, 4) # -> 40787896
# test_07:
# breaking_boundaries(6, 8, 16, 2, 1) # -> 137495089

# ========================= Memoization =========================
# m: num rows, n: num cols, k: num steps
# Time: O(mnk), Space: O(mnk)
def breaking_boundaries(m, n, k, r, c):
  return _breaking_boundaries(m, n, k, r, c, {})

def _breaking_boundaries(m, n, k, r, c, memo):
  if (r, c) in memo:
    return memo[(r, c)]
  if r < 0 or r == m or c < 0 or c == n:
    return 1
  if k == 0:
    return 0

  moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  count = 0
  for dy, dx in moves:
    new_y, new_x = r + dy, c + dx
    count += _breaking_boundaries(m, n, k - 1, new_y, new_x)

  memo[(r, c)] = count
  return count

# [[[[[[[[[[[[[[[[[[[[[[[[[ #86 merge sort ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, merge_sort, that takes in a list of numbers as an argument. 
# The function should return return a new list containing elements of the 
# original list sorted in ascending order. Your function must implement the merge 
# sort algorithm.
#
# test_00
# numbers = [10, 4, 42, 5, 8, 100, 5, 6, 12, 40]
# merge_sort(numbers)
# # -> [ 4, 5, 5, 6, 8, 10, 12, 40, 42, 100 ] 
# test_01
# numbers = [7, -30, -4, -1, 12, 0, 20]
# merge_sort(numbers)
# # -> [ -30, -4, -1, 0, 7, 12, 20 ] 
# test_02
# numbers = [8, 7, 6, 5, 4, 3, 2, 1, 0]
# merge_sort(numbers)
# # -> [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] 
# test_03
# numbers = [
#   72, 42, 16, 81, 84, 17,  2, 81, 22, 79, 86, 38, 
#   77, 80, 81, 70, 81, 80, 35, 21, 89, 38, 57, 28, 
#    4, 17, 50, 38, 68, 82, 22, 76, 45, 40, 67, 94, 
#   37, 27, 81, 53, 36, 18, 28, 60, 45, 74, 40, 29, 
#   18,  6, 28, 57, 42, 60, 64, 12, 78, 97, 96,  1, 
#   20, 20, 61, 67, 82, 10, 63, 71, 39, 52, 37, 69, 
#   37, 24, 66, 74, 15, 92, 49, 31, 56, 67, 50, 57, 
#   79,  0, 21, 56, 82, 22,  4, 20, 91, 72, 58, 93, 
#   99, 14, 42, 91 
# ]
# merge_sort(numbers)
# # -> [ 
# #    0,  1,  2,  4,  4,  6, 10, 12, 14, 15, 16, 17, 
# #   17, 18, 18, 20, 20, 20, 21, 21, 22, 22, 22, 24, 
# #   27, 28, 28, 28, 29, 31, 35, 36, 37, 37, 37, 38, 
# #   38, 38, 39, 40, 40, 42, 42, 42, 45, 45, 49, 50, 
# #   50, 52, 53, 56, 56, 57, 57, 57, 58, 60, 60, 61, 
# #   63, 64, 66, 67, 67, 67, 68, 69, 70, 71, 72, 72, 
# #   74, 74, 76, 77, 78, 79, 79, 80, 80, 81, 81, 81, 
# #   81, 81, 82, 82, 82, 84, 86, 89, 91, 91, 92, 93, 
# #   94, 96, 97, 99 
# # ]
# test_04
# numbers = [7] * 95000
# merge_sort(numbers)
# # -> [7, 7, 7, 7, 7, ...]
# test_05
# numbers = [7] * 120000
# merge_sort(numbers)
# # -> [7, 7, 7, 7, 7, ...]

# ========================= Merge Sort =========================
# Time: O(n * log(n)), Space: O(n)
from collections import deque

def merge_sort(nums):
  if len(nums) <= 1:
    return nums
  
  mid = len(nums) // 2
  sorted_left = merge_sort(nums[:mid])
  sorted_right = merge_sort(nums[mid:])

  return merge(sorted_left, sorted_right)

def merge(left, right):
  res = []
  list_1 = deque(left)
  list_2 = deque(right)

  while list_1 and list_2:
    if list_1[0] < list_2[0]:
      res.append(list_1.popleft())
    else:
      res.append(list_2.popleft())
  
  res += list_1 
  res += list_2

  return res

# [[[[[[[[[[[[[[[[[[[[[[[[[ #87 combine intervals ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, combine_intervals, that takes in an a list of intervals as an 
# argument. Each interval is a tuple containing a pair of numbers representing a 
# start and end time. Your function should combine overlapping intervals and 
# return a list containing the combined intervals.
# For example:
# Given two intervals:
# (1, 4) and (3, 7)
# The intervals overlap and
# should be combined into:
# (1, 7)
# You may return the combined intervals in any order.
# You can assume that the input list contains at least one interval and all intervals are valid with start < end.
#
# test_00
# intervals = [
#   (1, 4),
#   (12, 15),
#   (3, 7),
#   (8, 13),
# ]
# combine_intervals(intervals)
# # -> [ (1, 7), (8, 15) ]
# test_01
# intervals = [
#   (6, 8),
#   (2, 9),
#   (10, 12),
#   (20, 24),
# ]
# combine_intervals(intervals)
# # -> [ (2, 9), (10, 12), (20, 24) ]
# test_02
# intervals = [
#   (3, 7),
#   (5, 8),
#   (1, 5),
# ]
# combine_intervals(intervals)
# # -> [ (1, 8) ]
# test_03
# intervals = [
#   (3, 7),
#   (10, 13),
#   (5, 8),
#   (27, 31),
#   (1, 5),
#   (12, 16),
#   (20, 22),
# ]
# combine_intervals(intervals)
# # -> [ (1, 8), (10, 16), (20, 22), (27, 31) ]
# test_04
# intervals = [
#   (3, 7),
#   (10, 13),
#   (5, 8),
#   (27, 31),
#   (1, 5),
#   (12, 16),
#   (20, 32),
# ]
# combine_intervals(intervals)
# # -> [ (1, 8), (10, 16), (20, 32) ]
# test_05
# intervals = [
#   (64, 70),
#   (50, 55),
#   (62, 65),
#   (12, 50),
#   (72, 300000),
# ]
# combine_intervals(intervals)
# # -> [ (12, 55), (62, 70), (72, 300000) ]

# ========================= Sort and Combine =========================
# Time: O(n * log(n)), Space: O(n)
def combine_intervals(intervals):
  sorted_intervals = sorted(intervals)
  combined = [sorted_intervals[0]]

  for interval in sorted_intervals[1:]:
    curr_start, curr_end = interval 
    last_start, last_end = combined[-1]
    if curr_start <= last_end:
      if curr_end > last_end:
        combined[-1] = (last_start, curr_end)
    else:
      combined.append(interval)
  
  return combined

# [[[[[[[[[[[[[[[[[[[[[[[[[ #88 binary search ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, binary_search, that takes in a sorted list of numbers and a 
# target. The function should return the index where the target can be found 
# within the list. If the target is not found in the list, then return -1.
# You may assume that the input list contains unique numbers sorted in 
# increasing order.
# Your function must implement the binary search algorithm.
#
# test_00
# binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 6) # -> 6
# test_01
# binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 27) # -> -1
# test_02
# binary_search([0, 6, 8, 12, 16, 19, 20, 28], 8) # -> 2
# test_03
# binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 28) # -> 8
# test_04
# binary_search([7, 9], 7) # -> 0
# test_05
# binary_search([7, 9], 9) # -> 1
# test_06
# binary_search([7, 9], 12) # -> -1
# test_07
# binary_search([7], 7) # -> 0
# test_08
# binary_search([], 7) # -> -1

# ========================= Iterative Bsearch =========================
# Time: O(log(n)), Space: O(1)
def binary_search(numbers, target):
  lo = 0
  hi = len(numbers) - 1
  while lo <= hi:
      mid = (lo + hi) // 2
      search = numbers[mid]
      if search == target:
        return mid
      elif search < target:
        lo = mid + 1
      else:
        hi = mid - 1
  return -1

# [[[[[[[[[[[[[[[[[[[[[[[[[ #89 binary search tree includes ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, binary_search_tree_includes, that takes in the root of a 
# binary search tree containing numbers and a target value. The function should 
# return a boolean indicating whether or not the target is found within the tree.
# A Binary Search Tree is a binary tree where all values within a node's left 
# subtree are smaller than the node's value and all values in a node's right 
# subtree are greater than or equal to the node's value.
# Your solution should have a best case runtime of O(log(n)).
#
# tree a
# a = Node(12)
# b = Node(5)
# c = Node(18)
# d = Node(3)
# e = Node(9)
# f = Node(19)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      12
#    /   \
#   5     18
#  / \     \
# 3   9     19
#
# test_00:
# binary_search_tree_includes(a, 9) # -> True
# test_01:
# binary_search_tree_includes(a, 15) # -> False
# test_02:
# binary_search_tree_includes(a, 1) # -> False
# test_03:
# binary_search_tree_includes(a, 12) # -> True
# tree q
# q = Node(54)
# r = Node(42)
# s = Node(70)
# t = Node(31)
# u = Node(50)
# v = Node(72)
# w = Node(47)
# x = Node(90)
# q.left = r
# q.right = s
# r.left = t
# r.right = u
# s.right = v
# u.left = w
# v.right = x
#       54
#     /    \
#    42     70
#   / \      \
# 31   50     72
#     /        \
#    47         90
# test_04:
# binary_search_tree_includes(q, 55) # -> False
# test_05:
# binary_search_tree_includes(q, 47) # -> True
# test_06:
# binary_search_tree_includes(q, 49) # -> False
# test_07:
# binary_search_tree_includes(q, 70) # -> True
# test_08:
# binary_search_tree_includes(q, 100) # -> False

# ========================= Binary Search =========================
# Worst Case
# Time: O(n), Space: O(n)
# Best Case (Balanced Tree)
# Time: O(log(n)), Space: O(log(n))
def binary_search_tree_includes(root, target):
  if root is None:
    return False 
  if root.val == target:
    return True

  if target < root.val:
    return binary_search_tree_includes(root.left, target)
  else:
    return binary_search_tree_includes(root.right, target)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #90 is binary search tree ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, is_binary_search_tree, that takes in the root of a binary 
# tree. The function should return a boolean indicating whether or not the tree 
# satisfies the binary search tree property.
# A Binary Search Tree is a binary tree where all values within a node's left 
# subtree are smaller than the node's value and all values in a node's right 
# subtree are greater than or equal to the node's value.
#
# test_00:
# a = Node(12)
# b = Node(5)
# c = Node(18)
# d = Node(3)
# e = Node(9)
# f = Node(19)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      12
#    /   \
#   5     18
#  / \     \
# 3   9     19
# is_binary_search_tree(a) # -> True
# test_01:
# a = Node(12)
# b = Node(5)
# c = Node(18)
# d = Node(3)
# e = Node(15)
# f = Node(19)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      12
#    /   \
#   5     18
#  / \     \
# 3   15     19
# is_binary_search_tree(a) # -> False
# test_02:
# a = Node(12)
# b = Node(5)
# c = Node(19)
# d = Node(3)
# e = Node(9)
# f = Node(19)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      12
#    /   \
#   5     19
#  / \     \
# 3   9     19
# is_binary_search_tree(a) # -> True
# test_03:
# a = Node(12)
# b = Node(5)
# c = Node(10)
# d = Node(3)
# e = Node(9)
# f = Node(19)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#      12
#    /   \
#   5     10
#  / \     \
# 3   9     19
# is_binary_search_tree(a) # -> False
# test_04:
# q = Node(54)
# r = Node(42)
# s = Node(70)
# t = Node(31)
# u = Node(50)
# v = Node(72)
# w = Node(47)
# x = Node(90)
# q.left = r
# q.right = s
# r.left = t
# r.right = u
# s.right = v
# u.left = w
# v.right = x
#       54
#     /    \
#    42     70
#   / \      \
# 31   50     72
#     /        \
#    47         90
# is_binary_search_tree(q) # -> True

# ========================= In Order Traversal =========================
# Time: O(n), Space: O(n)
def is_binary_search_tree(root):
  values = []
  in_order_traversal(root, values)
  return is_sorted(values)

def in_order_traversal(root, values):
  if root is None:
    return
  
  in_order_traversal(root.left, values)
  values.append(root.val)
  in_order_traversal(root.right, values)

def is_sorted(nums):
  for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
      return False 
  return True

# [[[[[[[[[[[[[[[[[[[[[[[[[ #91 post order ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, post_order, that takes in the root of a binary tree. The 
# function should return a list containing the post-ordered values of the tree.
# Post-order traversal is when nodes are recursively visited in the order: left 
# child, right child, self.
#
# test_00:
# x = Node('x')
# y = Node('y')
# z = Node('z')
# x.left = y
# x.right = z
#       x
#    /    \
#   y      z
# post_order(x)
# ['y', 'z', 'x']
# test_01:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.left = f
# c.right = g
#      a
#    /    \
#   b      c
#  / \    / \
# d   e  f   g
# post_order(a)
# [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 
# test_02:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# h = Node('h')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# e.right = h
#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h
# post_order(a)
# [ 'd', 'g', 'h', 'e', 'b', 'f', 'c', 'a' ] 
# test_03:
# l = Node('l')
# m = Node('m')
# n = Node('n')
# o = Node('o')
# p = Node('p')
# q = Node('q')
# r = Node('r')
# s = Node('s')
# t = Node('t')
# l.left = m
# l.right = n
# n.left = o
# n.right = p
# o.left = q
# o.right = r
# p.left = s
# p.right = t
#        l
#     /     \
#    m       n
#         /    \
#         o     p
#        / \   / \
#       q   r s   t
# post_order(l)
# [ 'm', 'q', 'r', 'o', 's', 't', 'p', 'n', 'l' ] 
# test_04:
# post_order(None)
# []

# ========================= Post Order Traversal =========================
# Time: O(n), Space: O(n)
def post_order(root):
  values = []
  _post_order(root, values)
  return values 

def _post_order(root, values):
  if root is None:
    return 
  
  _post_order(root.left)
  _post_order(root.right)
  values.append(root.val)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #92 build tree in post ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, build_tree_in_post, that takes in a list of in-ordered values 
# and a list of post-ordered values for a binary tree. The function should build 
# a binary tree that has the given in-order and post-order traversal structure. 
# The function should return the root of this tree.
# You can assume that the values of inorder and postorder are unique.
#
# test_00
# build_tree_in_post(
#   [ 'y', 'x', 'z' ],
#   [ 'y', 'z', 'x' ] 
# )
#       x
#    /    \
#   y      z
# test_01
# build_tree_in_post(
#   [ 'd', 'b', 'e', 'a', 'f', 'c', 'g' ],
#   [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 
# )
#      a
#    /    \
#   b      c
#  / \    / \
# d   e  f   g
# test_02
# build_tree_in_post(
#   [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
#   [ 'd', 'g', 'h', 'e', 'b', 'f', 'c', 'a' ] 
# )
#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h
# test_03
# build_tree_in_post(
#   ['m', 'n'],
#   ['m', 'n']
# )
#       n
#     /
#    m
# test_04
# build_tree_in_post(
#   ['n', 'm'],
#   ['m', 'n']
# )
#     n
#      \
#       m

# ========================= Recursive (Slicing) =========================
# Time: O(n^2), Space: O(n^2)
def build_tree_in_post(in_order, post_order):
  if len(post_order) == 0:
    return None
  
  root_val = post_order[-1]
  left_length = in_order.index(root_val)
  left_in_order = in_order[:left_length]
  right_in_order = in_order[(left_length + 1):]
  left_post_order = post_order[:left_length]
  right_post_order = post_order[left_length:-1]

  root = Node(root_val)
  root.left = build_tree_in_post(left_in_order, left_post_order)
  root.right = build_tree_in_post(right_in_order, right_post_order)
  return root

# [[[[[[[[[[[[[[[[[[[[[[[[[ #93 build tree in pre ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, build_tree_in_pre, that takes in a list of in-ordered values 
# and a list of pre-ordered values for a binary tree. The function should build 
# a binary tree that has the given in-order and pre-order traversal structure. 
# The function should return the root of this tree.
# You can assume that the values of inorder and preorder are unique.
#
# test_00
# build_tree_in_pre(
#   [ 'z', 'y', 'x' ],
#   [ 'y', 'z', 'x' ] 
# )
#       y
#    /    \
#   z      x
# test_01
# build_tree_in_pre(
#   [ 'y', 'z', 'x' ],
#   [ 'y', 'x', 'z' ] 
# )
#       y
#        \
#         x
#        / 
#       z
# test_02
# build_tree_in_pre(
#   [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
#   [ 'a', 'b', 'd', 'e', 'g', 'h', 'c', 'f' ] 
# )
#       a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h
# test_03
# build_tree_in_pre(
#   [ 't', 'u', 's', 'q', 'r', 'p' ],
#   [ 'u', 't', 's', 'r', 'q', 'p' ] 
# )
#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p
# test_04
# build_tree_in_pre(
#   [ 'm', 'l', 'q', 'o', 'r', 'n', 's', 'p', 't' ],
#   [ 'l', 'm', 'n', 'o', 'q', 'r', 'p', 's', 't' ] 
# )
#        l
#     /     \
#    m       n
#         /    \
#         o     p
#        / \   / \
#       q   r s   t

# ========================= Recursive (In-Place) =========================
# Time: O(n), Space: O(n)
def build_tree_in_pre(in_order, pre_order):
  return _build_tree(in_order, pre_order, 0, len(in_order) - 1, 0, len(pre_order) - 1)

def _build_tree(in_order, pre_order, in_start, in_end, pre_start, pre_end):
  if in_start > in_end:
    return None
    
  root_val = pre_order[pre_start]
  mid = in_order.index(root_val)
  left_length = mid - in_start
  left_in_end = mid - 1
  right_in_start = mid + 1
  left_pre_start = pre_start + 1
  left_pre_end = pre_start + left_length
  right_pre_start = pre_start + left_length + 1
  
  root = Node(root_val)
  root.left = _build_tree(in_order, pre_order, in_start, left_in_end, left_pre_start, left_pre_end)
  root.right = _build_tree(in_order, pre_order, right_in_start, in_end, right_pre_start, pre_end)
  return root

# [[[[[[[[[[[[[[[[[[[[[[[[[ #94 lexical order ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, lexical_order, that takes in 2 words and an alphabet string 
# as an argument. The function should return True if the first word should appear 
# before the second word if lexically-ordered according to the given alphabet 
# order. If the second word should appear first, then return False.
# Note that the alphabet string may be any arbitrary string.
# Intuitively, Lexical Order is like "dictionary" order:
# You can assume that all characters are lowercase a-z.
# You can assume that the alphabet contains all 26 letters.
#
# test_00:
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# lexical_order("apple", "dock", alphabet) # -> True
# test_01:
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# lexical_order("apple", "ample", alphabet) # -> False
# test_02:
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# lexical_order("app", "application", alphabet) # -> True
# test_03:
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# lexical_order("backs", "backdoor", alphabet) # -> False
# test_04:
# alphabet = "ghzstijbacdopnfklmeqrxyuvw"
# lexical_order("zoo", "dinner", alphabet) # -> True
# test_05:
# alphabet = "ghzstijbacdopnfklmeqrxyuvw"
# lexical_order("leaper", "leap", alphabet) # -> False
# test_06:
# alphabet = "ghzstijbacdopnfklmeqrxyuvw"
# lexical_order("backs", "backdoor", alphabet) # -> True
# test_07:
# alphabet = "ghzstijbacdopnfklmeqrxyuvw"
# lexical_order("semper", "semper", alphabet) # -> True

# ========================= Iterative =========================
# Time: O(n), Space: O(1)
def lexical_order(word_1, word_2, alphabet):
  for i in range(min(len(word_1), len(word_2))):
    char_1 = word_1[i]
    char_2 = word_2[i]
    if char_1 == char_2:
      pass 
    else:
      if alphabet.index(char_1) > alphabet.index(char_2):
        return False 
      else:
        return True
  
  return len(word_1) <= len(word_2)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #95 detect dictionary ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, detect_dictionary, that takes in a dictionary of words and an 
# alphabet string. The function should return a boolean indicating whether or not 
# all words of the dictionary are lexically-ordered according to the alphabet.
# You can assume that all characters are lowercase a-z.
# You can assume that the alphabet contains all 26 letters.
#
# test_00:
# dictionary = ["zoo", "tick", "tack", "door"]
# alphabet = "ghzstijbacdopnfklmeqrxyuvw"
# detect_dictionary(dictionary, alphabet) # -> True
# test_01:
# dictionary = ["zoo", "tack", "tick", "door"]
# alphabet = "ghzstijbacdopnfklmeqrxyuvw"
# detect_dictionary(dictionary, alphabet) # -> False
# test_02:
# dictionary = ["zoos", "zoo", "tick", "tack", "door"]
# alphabet = "ghzstijbacdopnfklmeqrxyuvw"
# detect_dictionary(dictionary, alphabet) # -> False
# test_03:
# dictionary = ["miles", "milestone", "proper", "process", "goal"]
# alphabet = "mnoijpqrshkltabcdefguvwzxy"
# detect_dictionary(dictionary, alphabet) # -> True
# test_04:
# dictionary = ["miles", "milestone", "pint", "proper", "process", "goal"];
# alphabet = "mnoijpqrshkltabcdefguvwzxy"
# detect_dictionary(dictionary, alphabet) # -> True
# test_05:
# dictionary = ["miles", "milestone", "pint", "proper", "process","goal", "apple"];
# alphabet = "mnoijpqrshkltabcdefguvwzxy"
# detect_dictionary(dictionary, alphabet) # -> False

# ========================= Iterative =========================
# n: num words, k: length of longest word
# Time: O(nk), Space: O(1)
def detect_dictionary(dictionary, alphabet):
  for i in range(len(dictionary) - 1):
    if not lexical_order(dictionary[i], dictionary[i + 1], alphabet):
      return False

  return True

def lexical_order(word_1, word_2, alphabet):
  for i in range(min(len(word_1), len(word_2))):
    char_1 = word_1[i]
    char_2 = word_2[i]
    if char_1 == char_2:
      pass 
    else:
      if alphabet.index(char_1) > alphabet.index(char_2):
        return False 
      else:
        return True
  
  return len(word_1) <= len(word_2)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #96 topological order ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, topological_order, that takes in a dictionary representing 
# the adjacency list for a directed-acyclic graph. The function should return a 
# list containing the topological-order of the graph.
# The topological ordering of a graph is a sequence where "parent nodes" appear 
# before their "children" within the sequence.
#
# test_00:
# topological_order({
#   "a": ["f"],
#   "b": ["d"],
#   "c": ["a", "f"],
#   "d": ["e"],
#   "e": [],
#   "f": ["b", "e"],
# }) # -> ['c', 'a', 'f', 'b', 'd', 'e']
# test_01:
# topological_order({
#   "h": ["l", "m"],
#   "i": ["k"],
#   "j": ["k", "i"],
#   "k": ["h", "m"],
#   "l": ["m"],
#   "m": [],
# }) # -> ['j', 'i', 'k', 'h', 'l', 'm']
# test_02:
# topological_order({
#   "q": [],
#   "r": ["q"],
#   "s": ["r"],
#   "t": ["s"],
# }) # -> ['t', 's', 'r', 'q']
# test_03:
# topological_order({
#   "v": ["z", "w"],
#   "w": [],
#   "x": ["w", "v", "z"],
#   "y": ["x"],
#   "z": ["w"],
# }) # -> ['y', 'x', 'v', 'z', 'w']

# ========================= Kahn's Algorithm =========================
# n: num nodes, e: num edges
# Time: O(n + e), Space: O(n)
def topological_order(graph):
  num_parents = {}
  for node in graph:
    num_parents[node] = 0
  
  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1
  
  top_most = [ node for node in graph if num_parents[node] == 0 ]
  order = []
  while top_most:
    node = top_most.pop()
    order.append(node)
    for child in graph[node]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        top_most.append(child)
  
  return order

# [[[[[[[[[[[[[[[[[[[[[[[[[ #97 safe cracking ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Oh-no! You forgot the number combination that unlocks your safe. Luckily, you 
# knew that you'd be forgetful so you previously wrote down a bunch of hints that 
# can be used to determine the correct combination. Each hint is a pair of 
# numbers 'x, y' that indicates you must enter digit 'x' before 'y' (but not 
# necessarily immediately before y).
# The keypad on the safe has digits 0-9. You can assume that the hints will 
# generate exactly one working combination and that a digit can occur zero or 
# one time in the answer.
# Write a function, safe_cracking, that takes in a list of hints as an argument 
# and determines the combination that will unlock the safe. The function should 
# return a string representing the combination.
#
# test_00:
# safe_cracking([
#   (7, 1),
#   (1, 8),
#   (7, 8),
# ]) # -> '718'
# test_01:
# safe_cracking([
#   (3, 1),
#   (4, 7),
#   (5, 9),
#   (4, 3),
#   (7, 3),
#   (3, 5),
#   (9, 1),
# ]) # -> '473591'
# test_02:
# safe_cracking([
#   (2, 5),
#   (8, 6),
#   (0, 6),
#   (6, 2),
#   (0, 8),
#   (2, 3),
#   (3, 5),
#   (6, 5),
# ]) # -> '086235'
# test_03:
# safe_cracking([
#   (0, 1),
#   (6, 0),
#   (1, 8),
# ]) # -> '6018'
# test_04:
# safe_cracking([
#   (8, 9),
#   (4, 2),
#   (8, 2),
#   (3, 8),
#   (2, 9),
#   (4, 9),
#   (8, 4),
# ]) # -> '38429'

# ========================= Kahn's Algorithm =========================
# n: num nodes, e: num edges
# Time: O(n + e), Space: O(n)
def safe_cracking(hints):
  graph = build_graph(hints)
  num_parents = {}
  for node in graph:
    num_parents[node] = 0
  
  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1
  
  top_most = [ node for node in graph if num_parents[node] == 0 ]
  combination = ''
  while top_most:
    node = top_most.pop()
    combination += str(node)
    for child in graph[node]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        top_most.append(child)
  
  return combination

def build_graph(edges):
  graph = {}
  
  for num_1, num_2 in edges:
    if num_1 not in graph:
      graph[num_1] = []
    if num_2 not in graph:
      graph[num_2] = []
    graph[num_1].append(num_2)

  return graph

# [[[[[[[[[[[[[[[[[[[[[[[[[ #98 string search ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, string_search, that takes in a grid of letters and a string 
# as arguments. The function should return a boolean indicating whether or not 
# the string can be found in the grid as a path by connecting horizontal or 
# vertical positions. The path can begin at any position, but you cannot reuse a 
# position more than once in the path.
# You can assume that all letters are lowercase and alphabetic.
#
# test_00:
# grid = [
#   ['e', 'y', 'h', 'i', 'j'],
#   ['q', 'x', 'e', 'r', 'p'],
#   ['r', 'o', 'l', 'l', 'n'],
#   ['p', 'r', 'x', 'o', 'h'],
#   ['a', 'a', 'm', 'c', 'm']
# ]
# string_search(grid, 'hello') # -> True
# test_01:
# grid = [
#   ['e', 'y', 'h', 'i', 'j'],
#   ['q', 'x', 'e', 'r', 'p'],
#   ['r', 'o', 'l', 'l', 'n'],
#   ['p', 'r', 'x', 'o', 'h'],
#   ['a', 'a', 'm', 'c', 'm']
# ]
# string_search(grid, 'proxy') # -> True
# test_02:
# grid = [
#   ['e', 'y', 'h', 'i', 'j'],
#   ['q', 'x', 'e', 'r', 'p'],
#   ['r', 'o', 'l', 'l', 'n'],
#   ['p', 'r', 'x', 'o', 'h'],
#   ['a', 'a', 'm', 'c', 'm']
# ]
# string_search(grid, 'rolling') # -> False
# test_03:
# grid = [
#   ['e', 'y', 'h', 'i', 'j'],
#   ['q', 'x', 'e', 'r', 'p'],
#   ['r', 'o', 'l', 'l', 'n'],
#   ['p', 'r', 'x', 'o', 'h'],
#   ['a', 'a', 'm', 'z', 'm']
# ]
# string_search(grid, 'zoo') # -> False
# test_04:
# grid = [
#   ['q', 'w', 'h', 'i', 'j'],
#   ['q', 'e', 'r', 'o', 'p'],
#   ['h', 'y', 't', 'x', 'z'],
#   ['k', 'o', 'm', 'o', 'p']
# ]
# string_search(grid, 'qwerty') # -> True
# test_05:
# grid = [ 
#   [ 'f', 'd', 'i', 'e', 'l', 'u', 'j', 't', 'q', 'v', 'o', 'p' ], 
#   [ 'o', 'p', 'b', 'e', 'm', 'w', 'm', 'l', 'h', 'j', 's', 'v' ], 
#   [ 'g', 'b', 's', 'm', 'i', 'w', 'w', 'h', 'l', 'm', 'l', 'n' ], 
#   [ 'a', 'l', 's', 'k', 'p', 'c', 't', 'u', 'v', 'b', 'c', 'm' ], 
#   [ 'm', 't', 'c', 'k', 'e', 'n', 'r', 'b', 'a', 'z', 'l', 'c' ], 
#   [ 'q', 'm', 'a', 'p', 'a', 'p', 'i', 'i', 'u', 't', 'z', 'z' ], 
#   [ 'd', 'u', 'z', 'o', 'e', 'r', 'a', 't', 't', 'c', 'q', 'k' ], 
#   [ 'f', 'u', 'z', 'g', 'c', 'i', 'k', 'v', 'o', 'f', 's', 'w' ], 
#   [ 'p', 'h', 'u', 'i', 'k', 'c', 'v', 'v', 'h', 'q', 'v', 'i' ], 
#   [ 'l', 'q', 'w', 'f', 'y', 'g', 'w', 'f', 'a', 'u', 'x', 'q' ] 
# ]
# string_search(grid, 'paprika') # -> True
# test_06:
# grid = [
#     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
#     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
#     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
#     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
#     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
#     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
#     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
#     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'x' ],
#     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'h' ],
# ]
# string_search(grid, 'ssssssssssh') # -> False

# ========================= Depth First =========================
# r: num rows, c: num cols, s: length of string
# Time: O(s^(rc)), Space: O(rc) 
# Alvin says the time complexity is O(3^(rc)), but I disagree
def string_search(grid, s):
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == s[0] and is_string(grid, s, 1, r, c, set()):
        return True 
  
  return False

def is_string(grid, s, i, r, c, visited):
  if i == len(s):
    return True
  if not in_bounds(grid, r, c):
    return False
  if (r, c) in visited:
    return False
    
  visited.add((r, c))
  deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  for dy, dx in deltas:
    new_y, new_x = r + dy, c + dx
    if in_bounds(grid, new_y, new_x) and grid[new_y][new_x] == s[i]:
      if is_string(grid, s, i + 1, new_y, new_x, visited):
        return True
    
  return False

def in_bounds(grid, r, c):
  if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]):
    return False
  return True

# [[[[[[[[[[[[[[[[[[[[[[[[[ #99 token replace ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, token_replace, that takes in a dictionary of tokens and a 
# string. The function should return a new string where tokens are replaced.
# Tokens are enclosed in a pair of '$'. You can assume that the input string is 
# properly formatted. Tokens should be replaced from left to right in the string
# (see test_05).
#
# test_00:
# tokens = {
#   '$LOCATION$': 'park',
#   '$ANIMAL$': 'dog',
# }
# token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens) 
# # -> 'Walk the dog in the park!'
# test_01:
# tokens = {
#   '$ADJECTIVE$': 'quick',
#   '$VERB$': 'hopped',
#   '$DIRECTION$': 'North'
# }
# token_replace('the $ADJECTIVE$ fox $VERB$ $ADJECTIVE$ly $DIRECTION$ward', tokens) 
# # -> 'the quick fox hopped quickly Northward'
# test_02:
# tokens = {
#   '$greeting$': 'hey programmer',
# }
# token_replace('his greeting is always $greeting$.', tokens) 
# # -> 'his greeting is always hey programmer.'
# test_03:
# tokens = {
#   '$A$': 'lions',
#   '$B$': 'tigers',
#   '$C$': 'bears',
# }
# token_replace('$A$$B$$C$, oh my.', tokens) 
# # -> 'lionstigersbears, oh my.'
# test_04:
# tokens = {
#   '$A$': 'lions',
#   '$B$': 'tigers',
#   '$C$': 'bears',
# }
# token_replace('$B$', tokens) 
# # -> 'tigers'
# test_05:
# tokens = {
#   '$second$': 'beta',
#   '$first$': 'alpha',
#   '$third$': 'gamma',
# }
# token_replace('$first$second$third$', tokens) 
# # -> 'alphasecondgamma'

# ========================= Two Pointers =========================
# Time: O(n), Space: O(n) 
def token_replace(s, tokens):
  replaced = ''
  i = 0
  j = 0
  while i < len(s):
    if s[i] == '$':
      j = i + 1
      while s[j] != '$':
        j += 1
      token = s[i: j + 1]
      replaced += tokens[token]
      i = j
    else:
      replaced += s[i]
    i += 1

  return replaced

# [[[[[[[[[[[[[[[[[[[[[[[[[ #100 token transform ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, token_transform, that takes in a dictionary of tokens and a 
# string. In the dictionary, the replacement values for a token may reference 
# other tokens. The function should return a new string where tokens are replaced 
# with their fully evaluated string values.
# Tokens are enclosed in a pair of '$'.
# You may assume that their are no circular token dependencies.
#
# test_00:
# tokens = {
#   '$LOCATION$': '$ANIMAL$ park',
#   '$ANIMAL$': 'dog',
# }
# token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
# # -> 'Walk the dog in the dog park!'
# test_01:
# tokens = {
#   '$ADJECTIVE_1$': "quick",
#   '$ADJECTIVE_2$': "eager",
#   '$ADVERBS$': "$ADJECTIVE_1$ly and $ADJECTIVE_2$ly",
#   '$VERB$': "hopped $DIRECTION$",
#   '$DIRECTION$': "North",
# }
# token_transform("the $ADJECTIVE_1$ fox $ADVERBS$ $VERB$ward", tokens)
# # -> 'the quick fox quickly and eagerly hopped Northward'
# test_02:
# tokens = {
#   '$B$': "epicly $C$",
#   '$A$': "pretty $B$ problem $D$",
#   '$D$': "we have",
#   '$C$': "clever",
# }
# token_transform("What a $A$ here!", tokens)
# # -> 'What a pretty epicly clever problem we have here!'
# test_03:
# tokens = {
#   '$1$': "a$2$",
#   '$2$': "b$3$",
#   '$3$': "c$4$",
#   '$4$': "d$5$",
#   '$5$': "e$6$",
#   '$6$': "f!",
# }
# token_transform("$1$ $1$ $1$ $1$ $1$ $1$ $4$ $4$", tokens)
# # -> 'abcdef! abcdef! abcdef! abcdef! abcdef! abcdef! def! def!'
# test_04:
# tokens = {
#   '$0$': "$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$",
#   '$1$': "$2$$2$$2$$2$$2$$2$$2$$2$$2$",
#   '$2$': "$3$$3$$3$$3$$3$$3$$3$",
#   '$3$': "$4$$4$$4$$4$$4$$4$",
#   '$4$': "$5$$5$$5$$5$$5$",
#   '$5$': "$6$$6$$6$$6$",
#   '$6$': "$7$$7$$7$",
#   '$7$': "$8$$8$",
#   '$8$': "",
# }
# token_transform("z$0$z$0$z$0$z$0$z$0$z$0$z", tokens)
# # -> 'zzzzzzz'

# ========================= Recursive Two Pointers =========================
# n: length of string, m: num tokens
# Time: O(n), Space: O(n) 
def token_transform(s, tokens):
  transformed = ''
  i = 0
  j = 0
  while i < len(s):
    if s[i] == '$':
      j = i + 1
      while s[j] != '$':
        j += 1
      key = s[i:j + 1]
      final_value = token_transform(tokens[key], tokens)
      transformed += final_value
      tokens[key] = final_value
      i = j
    else:
      transformed += s[i]
    i += 1

  return transformed