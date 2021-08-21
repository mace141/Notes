# [[[[[[[[[[[[[[[[[[[[[[[[[ #1 max value ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, max_value, that takes in list of numbers as an argument. 
# The function should return the largest number in the list.
# Solve this without using any built-in list methods.
# You can assume that the list is non-empty.
#
# test_00:
# max_value([4, 7, 2, 8, 10, 9]); # -> 10
# test_01:
# max_value([10, 5, 40, 40.3]); # -> 40.3
# test_02:
# max_value([-5, -2, -1, -11]); # -> -1
# test_03:
# max_value([42]); # -> 42
# test_04:
# max_value([1000, 8]); # -> 1000
# test_05:
# max_value([1000, 8, 9000]); # -> 9000

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
# is_prime(2); # -> true
# test_01:
# is_prime(3); # -> true
# test_02:
# is_prime(4); # -> false
# test_03:
# is_prime(5); # -> true
# test_04:
# is_prime(6); # -> false
# test_05:
# is_prime(7); # -> true
# test_06:
# is_prime(8); # -> false
# test_07:
# is_prime(25); # -> false
# test_08:
# is_prime(31); # -> true
# test_09:
# is_prime(2017); # -> true
# test_10:
# is_prime(2048); # -> false
# test_11:
# is_prime(1); # -> false

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
#
# <number><char>
#
# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 
# 'char' of a group is repeated 'number' times concecutively. You may assume that 
# the input string is well-formed according to the previously mentioned pattern.
#
# test_00:
# uncompress("2c3a1t"); # -> 'ccaaat'
# test_01:
# uncompress("4s2b"); # -> 'ssssbb'
# test_02:
# uncompress("2p1o5p"); # -> 'ppoppppp'
# test_03:
# uncompress("3n12e2z"); # -> 'nnneeeeeeeeeeeezz'

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
#
# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.
#
# test_00:
# compress('ccaaatsss'); # -> '2c3at3s'
# test_01:
# compress('ssssbbz'); # -> '4s2bz'
# test_02:
# compress('ppoppppp'); # -> '2po5p'
# test_03:
# compress('nnneeeeeeeeeeeezz'); # -> '3n12e2z'

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
# anagrams('restful', 'fluster'); # -> true
# test_01:
# anagrams('cats', 'tocs'); # -> false
# test_02:
# anagrams('monkeyswrite', 'newyorktimes'); # -> true
# test_03:
# anagrams('paper', 'reapa'); # -> false
# test_04:
# anagrams('elbow', 'below'); # -> true
# test_05:
# anagrams('tax', 'taxi'); # -> false

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
# most_frequent_char('bookeeper'); # -> 'e'
# test_01:
# most_frequent_char('david'); # -> 'd'
# test_02:
# most_frequent_char('abby'); # -> 'b'
# test_03:
# most_frequent_char('mississippi'); # -> 'i'
# test_04:
# most_frequent_char('potato'); # -> 'o'
# test_05:
# most_frequent_char('eleventennine'); # -> 'e'

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
# a = [];
# b = [];
# for (let i = 0; i < 50000; i += 1) {
#   a.push(i);
#   b.push(i);
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
# five_sort([12, 5, 1, 5, 12, 7]);
# -> [12, 7, 1, 12, 5, 5] 
# test_01
# five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]);
# -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 
# test_02
# five_sort([5, 5, 5, 1, 1, 1, 4]);
# -> [4, 1, 1, 1, 5, 5, 5] 
# test_03
# five_sort([5, 5, 6, 5, 5, 5, 5]);
# -> [6, 5, 5, 5, 5, 5, 5] 
# test_04
# five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]);
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
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# a.next = b;
# b.next = c;
# c.next = d;
# a -> b -> c -> d
# linked_list_values(a); # -> [ 'a', 'b', 'c', 'd' ]
# test_01:
# x = new Node("x");
# y = new Node("y");
# x.next = y;
# x -> y
# linked_list_values(x); # -> [ 'x', 'y' ]
# test_02:
# q = new Node("q");
# q
# linked_list_values(q); # -> [ 'q' ]
# test_03:
# linked_list_values(None); # -> [ ]

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
# a = new Node(2);
# b = new Node(8);
# c = new Node(3);
# d = new Node(-1);
# e = new Node(7);
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# 2 -> 8 -> 3 -> -1 -> 7
# sum_list(a); # 19
# test_01:
# x = new Node(38);
# y = new Node(4);
# x.next = y;
# 38 -> 4
# sum_list(x); # 42
# test_02:
# z = new Node(100);
# 100
# sum_list(z); # 100
# test_03:
# sum_list(None); # 0

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
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# a.next = b;
# b.next = c;
# c.next = d;
# a -> b -> c -> d
# linked_list_find(a, "c"); # true
# test_01:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# a.next = b;
# b.next = c;
# c.next = d;
# a -> b -> c -> d
# linked_list_find(a, "d"); # true
# test_02:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# a.next = b;
# b.next = c;
# c.next = d;
# a -> b -> c -> d
# linked_list_find(a, "q"); # false
# test_03:
# node_1 = new Node("jason");
# node2 = new Node("leneli");
# node_1.next = node2;
# jason -> leneli
# linked_list_find(node_1, "jason"); # true
# test_04:
# node_1 = new Node(42);
# 42
# linked_list_find(node_1, 42); # true
# test_05:
# node_1 = new Node(42);
# 42
# linked_list_find(node_1, 100); # false

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
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# a.next = b;
# b.next = c;
# c.next = d;
# a -> b -> c -> d
# get_node_value(a, 2); # 'c'
# test_01:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# a.next = b;
# b.next = c;
# c.next = d;
# a -> b -> c -> d
# get_node_value(a, 3); # 'd'
# test_02:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# a.next = b;
# b.next = c;
# c.next = d;
# a -> b -> c -> d
# get_node_value(a, 7); # None
# test_03:
# node_1 = new Node("banana");
# node2 = new Node("mango");
# node_1.next = node2;
# banana -> mango
# get_node_value(node_1, 0); # 'banana'
# test_04:
# node_1 = new Node("banana");
# node2 = new Node("mango");
# node_1.next = node2;
# banana -> mango
# get_node_value(node_1, 1); # 'mango'

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
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# e.next = f;
# a -> b -> c -> d -> e -> f
# reverse_list(a); # f -> e -> d -> c -> b -> a
# test_01:
# x = new Node("x");
# y = new Node("y");
# x.next = y;
# x -> y
# reverse_list(x); # y -> x
# test_02:
# p = new Node("p");
# p
# reverse_list(p); # p

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
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# a.next = b;
# b.next = c;
# a -> b -> c
# x = new Node("x");
# y = new Node("y");
# z = new Node("z");
# x.next = y;
# y.next = z;
# x -> y -> z
# zipper_lists(a, x);
# a -> x -> b -> y -> c -> z
# test_01:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# e.next = f;
# a -> b -> c -> d -> e -> f
# x = new Node("x");
# y = new Node("y");
# z = new Node("z");
# x.next = y;
# y.next = z;
# x -> y -> z
# zipper_lists(a, x);
# a -> x -> b -> y -> c -> z -> d -> e -> f
# test_02:
# s = new Node("s");
# t = new Node("t");
# s.next = t;
# s -> t
# one = new Node(1);
# two = new Node(2);
# three = new Node(3);
# four = new Node(4);
# one.next = two;
# two.next = three;
# three.next = four;
# 1 -> 2 -> 3 -> 4
# zipper_lists(s, one);
# s -> 1 -> t -> 2 -> 3 -> 4
# test_03:
# w = new Node("w");
# w
# one = new Node(1);
# two = new Node(2);
# three = new Node(3);
# one.next = two;
# two.next = three;
# 1 -> 2 -> 3 
# zipper_lists(w, one);
# w -> 1 -> 2 -> 3
# test_04:
# one = new Node(1);
# two = new Node(2);
# three = new Node(3);
# one.next = two;
# two.next = three;
# 1 -> 2 -> 3 
# w = new Node("w");
# w
# zipper_lists(one, w);
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
# a = new Node(5);
# b = new Node(7);
# c = new Node(10);
# d = new Node(12);
# e = new Node(20);
# f = new Node(28);
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# e.next = f;
# 5 -> 7 -> 10 -> 12 -> 20 -> 28
# q = new Node(6);
# r = new Node(8);
# s = new Node(9);
# t = new Node(25);
# q.next = r;
# r.next = s;
# s.next = t;
# 6 -> 8 -> 9 -> 25
# merge_lists(a, q);
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 
# test_01:
# a = new Node(5);
# b = new Node(7);
# c = new Node(10);
# d = new Node(12);
# e = new Node(20);
# f = new Node(28);
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# e.next = f;
# 5 -> 7 -> 10 -> 12 -> 20 -> 28
# q = new Node(1);
# r = new Node(8);
# s = new Node(9);
# t = new Node(10);
# q.next = r;
# r.next = s;
# s.next = t;
# 1 -> 8 -> 9 -> 10
# merge_lists(a, q);
# 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28 
# test_02:
# h = new Node(30);
# 30
# p = new Node(15);
# q = new Node(67);
# p.next = q;
# 15 -> 67
# merge_lists(h, p);
# 15 -> 30 -> 67

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
# a = new Node(7);
# b = new Node(7);
# c = new Node(7);
# a.next = b;
# b.next = c;
# 7 -> 7 -> 7
# is_univalue_list(a); # true
# test_01:
# a = new Node(7);
# b = new Node(7);
# c = new Node(4);
# a.next = b;
# b.next = c;
# 7 -> 7 -> 4
# is_univalue_list(a); # false
# test_02:
# u = new Node(2);
# v = new Node(2);
# w = new Node(2);
# x = new Node(2);
# y = new Node(2);
# u.next = v;
# v.next = w;
# w.next = x;
# x.next = y;
# 2 -> 2 -> 2 -> 2 -> 2
# is_univalue_list(u); # true
# test_03:
# u = new Node(2);
# v = new Node(2);
# w = new Node(3);
# x = new Node(3);
# y = new Node(2);
# u.next = v;
# v.next = w;
# w.next = x;
# x.next = y;
# 2 -> 2 -> 3 -> 3 -> 2
# is_univalue_list(u); # false
# test_04:
# z = new Node('z');
# z
# is_univalue_list(z); # true

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
# test_00:
# a = new Node(5);
# b = new Node(5);
# c = new Node(7);
# d = new Node(7);
# e = new Node(7);
# f = new Node(6);
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# e.next = f;
# 5 -> 5 -> 7 -> 7 -> 7 -> 6
# longest_streak(a); # 3
# test_01:
# a = new Node(3);
# b = new Node(3);
# c = new Node(3);
# d = new Node(3);
# e = new Node(9);
# f = new Node(9);
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# e.next = f;
# 3 -> 3 -> 3 -> 3 -> 9 -> 9
# longest_streak(a); # 4
# test_02:
# a = new Node(9);
# b = new Node(9);
# c = new Node(1);
# d = new Node(9);
# e = new Node(9);
# f = new Node(9);
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# e.next = f;
# 9 -> 9 -> 1 -> 9 -> 9 -> 9
# longest_streak(a); # 3
# test_03:
# a = new Node(5);
# b = new Node(5);
# a.next = b;
# 5 -> 5
# longest_streak(a); # 2
# test_04:
# a = new Node(4);
# 4
# longest_streak(a); # 1
# test_05:
# longest_streak(None); # 0

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
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# e.next = f;
# a -> b -> c -> d -> e -> f
# remove_node(a, "c");
# a -> b -> d -> e -> f
# test_01:
# x = new Node("x");
# y = new Node("y");
# z = new Node("z");
# x.next = y;
# y.next = z;
# x -> y -> z
# remove_node(x, "z");
# x -> y
# test_02:
# q = new Node("q");
# r = new Node("r");
# s = new Node("s");
# q.next = r;
# r.next = s;
# q -> r -> s
# remove_node(q, "q");
# r -> s
# test_03:
# node_1 = new Node("h");
# node2 = new Node("i");
# node3 = new Node("j");
# node4 = new Node("i");
# node_1.next = node2;
# node2.next = node3;
# node3.next = node4;
# h -> i -> j -> i
# remove_node(node_1, "i");
# h -> j -> i
# test_04:
# t = new Node("t");
# t
# remove_node(t, "t");
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
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# a.next = b;
# b.next = c;
# c.next = d;
# a -> b -> c -> d
# insert_node(a, 'x', 2);
# a -> b -> x -> c -> d
# test_01:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# a.next = b;
# b.next = c;
# c.next = d;
# a -> b -> c -> d
# insert_node(a, 'v', 3);
# a -> b -> c -> v -> d
# test_02:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# a.next = b;
# b.next = c;
# c.next = d;
# a -> b -> c -> d
# insert_node(a, 'm', 4);
# a -> b -> c -> d -> m
# test_03:
# a = new Node("a");
# b = new Node("b");
# a.next = b;
# a -> b
# insert_node(a, 'z', 0);
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

  head.next = insert_node(head, value, index, count + 1)
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
# create_linked_list(["h", "e", "y"]);
# h -> e -> y
# test_01:
# create_linked_list([1, 7, 1, 8]);
# 1 -> 7 -> 1 -> 8
# test_02:
# create_linked_list(["a"]);
# a
# test_03:
# create_linked_list([]);
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
# The nodes in the input lists are reversed; this means that the least significant 
# digit of the number is the head. The function should return the head of a new 
# linked listed representing the sum of the input lists. The output list should 
# have it's digits reversed as well.
#
# Say we wanted to compute 621 + 354 normally. The sum is 975:
#
#    621
#  + 354
#  -----
#    975
#
# Then, the reversed linked list format of this problem would appear as:
#
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
# a1 = new Node(1);
# a2 = new Node(2);
# a3 = new Node(6);
# a1.next = a2;
# a2.next = a3;
# 1 -> 2 -> 6
# b1 = new Node(4);
# b2 = new Node(5);
# b3 = new Node(3);
# b1.next = b2;
# b2.next = b3;
# 4 -> 5 -> 3
# addLists(a1, b1);
# 5 -> 7 -> 9
# test_01:
#  7541
# +  32
# -----
#  7573
# a1 = new Node(1);
# a2 = new Node(4);
# a3 = new Node(5);
# a4 = new Node(7);
# a1.next = a2;
# a2.next = a3;
# a3.next = a4;
# 1 -> 4 -> 5 -> 7
# b1 = new Node(2);
# b2 = new Node(3);
# b1.next = b2;
# 2 -> 3 
# addLists(a1, b1);
# 3 -> 7 -> 5 -> 7
# test_02:
#   39
# + 47
# ----
#   86
# a1 = new Node(9);
# a2 = new Node(3);
# a1.next = a2;
# 9 -> 3
# b1 = new Node(7);
# b2 = new Node(4);
# b1.next = b2;
# 7 -> 4
# addLists(a1, b1);
# 6 -> 8
# test_03:
#   89
# + 47
# ----
#  136
# a1 = new Node(9);
# a2 = new Node(8);
# a1.next = a2;
# 9 -> 8
# b1 = new Node(7);
# b2 = new Node(4);
# b1.next = b2;
# 7 -> 4
# addLists(a1, b1);
# 6 -> 3 -> 1
# test_04:
#   999
#  +  6
#  ----
#  1005
# a1 = new Node(9);
# a2 = new Node(9);
# a3 = new Node(9);
# a1.next = a2;
# a2.next = a3;
# 9 -> 9 -> 9
# b1 = new Node(6);
# 6
# addLists(a1, b1);
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
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# f = new Node('f');
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# depth_first_values(a); 
#    -> ['a', 'b', 'd', 'e', 'c', 'f']
# test_01:
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# f = new Node('f');
# g = new Node('g');
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g
# depth_first_values(a); 
#    -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
# test_02:
# a = new Node('a');
#      a
# depth_first_values(a); 
#    -> ['a']
# test_03:
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# a.right = b;
# b.left = c;
# c.right = d;
# d.right = e;
#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e
# depth_first_values(a); 
#    -> ['a', 'b', 'c', 'd', 'e']
# test_04:
# howHigh(None); 
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
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# f = new Node('f');
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# breadth_first_values(a); 
#    -> ['a', 'b', 'c', 'd', 'e', 'f']
# test_01:
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# f = new Node('f');
# g = new Node('g');
# h = new Node('h');
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# f.right = h;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
# breadth_first_values(a); 
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# test_02:
# a = new Node('a');
#      a
# breadth_first_values(a); 
#    -> ['a']
# test_03:
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# x = new Node('x');
# a.right = b;
# b.left = c;
# c.left = x;
# c.right = d;
# d.right = e;
#      a
#       \
#        b
#       /
#      c
#    /  \
#   x    d
#         \
#          e
# breadth_first_values(a); 
#    -> ['a', 'b', 'c', 'x', 'd', 'e']
# test_04:
# howHigh(None); 
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
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# tree_includes(a, "e"); # -> true
# test_01:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# tree_includes(a, "a"); # -> true
# test_02:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# tree_includes(a, "n"); # -> false
# test_03:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# g = new Node("g");
# h = new Node("h");
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# f.right = h;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
# tree_includes(a, "f"); # -> true
# test_04:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# g = new Node("g");
# h = new Node("h");
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# f.right = h;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
# tree_includes(a, "p"); # -> false
# test_05:
# tree_includes(None, "b"); # -> false

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
# a = new Node(3);
# b = new Node(11);
# c = new Node(4);
# d = new Node(4);
# e = new Node(-2);
# f = new Node(1);
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
# treeSum(a); # -> 21
# test_01:
# a = new Node(1);
# b = new Node(6);
# c = new Node(0);
# d = new Node(3);
# e = new Node(-6);
# f = new Node(2);
# g = new Node(2);
# h = new Node(2);
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# f.right = h;
#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2
# treeSum(a); # -> 10
# test_02:
# treeSum(None); # -> 0

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
# a = new Node(3);
# b = new Node(11);
# c = new Node(4);
# d = new Node(4);
# e = new Node(-2);
# f = new Node(1);
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
# treeMinValue(a); # -> -2
# test_01:
# a = new Node(5);
# b = new Node(11);
# c = new Node(3);
# d = new Node(4);
# e = new Node(14);
# f = new Node(12);
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#       5
#    /    \
#   11     3
#  / \      \
# 4   15     12
# treeMinValue(a); # -> 3
# test_02:
# a = new Node(-1);
# b = new Node(-6);
# c = new Node(-5);
# d = new Node(-3);
# e = new Node(-4);
# f = new Node(-13);
# g = new Node(-2);
# h = new Node(-2);
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# f.right = h;
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     /       \
#    -2       -2
# tree_min_value(a); # -> -13
# test_03:
# a = new Node(42);
#        42
# tree_min_value(a); # -> 42

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
# a = new Node(3);
# b = new Node(11);
# c = new Node(4);
# d = new Node(4);
# e = new Node(-2);
# f = new Node(1);
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#      3
#    /   \
#   11    4
#  / \     \
# 4   -2    1
# max_path_sum(a); # -> 18
# test_01:
# a = new Node(5);
# b = new Node(11);
# c = new Node(54);
# d = new Node(20);
# e = new Node(15);
# f = new Node(1);
# g = new Node(3);
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# e.left = f;
# e.right = g;
#       5
#     /   \
#    11   54
#  /   \
# 20   15
#      / \
#     1  3
# max_path_sum(a); # -> 59
# test_02:
# a = new Node(-1);
# b = new Node(-6);
# c = new Node(-5);
# d = new Node(-3);
# e = new Node(0);
# f = new Node(-13);
# g = new Node(-1);
# h = new Node(-2);
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# f.right = h;
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   0    -13
#     /       \
#    -1       -2
# max_path_sum(a); # -> -8
# test_03:
# a = new Node(42);
#        42
# max_path_sum(a); # -> 42

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
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# path_finder(a, 'e'); # -> [ 'a', 'b', 'e' ]
# test_01:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
# path_finder(a, 'p'); # -> None
# test_02:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# g = new Node("g");
# h = new Node("h");
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# f.right = h;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
# path_finder(a, "c"); # -> ['a', 'c']
# test_03:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# g = new Node("g");
# h = new Node("h");
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# f.right = h;
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
# path_finder(a, "h"); # -> ['a', 'c', 'f', 'h']
# test_04:
# x = new Node("x");
#      x
# path_finder(x, "x"); # -> ['x']
# test_05:
# path_finder(None, "x"); # -> None
# test_06:
# root = new Node(0);
# let curr = root;
# for (let i = 1; i <= 6000; i += 1) {
#   curr.right = new Node(i);
#   curr = curr.right;
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
# path_finder(root, 3451); # -> [0, 1, 2, 3, ..., 3450, 3451]

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
# a = new Node(12);
# b = new Node(6);
# c = new Node(6);
# d = new Node(4);
# e = new Node(6);
# f = new Node(12);
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#     12
#    /  \
#   6    6
#  / \    \
# 4   6    12
# tree_value_count(a,  6); # -> 3
# test_01:
# a = new Node(12);
# b = new Node(6);
# c = new Node(6);
# d = new Node(4);
# e = new Node(6);
# f = new Node(12);
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#     12
#    /  \
#   6    6
#  / \    \
# 4   6    12
# tree_value_count(a,  12); # -> 2
# test_02:
# a = new Node(7);
# b = new Node(5);
# c = new Node(1);
# d = new Node(1);
# e = new Node(8);
# f = new Node(7);
# g = new Node(1);
# h = new Node(1);
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# f.right = h;
#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1
# tree_value_count(a, 1); # -> 4
# test_03:
# a = new Node(7);
# b = new Node(5);
# c = new Node(1);
# d = new Node(1);
# e = new Node(8);
# f = new Node(7);
# g = new Node(1);
# h = new Node(1);
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# f.right = h;
#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1
# tree_value_count(a, 9); # -> 0
# test_04:
# tree_value_count(None, 42); # -> 0

def tree_value_count(root, target):
  if root is None:
    return 0
  
  count = 0
  if root.val == target:
    count += 1
  
  return count + tree_value_count(root.left) + tree_value_count(root.right)

# [[[[[[[[[[[[[[[[[[[[[[[[[ #32 how high ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, howHigh, that takes in the root of a binary tree. The 
# function should return a number representing the height of the tree.
#
# The height of a binary tree is defined as the maximal number of edges from 
# the root node to any leaf node.
#
# If the tree is empty, return -1.
#
# test_00:
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# f = new Node('f');
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#
# howHigh(a); # -> 2
#
# test_01:
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# f = new Node('f');
# g = new Node('g');
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g
#
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g
#
# howHigh(a); # -> 3
#
# test_02:
# a = new Node('a');
# c = new Node('c');
#
# a.right = c;
#
#      a
#       \
#        c
#
# howHigh(a); # -> 1
#
# test_03:
# a = new Node('a');
#
#      a
#
# howHigh(a); # -> 0


# [[[[[[[[[[[[[[[[[[[[[[[[[ #33 bottom right value ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, bottomRightValue, that takes in the root of a binary tree. 
# The function should return the right-most value in the bottom-most level of 
# the tree.
#
# You may assume that the input tree is non-empty.
#
# test_00:
# a = new Node(3);
# b = new Node(11);
# c = new Node(10);
# d = new Node(4);
# e = new Node(-2);
# f = new Node(1);
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#
#       3
#    /    \
#   11     10
#  / \      \
# 4   -2     1
#
# bottomRightValue(a); # -> 1
#
# test_01:
# a = new Node(-1);
# b = new Node(-6);
# c = new Node(-5);
# d = new Node(-3);
# e = new Node(-4);
# f = new Node(-13);
# g = new Node(-2);
# h = new Node(6);
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# e.right = h;
#
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \       
#    -2  6
#
# bottomRightValue(a); # -> 6
#
# test_02:
# a = new Node(-1);
# b = new Node(-6);
# c = new Node(-5);
# d = new Node(-3);
# e = new Node(-4);
# f = new Node(-13);
# g = new Node(-2);
# h = new Node(6);
# i = new Node(7);
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# e.right = h;
# f.left = i;
#
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \    /   
#    -2  6  7 
#
# bottomRightValue(a); # -> 7
#
# test_03
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# f = new Node('f');
#
# a.left = b;
# a.right = c;
# b.right = d;
# d.left = e;
# e.right = f;
#
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
# bottomRightValue(a); # -> 'f'
#
# test_04
# a = new Node(42);
#
#      42
#
# bottomRightValue(a); # -> 42


# [[[[[[[[[[[[[[[[[[[[[[[[[ #34 all tree paths ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, allTreePaths, that takes in the root of a binary tree. The
# function should return a 2-Dimensional list where each sublist represents a
# root-to-leaf path in the tree.
#
# The order within an individual path must start at the root and end at the leaf,
# but the relative order of among paths in the outer list does not matter.
#
# You may assume that the input tree is non-empty.
#
# test_00:
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# f = new Node('f');
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#
# allTreePaths(a); # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e' ], 
#   [ 'a', 'c', 'f' ] 
# ] 
#
# test_01:
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# f = new Node('f');
# g = new Node('g');
# h = new Node('h');
# i = new Node('i');
#
# a.l#eft = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# e.right = h;
# f.left = i;
#
#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /   
#     g  h   i 
#
# allTreePaths(a); # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e', 'g' ], 
#   [ 'a', 'b', 'e', 'h' ], 
#   [ 'a', 'c', 'f', 'i' ] 
# ] 
#
# test_02:
# q = new Node('q');
# r = new Node('r');
# s = new Node('s');
# t = new Node('t');
# u = new Node('u');
# v = new Node('v');
#
# q.left = r;
# q.right = s;
# r.right = t;
# t.left = u;
# u.right = v;
#
#      q
#    /   \ 
#   r     s
#    \
#     t
#    /
#   u
#  /
# v
#
# allTreePaths(q); # ->
# [ 
#   [ 'q', 'r', 't', 'u', 'v' ], 
#   [ 'q', 's' ] 
# ] 
#
# test_03:
# z = new Node('z');
#
#      z
#
# console.log(allTreePaths(z)); # -> 
# [
#   ['z']
# ]


# [[[[[[[[[[[[[[[[[[[[[[[[[ #35 tree levels ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, treeLevels, that takes in the root of a binary tree. The 
# function should return a 2-Dimensional list where each sublist represents a
# level of the tree.
#
# test_00:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#
# treeLevels(a); # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]
#
# test_01:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# g = new Node("g");
# h = new Node("h");
# i = new Node("i");
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# e.right = h;
# f.left = i;
#
#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /
#     g  h   i
#
# treeLevels(a); # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f'],
#   ['g', 'h', 'i']
# ]
#
# test_02:
# q = new Node("q");
# r = new Node("r");
# s = new Node("s");
# t = new Node("t");
# u = new Node("u");
# v = new Node("v");
#
# q.left = r;
# q.right = s;
# r.right = t;
# t.left = u;
# u.right = v;
#
#      q
#    /   \
#   r     s
#    \
#     t
#    /
#   u
#  /
# v
#
# treeLevels(q); #->
# [
#   ['q'],
#   ['r', 's'],
#   ['t'],
#   ['u'],
#   ['v']
# ]
#
#
# test_03:
# treeLevels(None); # -> []



# [[[[[[[[[[[[[[[[[[[[[[[[[ #36 level averages ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, levelAverages, that takes in the root of a binary tree that
# contains number values. The function should return an list containing the 
# average value of each level.
#
# test_00:
# a = new Node(3);
# b = new Node(11);
# c = new Node(4);
# d = new Node(4);
# e = new Node(-2);
# f = new Node(1);
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#
#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
#
# levelAverages(a); # -> [ 3, 7.5, 1 ] 
#
# test_01:
# a = new Node(5);
# b = new Node(11);
# c = new Node(54);
# d = new Node(20);
# e = new Node(15);
# f = new Node(1);
# g = new Node(3);
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# e.left = f;
# e.right = g;
#
#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3
#
# levelAverages(a); # -> [ 5, 32.5, 17.5, 2 ] 
#
# test_02:
# a = new Node(-1);
# b = new Node(-6);
# c = new Node(-5);
# d = new Node(-3);
# e = new Node(0);
# f = new Node(45);
# g = new Node(-1);
# h = new Node(-2);
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# f.right = h;
#
#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   0     45
#     /       \
#    -1       -2
#
# levelAverages(a); # -> [ -1, -5.5, 14, -1.5 ]
#
# test_03:
# q = new Node(13);
# r = new Node(4);
# s = new Node(2);
# t = new Node(9);
# u = new Node(2);
# v = new Node(42);
#
# q.left = r;
# q.right = s;
# r.right = t;
# t.left = u;
# u.right = v;
#
#        13
#      /   \
#     4     2
#      \
#       9
#      /
#     2
#    /
#   42
#
# levelAverages(q); # -> [ 13, 3, 9, 2, 42 ]
#
# test_04:
# levelAverages(None); # -> [ ]


# [[[[[[[[[[[[[[[[[[[[[[[[[ #37 leaf list ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, leafList, that takes in the root of a binary tree and 
# returns an list containing the values of all leaf nodes in left-to-right order.
#
# test_00:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
#
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#
# leafList(a); # -> [ 'd', 'e', 'f' ] 
#
# test_01:
# a = new Node("a");
# b = new Node("b");
# c = new Node("c");
# d = new Node("d");
# e = new Node("e");
# f = new Node("f");
# g = new Node("g");
# h = new Node("h");
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;
# e.left = g;
# f.right = h;
#
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h
#
# leafList(a); # -> [ 'd', 'g', 'h' ]
#
# test_02:
# a = new Node(5);
# b = new Node(11);
# c = new Node(54);
# d = new Node(20);
# e = new Node(15);
# f = new Node(1);
# g = new Node(3);
#
# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# e.left = f;
# e.right = g;
#
#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3
#
# leafList(a); # -> [ 20, 1, 3, 54 ]
#
# test_03:
# x = new Node('x');
#
#      x
#
# leafList(x); # -> [ 'x' ]
#
# test_04:
# leafList(None); # -> [ ]


# [[[[[[[[[[[[[[[[[[[[[[[[[ #38 has path ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, hasPath, that takes in an object representing the adjacency
# list of a directed acyclic graph and two nodes (src, dst). The function should
# return a boolean indicating whether or not there exists a directed path between
# the source and destination nodes.
#
# test_00:
# graph = {
#   f: ['g', 'i'],
#   g: ['h'],
#   h: [],
#   i: ['g', 'k'],
#   j: ['i'],
#   k: []
# };
#
# hasPath(graph, 'f', 'k'); # true
#
# test_01:
# graph = {
#   f: ['g', 'i'],
#   g: ['h'],
#   h: [],
#   i: ['g', 'k'],
#   j: ['i'],
#   k: []
# };
#
# hasPath(graph, 'f', 'j'); # false
#
# test_02:
# graph = {
#   f: ['g', 'i'],
#   g: ['h'],
#   h: [],
#   i: ['g', 'k'],
#   j: ['i'],
#   k: []
# };
#
# hasPath(graph, 'i', 'h'); # true
#
# test_03:
# graph = {
#   v: ['x', 'w'],
#   w: [],
#   x: [],
#   y: ['z'],
#   z: [],  
# };
#
# hasPath(graph, 'v', 'w'); # true
#
# test_04:
# graph = {
#   v: ['x', 'w'],
#   w: [],
#   x: [],
#   y: ['z'],
#   z: [],  
# };
#
# hasPath(graph, 'v', 'z'); # false


# [[[[[[[[[[[[[[[[[[[[[[[[[ #39 undirected path ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, undirectedPath, that takes in an list of edges for an 
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
# ];
#
# undirectedPath(edges, 'j', 'm'); # -> true
#
# test_01:
# edges = [
#   ['i', 'j'],
#   ['k', 'i'],
#   ['m', 'k'],
#   ['k', 'l'],
#   ['o', 'n']
# ];
#
# undirectedPath(edges, 'm', 'j'); # -> true
#
# test_02:
# edges = [
#   ['i', 'j'],
#   ['k', 'i'],
#   ['m', 'k'],
#   ['k', 'l'],
#   ['o', 'n']
# ];
#
# undirectedPath(edges, 'l', 'j'); # -> true
#
# test_03:
# edges = [
#   ['i', 'j'],
#   ['k', 'i'],
#   ['m', 'k'],
#   ['k', 'l'],
#   ['o', 'n']
# ];
#
# undirectedPath(edges, 'k', 'o'); # -> false
# test_04:
# edges = [
#   ['i', 'j'],
#   ['k', 'i'],
#   ['m', 'k'],
#   ['k', 'l'],
#   ['o', 'n']
# ];
#
# undirectedPath(edges, 'i', 'o'); # -> false
#
# test_05:
# edges = [
#   ['b', 'a'],
#   ['c', 'a'],
#   ['b', 'c'],
#   ['q', 'r'],
#   ['q', 's'],
#   ['q', 'u'],
#   ['q', 't'],
# ];
#
# undirectedPath(edges, 'a', 'b'); # -> true
#
# test_06:
# edges = [
#   ['b', 'a'],
#   ['c', 'a'],
#   ['b', 'c'],
#   ['q', 'r'],
#   ['q', 's'],
#   ['q', 'u'],
#   ['q', 't'],
# ];
#
# undirectedPath(edges, 'a', 'c'); # -> true
#
# test_07:
# edges = [
#   ['b', 'a'],
#   ['c', 'a'],
#   ['b', 'c'],
#   ['q', 'r'],
#   ['q', 's'],
#   ['q', 'u'],
#   ['q', 't'],
# ];
#
# undirectedPath(edges, 'r', 't'); # -> true
#
# test_08:
# edges = [
#   ['b', 'a'],
#   ['c', 'a'],
#   ['b', 'c'],
#   ['q', 'r'],
#   ['q', 's'],
#   ['q', 'u'],
#   ['q', 't'],
# ];
#
# undirectedPath(edges, 'r', 'b'); # -> false


# [[[[[[[[[[[[[[[[[[[[[[[[[ #40 connected components count ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, connectedComponentsCount, that takes in the adjacency list 
# of an undirected graph. The function should return the number of connected 
# components within the graph.
#
# test_00:
# connectedComponentsCount({
#   0: [8, 1, 5],
#   1: [0],
#   5: [0, 8],
#   8: [0, 5],
#   2: [3, 4],
#   3: [2, 4],
#   4: [3, 2]
# }); # -> 2
#
# test_01:
# connectedComponentsCount({
#   1: [2],
#   2: [1,8],
#   6: [7],
#   9: [8],
#   7: [6, 8],
#   8: [9, 7, 2]
# }); # -> 1
#
# test_02:
# connectedComponentsCount({
#   3: [],
#   4: [6],
#   6: [4, 5, 7, 8],
#   8: [6],
#   7: [6],
#   5: [6],
#   1: [2],
#   2: [1]
# }); # -> 3
#
# test_03:
# connectedComponentsCount({}); # -> 0
#
# test_04:
# connectedComponentsCount({
#   0: [4,7],
#   1: [],
#   2: [],
#   3: [6],
#   4: [0],
#   6: [3],
#   7: [0],
#   8: []
# }); # -> 5


# [[[[[[[[[[[[[[[[[[[[[[[[[ #41 largest component ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, largestComponent, that takes in the adjacency list of an 
# undirected graph. The function should return the size of the largest connected
# component in the graph.
#
# test_00:
# largestComponent({
#   0: ['8', '1', '5'],
#   1: ['0'],
#   5: ['0', '8'],
#   8: ['0', '5'],
#   2: ['3', '4'],
#   3: ['2', '4'],
#   4: ['3', '2']
# }); # -> 4
#
# test_01:
# largestComponent({
#   1: ['2'],
#   2: ['1','8'],
#   6: ['7'],
#   9: ['8'],
#   7: ['6', '8'],
#   8: ['9', '7', '2']
# }); # -> 6
#
# test_02:
# largestComponent({
#   3: [],
#   4: ['6'],
#   6: ['4', '5', '7', '8'],
#   8: ['6'],
#   7: ['6'],
#   5: ['6'],
#   1: ['2'],
#   2: ['1']
# }); # -> 5
#
# test_03:
# largestComponent({}); # -> 0
#
# test_04:
# largestComponent({
#   0: ['4','7'],
#   1: [],
#   2: [],
#   3: ['6'],
#   4: ['0'],
#   6: ['3'],
#   7: ['0'],
#   8: []
# }); # -> 3


# [[[[[[[[[[[[[[[[[[[[[[[[[ #42 shortest path ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, shortestPath, that takes in an list of edges for an 
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
# ];
#
# shortestPath(edges, 'w', 'z'); # -> 2
#
# test_01:
# edges = [
#   ['w', 'x'],
#   ['x', 'y'],
#   ['z', 'y'],
#   ['z', 'v'],
#   ['w', 'v']
# ];
#
# shortestPath(edges, 'y', 'x'); # -> 1
#
# test_02:
# edges = [
#   ['a', 'c'],
#   ['a', 'b'],
#   ['c', 'b'],
#   ['c', 'd'],
#   ['b', 'd'],
#   ['e', 'd'],
#   ['g', 'f']
# ];
#
# shortestPath(edges, 'a', 'e'); # -> 3
#
# test_03:
# edges = [
#   ['a', 'c'],
#   ['a', 'b'],
#   ['c', 'b'],
#   ['c', 'd'],
#   ['b', 'd'],
#   ['e', 'd'],
#   ['g', 'f']
# ];
#
# shortestPath(edges, 'e', 'c'); # -> 2
#
# test_04:
# edges = [
#   ['a', 'c'],
#   ['a', 'b'],
#   ['c', 'b'],
#   ['c', 'd'],
#   ['b', 'd'],
#   ['e', 'd'],
#   ['g', 'f']
# ];
#
# shortestPath(edges, 'b', 'g'); # -> -1
#
# test_05:
# edges = [
#   ['c', 'n'],
#   ['c', 'e'],
#   ['c', 's'],
#   ['c', 'w'],
#   ['w', 'e'],
# ];
#
# shortestPath(edges, 'w', 'e'); # -> 1
#
# test_06:
# edges = [
#   ['c', 'n'],
#   ['c', 'e'],
#   ['c', 's'],
#   ['c', 'w'],
#   ['w', 'e'],
# ];
#
# shortestPath(edges, 'n', 'e'); # -> 2
#
# test_07:
# edges = [
#   ['m', 'n'],
#   ['n', 'o'],
#   ['o', 'p'],
#   ['p', 'q'],
#   ['t', 'o'],
#   ['r', 'q'],
#   ['r', 's']
# ];
#
# shortestPath(edges, 'm', 's'); # -> 6


# [[[[[[[[[[[[[[[[[[[[[[[[[ #43 island count ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, islandCount, that takes in a grid containing Ws and Ls. W 
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
# ];
#
# islandCount(grid); # -> 3
#
# test_01:
# grid = [
#   ['L', 'W', 'W', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['W', 'L', 'W', 'L', 'W'],
#   ['W', 'W', 'W', 'W', 'W'],
#   ['W', 'W', 'L', 'L', 'L'],
# ];
#
# islandCount(grid); # -> 4
#
# test_02:
# grid = [
#   ['L', 'L', 'L'],
#   ['L', 'L', 'L'],
#   ['L', 'L', 'L'],
# ];
#
# islandCount(grid); # -> 1
#
# test_03:
# grid = [
#   ['W', 'W'],
#   ['W', 'W'],
#   ['W', 'W'],
# ];
#
# islandCount(grid); # -> 0


# [[[[[[[[[[[[[[[[[[[[[[[[[ #44 minimum island ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, minimumIsland, that takes in a grid containing Ws and Ls. 
# W represents water and L represents land. The function should return the size
# of the smallest island. An island is a vertically or horizontally connected 
# region of land.
#
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
# ];
#
# minimumIsland(grid); # -> 2
#
# test_01:
# grid = [
#   ['L', 'W', 'W', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['W', 'L', 'W', 'L', 'W'],
#   ['W', 'W', 'W', 'W', 'W'],
#   ['W', 'W', 'L', 'L', 'L'],
# ];
#
# minimumIsland(grid); # -> 1
#
# test_02:
# grid = [
#   ['L', 'L', 'L'],
#   ['L', 'L', 'L'],
#   ['L', 'L', 'L'],
# ];
#
# minimumIsland(grid); # -> 9
#
# test_03:
# grid = [
#   ['W', 'W'],
#   ['L', 'L'],
#   ['W', 'W'],
#   ['W', 'L']
# ];
#
# minimumIsland(grid); # -> 1


# [[[[[[[[[[[[[[[[[[[[[[[[[ #45 closest carrot ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, closestCarrot, that takes in a grid, a starting row, and a 
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
# ];
# 
# closestCarrot(grid, 1, 2); # -> 4
#
# test_01:
# grid = [
#   ['O', 'O', 'O', 'O', 'O'],
#   ['O', 'X', 'O', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['O', 'X', 'C', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['C', 'O', 'O', 'O', 'O'],
# ];
# 
# closestCarrot(grid, 0, 0); # -> 5
#
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
# ];
# 
# closestCarrot(grid, 3, 4); # -> 9
#
# test_03:
# grid = [
#   ['O', 'O', 'X', 'O', 'O'],
#   ['O', 'X', 'X', 'X', 'O'],
#   ['O', 'X', 'C', 'C', 'O'],
# ];
# 
# closestCarrot(grid, 1, 4); # -> 2
#
# test_04:
# grid = [
#   ['O', 'O', 'X', 'O', 'O'],
#   ['O', 'X', 'X', 'X', 'O'],
#   ['O', 'X', 'C', 'C', 'O'],
# ];
# 
# closestCarrot(grid, 2, 0); # -> -1


# [[[[[[[[[[[[[[[[[[[[[[[[[ #46 longest path ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, longestPath, that takes in an adjacency list for a directed
# acyclic graph. The function should return the length of the longest path 
# within the graph. A path may start and end at any two nodes. The length of a
# path is considered the number of edges in the path, not the number of nodes.
#
# test_00:
# graph = {
#   a: ['c', 'b'],
#   b: ['c'],
#   c: []
# };
#
# longestPath(graph); # -> 2
#
# test_01:
# graph = {
#   a: ['c', 'b'],
#   b: ['c'],
#   c: [],
#   q: ['r'],
#   r: ['s', 'u', 't'],
#   s: ['t'],
#   t: ['u'],
#   u: []
# };
#
# longestPath(graph); # -> 4
#
# test_02:
# graph = {
#   h: ['i', 'j', 'k'],
#   g: ['h'],
#   i: [],
#   j: [],
#   k: [],
#   x: ['y'],
#   y: []
# };
#
# longestPath(graph); # -> 2
#
# test_03:
# graph = {
#   a: ['b'],
#   b: ['c'],
#   c: [],
#   e: ['f'],
#   f: ['g'],
#   g: ['h'],
#   h: []
# };
#
# longestPath(graph); # -> 3


# [[[[[[[[[[[[[[[[[[[[[[[[[ #47 semesters required ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, semestersRequired, that takes in a number of courses (n) and
# a list of prerequisites as arguments. Courses have ids ranging from 0 through
# n - 1. A single prerequisite of [A, B] means that course A must be taken 
# before course B. Return the minimum number of semesters required to complete
# all n courses. There is no limit on how many courses you can take in a single
# semester, as long the prerequisites of a course are satisfied before taking it.
#
# Note that given prerequisite [A, B], you cannot take course A and course B
# concurrently in the same semester. You must take A in some semester before B.
#
# You can assume that it is possible to eventually complete all courses.
#
# test_00:
# numCourses = 6;
# prereqs = [
#   [1, 2],
#   [2, 4],
#   [3, 5],
#   [0, 5],
# ];
# semestersRequired(numCourses, prereqs); # -> 3
#
# test_01:
# numCourses = 7;
# prereqs = [
#   [4, 3],
#   [3, 2],
#   [2, 1],
#   [1, 0],
#   [5, 2],
#   [5, 6],
# ];
# semestersRequired(numCourses, prereqs); # -> 5
#
# test_02:
# numCourses = 5;
# prereqs = [
#   [1, 0],
#   [3, 4],
#   [1, 2],
#   [3, 2],
# ];
# semestersRequired(numCourses, prereqs); # -> 2
#
# test_03:
# numCourses = 12;
# prereqs = [];
# semestersRequired(numCourses, prereqs); # -> 1
#
# test_04:
# numCourses = 3;
# prereqs = [
#   [0, 2],
#   [0, 1],
#   [1, 2],
# ];
# semestersRequired(numCourses, prereqs); # -> 3
#
# test_05:
# numCourses = 6;
# prereqs = [
#   [3, 4],
#   [3, 0],
#   [3, 1],
#   [3, 2],
#   [3, 5],
# ];
# semestersRequired(numCourses, prereqs); # -> 2


# [[[[[[[[[[[[[[[[[[[[[[[[[ #48 best bridge ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, bestBridge, that takes in a grid as an argument. The grid 
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
# ];
# bestBridge(grid); # -> 1
#
# test_01:
# grid = [
#   ["W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W"],
#   ["L", "L", "W", "W", "L"],
#   ["W", "L", "W", "W", "L"],
#   ["W", "W", "W", "L", "L"],
#   ["W", "W", "W", "W", "W"],
# ];
# bestBridge(grid); # -> 2
#
# test_02:
# grid = [
#   ["W", "W", "W", "W", "W"],
#   ["W", "W", "W", "L", "W"],
#   ["L", "W", "W", "W", "W"],
# ];
# bestBridge(grid); # -> 3
#
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
# ];
# bestBridge(grid); # -> 3
#
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
# ];
# bestBridge(grid); # -> 2
#
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
# ];
# bestBridge(grid); # -> 8


# [[[[[[[[[[[[[[[[[[[[[[[[[ #49 has cycle ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, hasCycle, that takes in an object representing the adjacency
# list of a directed graph. The function should return a boolean indicating 
# whether or not the graph contains a cycle.
#
# test_00:
# hasCycle({
#   a: ["b"],
#   b: ["c"],
#   c: ["a"],
# }); # -> true
#
# test_01:
# hasCycle({
#   a: ["b", "c"],
#   b: ["c"],
#   c: ["d"],
#   d: [],
# }); # -> false
#
# test_02:
# hasCycle({
#   a: ["b", "c"],
#   b: [],
#   c: [],
#   e: ["f"],
#   f: ["e"],
# }); # -> true
#
# test_03:
# hasCycle({
#   q: ["r", "s"],
#   r: ["t", "u"],
#   s: [],
#   t: [],
#   u: [],
#   v: ["w"],
#   w: [],
#   x: ["w"],
# }); # -> false
#
# test_04:
# hasCycle({
#   a: ["b"],
#   b: ["c"],
#   c: ["a"],
#   g: [],
# }); # -> true


# [[[[[[[[[[[[[[[[[[[[[[[[[ #50 prereqs possible ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, prereqsPossible, that takes in a number of courses (n) and
# prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A
# single prerequisite of [A, B] means that course A must be taken before course
# B. The function should return a boolean indicating whether or not it is
# possible to complete all courses.
# 
# test_00:
# numCourses = 6;
# prereqs = [
#   [0, 1],
#   [2, 3],
#   [0, 2],
#   [1, 3],
#   [4, 5],
# ];
# prereqsPossible(numCourses, prereqs); # -> true
#
# test_01:
# numCourses = 6;
# prereqs = [
#   [0, 1],
#   [2, 3],
#   [0, 2],
#   [1, 3],
#   [4, 5],
#   [3, 0],
# ];
# prereqsPossible(numCourses, prereqs); # -> false
#
# test_02:
# numCourses = 5;
# prereqs = [
#   [2, 4],
#   [1, 0],
#   [0, 2],
#   [0, 4],
# ];
# prereqsPossible(numCourses, prereqs); # -> true
#
# test_03:
# numCourses = 6;
# prereqs = [
#   [2, 4],
#   [1, 0],
#   [0, 2],
#   [0, 4],
#   [5, 3],
#   [3, 5],
# ];
# prereqsPossible(numCourses, prereqs); # -> false
#
# test_04:
# numCourses = 8;
# prereqs = [
#   [1, 0],
#   [0, 6],
#   [2, 0],
#   [0, 5],
#   [3, 7],
#   [4, 3],
# ];
# prereqsPossible(numCourses, prereqs); # -> true
#
# test_05:
# numCourses = 8;
# prereqs = [
#   [1, 0],
#   [0, 6],
#   [2, 0],
#   [0, 5],
#   [3, 7],
#   [7, 4],
#   [4, 3],
# ];
# prereqsPossible(numCourses, prereqs); # -> false
#
# test_06:
# numCourses = 42;
# prereqs = [[6, 36]];
# prereqsPossible(numCourses, prereqs); # -> true


# [[[[[[[[[[[[[[[[[[[[[[[[[ #51 fib ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function fib that takes in a number argument, n, and returns the n-th
# number of the Fibonacci sequence.
# The 0-th number of the sequence is 0.
# The 1-st number of the sequence is 1.
# To generate further numbers of the sequence, calculate the sum of previous two numbers.
# Solve this recursively.
# 
# test_00:
# fib(0); # -> 0
# test_01:
# fib(1); # -> 1
# test_02:
# fib(2); # -> 1
# test_03:
# fib(3); # -> 2
# test_04:
# fib(4); # -> 3
# test_05:
# fib(5); # -> 5
# test_06:
# fib(35); # -> 9227465
# test_07:
# fib(46); # -> 1836311903

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
# tribonacci(0); # -> 0
# test_01:
# tribonacci(1); # -> 0
# test_02:
# tribonacci(2); # -> 1
# test_03:
# tribonacci(5); # -> 4
# test_04:
# tribonacci(7); # -> 13
# test_05:
# tribonacci(14); # -> 927
# test_06:
# tribonacci(20); # -> 35890
# test_07:
# tribonacci(37); # -> 1132436852


# [[[[[[[[[[[[[[[[[[[[[[[[[ #53 sum possible ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function sumPossible that takes in an amount and an list of positive
# numbers. The function should return a boolean indicating whether or not it is
# possible to create the amount by summing numbers of the list. You may reuse
# numbers of the list as many times as necessary.
# You may assume that the target amount is non-negative.
#
# test_00:
# sumPossible(8, [5, 12, 4]); # -> true, 4 + 4
# test_01:
# sumPossible(15, [6, 2, 10, 19]); # -> false
# test_02:
# sumPossible(13, [6, 2, 1]); # -> true
# test_03:
# sumPossible(103, [6, 20, 1]); # -> true
# test_04:
# sumPossible(12, []); # -> false
# test_05:
# sumPossible(12, [12]); # -> true
# test_06:
# sumPossible(0, []); # -> true
# test_07:
# sumPossible(271, [10, 8, 265, 24]); # -> false
# test_08:
# sumPossible(2017, [4, 2, 10]); # -> false


# [[[[[[[[[[[[[[[[[[[[[[[[[ #54 min change ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function minChange that takes in an amount and an list of coins. The
# function should return the minimum number of coins required to create the
# amount. You may use each coin as many times as necessary.
# If it is not possible to create the amount, then return -1.
#
# test_00:
# minChange(8, [1, 5, 4, 12]); # -> 2, because 4+4 is the minimum coins possible
# test_01:
# minChange(13, [1, 9, 5, 14, 30]); # -> 5
# test_02:
# minChange(23, [2, 5, 7]); # -> 4
# test_03:
# minChange(102, [1, 5, 10, 25]); # -> 6
# test_04:
# minChange(200, [1, 5, 10, 25]); # -> 8
# test_05:
# minChange(2017, [4, 2, 10]); # -1
# test_06:
# minChange(271, [10, 8, 265, 24]); # -1
# test_07:
# minChange(0, [4, 2, 10]); # 0
# test_08:
# minChange(0, [])); # 0


# [[[[[[[[[[[[[[[[[[[[[[[[[ #55 count paths ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, countPaths, that takes in a grid as an argument. In the grid,
# 'X' represents walls and 'O' represents open spaces. You may only move down or
# to the right and cannot pass through walls. The function should return the
# number of ways possible to travel from the top-left corner of the grid to the
# bottom-right corner.
#
# test_00:
# grid = [
#   ["O", "O"],
#   ["O", "O"],
# ];
# countPaths(grid); # -> 2
# test_01:
# grid = [
#   ["O", "O", "X"],
#   ["O", "O", "O"],
#   ["O", "O", "O"],
# ];
# countPaths(grid); # -> 5
# test_02:
# grid = [
#   ["O", "O", "O"],
#   ["O", "O", "X"],
#   ["O", "O", "O"],
# ];
# countPaths(grid); # -> 3
# test_03:
# grid = [
#   ["O", "O", "O"],
#   ["O", "X", "X"],
#   ["O", "O", "O"],
# ];
# countPaths(grid); # -> 1
# test_04:
# grid = [
#   ["O", "O", "X", "O", "O", "O"],
#   ["O", "O", "X", "O", "O", "O"],
#   ["X", "O", "X", "O", "O", "O"],
#   ["X", "X", "X", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O"],
# ];
# countPaths(grid); # -> 0
# test_05:
# grid = [
#   ["O", "O", "X", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "X"],
#   ["X", "O", "O", "O", "O", "O"],
#   ["X", "X", "X", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "O"],
# ];
# countPaths(grid); # -> 42
# test_06:
# grid = [
#   ["O", "O", "X", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "X"],
#   ["X", "O", "O", "O", "O", "O"],
#   ["X", "X", "X", "O", "O", "O"],
#   ["O", "O", "O", "O", "O", "X"],
# ];
# countPaths(grid); # -> 0
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
# ];
# countPaths(grid); # -> 40116600
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
# ];
# countPaths(grid); # -> 3190434


# [[[[[[[[[[[[[[[[[[[[[[[[[ #56 max path sum ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, maxPathSum, that takes in a grid as an argument. The
# function should return the maximum sum possible by traveling a path from the
# top-left corner to the bottom-right corner. You may only travel through the
# grid by moving down or right.
#
# test_00:
# grid = [
#   [1, 3, 12],
#   [5, 1, 1],
#   [3, 6, 1],
# ];
# maxPathSum(grid); # -> 18
# test_01:
# grid = [
#   [1, 2, 8, 1],
#   [3, 1, 12, 10],
#   [4, 0, 6, 3],
# ];
# maxPathSum(grid); # -> 36
# test_02:
# grid = [
#   [1, 2, 8, 1],
#   [3, 10, 12, 10],
#   [4, 0, 6, 3],
# ];
# maxPathSum(grid); # -> 39
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
# ];
# maxPathSum(grid); # -> 27
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
# ];
# maxPathSum(grid); # -> 56


# [[[[[[[[[[[[[[[[[[[[[[[[[ #57 non adjacent sum ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, nonAdjacentSum, that takes in an list of numbers as an
# argument. The function should return the maximum sum of non-adjacent elements
# in the list. There is no limit on how many elements can be taken into the sum
# as long as they are not adjacent.
#
# For example, given:
# [2, 4, 5, 12, 7]
#
# The maximum non-adjacent sum is 16, because 4 + 12. 
# 4 and 12 are not adjacent in the list.
#
# test_00:
# nums = [2, 4, 5, 12, 7];
# nonAdjacentSum(nums); # -> 16
# test_01:
# nums = [7, 5, 5, 12];
# nonAdjacentSum(nums); # -> 19
# test_02:
# nums = [7, 5, 5, 12, 17, 29];
# nonAdjacentSum(nums); # -> 48
# test_03:
# nums = [
#   72, 62, 10,  6, 20, 19, 42,
#   46, 24, 78, 30, 41, 75, 38,
#   23, 28, 66, 55, 12, 17, 9,
#   12, 3, 1, 19, 30, 50, 20
# ];
# nonAdjacentSum(nums); # -> 488
# test_04:
# nums = [
#   72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
#   30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
#   83, 80, 56, 68,  6, 22, 56, 96, 77, 98,
#   61, 20,  0, 76, 53, 74,  8, 22, 92, 37,
#   30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
#   72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
#   42
# ];
# nonAdjacentSum(nums); # -> 1465


# [[[[[[[[[[[[[[[[[[[[[[[[[ #58 summing squares ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, summingSquares, that takes a target number as an argument.
# The function should return the minimum number of perfect squares that sum to
# the target. A perfect square is a number of the form (i*i) where i >= 1.
#
# For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.
# Given 12:
# summingSquares(12) -> 3
# The minimum squares required for 12 is three, by doing 4 + 4 + 4.
# Another way to make 12 is 9 + 1 + 1 + 1, but that requires four perfect squares.
#
# test_00:
# summingSquares(8); # -> 2
# test_01:
# summingSquares(9); # -> 1
# test_02:
# summingSquares(12); # -> 3
# test_03:
# summingSquares(1); # -> 1
# test_04:
# summingSquares(31); # -> 4
# test_05:
# summingSquares(50); # -> 2
# test_06:
# summingSquares(68); # -> 2
# test_07:
# summingSquares(87); # -> 4


# [[[[[[[[[[[[[[[[[[[[[[[[[ #59 counting change ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, countingChange, that takes in an amount and an list of
# coins. The function should return the number of different ways it is possible
# to make change for the given amount using the coins.
#
# You may reuse a coin as many times as necessary.
# For example,
# countingChange(4, [1,2,3]) -> 4
# There are four different ways to make an amount of 4:
# 1. 1 + 1 + 1 + 1
# 2. 1 + 1 + 2
# 3. 1 + 3
# 4. 2 + 2
#
# test_00:
# countingChange(4, [1, 2, 3]); # -> 4
# test_01:
# countingChange(8, [1, 2, 3]); # -> 10
# test_02:
# countingChange(24, [5, 7, 3]); # -> 5
# test_03:
# countingChange(13, [2, 6, 12, 10]); # -> 0
# test_04:
# countingChange(512, [1, 5, 10, 25]); # -> 20119
# test_05:
# countingChange(1000, [1, 5, 10, 25]); # -> 142511
# test_06:
# countingChange(240, [1, 2, 3, 4, 5, 6, 7, 8, 9]); # -> 1525987916


# [[[[[[[[[[[[[[[[[[[[[[[[[ #60 list stepper ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, listStepper, that takes in an list of numbers as an
# argument. You start at the first position of the list. The function should
# return a boolean indicating whether or not it is possible reach the last
# position of the list. When situated at some position of the list, you may
# take a maximum number of steps based on the number at that position.
#
# For example, given:
#     idx =  0  1  2  3  4  5
# numbers = [2, 4, 2, 0, 0, 1]
# The answer is true.
# We start at idx 0, we could take 1 step or 2 steps forward.
# The correct choice is to take 1 step to idx 1.
# Then take 4 steps forward to the end at idx 5.
#
# test_00:
# listStepper([2, 4, 2, 0, 0, 1]); # -> true
# test_01:
# listStepper([2, 3, 2, 0, 0, 1]); # -> false
# test_02:
# listStepper([3, 1, 3, 1, 0, 1]); # -> true
# test_03:
# listStepper([4, 1, 5, 1, 1, 1, 0, 4]); # -> true
# test_04:
# listStepper([4, 1, 2, 1, 1, 1, 0, 4]); # -> false
# test_05:
# listStepper([1, 1, 1, 1, 1, 0]); # -> true
# test_06:
# listStepper([1, 1, 1, 1, 0, 0]); # -> false
# test_07:
# listStepper([ 
#   31, 30, 29, 28, 27,
#   26, 25, 24, 23, 22,
#   21, 20, 19, 18, 17,
#   16, 15, 14, 13, 12,
#   11, 10, 9, 8, 7, 6,
#   5, 3, 2, 1, 0, 0, 0
# ]); # -> false


# [[[[[[[[[[[[[[[[[[[[[[[[[ #61 max palin subsequence ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, max_palin_subsequence, that takes in a string as an argument.
# The function should return the length of the longest subsequence of the string
# that is also a palindrome.
# A subsequence of a string can be created by deleting any characters of the
# string, while maintaining the relative order of characters.
#
# test_00:
# max_palin_subsequence("luwxult"); # -> 5
# test_01:
# max_palin_subsequence("xyzaxxzy"); # -> 6
# test_02:
# max_palin_subsequence("lol"); # -> 3
# test_03:
# max_palin_subsequence("boabcdefop"); # -> 3
# test_04:
# max_palin_subsequence("z"); # -> 1
# test_05:
# max_palin_subsequence("chartreusepugvicefree"); # -> 7
# test_06:
# max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty"); # -> 15
# test_07:
# max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe"); # -> 31

def max_palin_subsequence(string, memo = {}):
  return _helper(string, 0, len(string), memo)

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
  

# [[[[[[[[[[[[[[[[[[[[[[[[[ #62 overlap subsequence ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, overlapSubsequence, that takes in two strings as arguments.
# The function should return the length of the longest overlapping subsequence.
# A subsequence of a string can be created by deleting any characters of the
# string, while maintaining the relative order of characters.
#
# test_00:
# overlapSubsequence("dogs", "daogt"); # -> 3
# test_01:
# overlapSubsequence("xcyats", "criaotsi"); # -> 4
# test_02:
# overlapSubsequence("xfeqortsver", "feeeuavoeqr"); # -> 5
# test_03:
# overlapSubsequence("kinfolklivemustache", "bespokekinfolksnackwave"); # -> 11
# test_04:
# overlapSubsequence(
#   "mumblecorebeardleggingsauthenticunicorn",
#   "succulentspughumblemeditationlocavore"
# ); # -> 15


# [[[[[[[[[[[[[[[[[[[[[[[[[ #63 can concat ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, canConcat, that takes in a string and an list of words as
# arguments. The function should return boolean indicating whether or not it is
# possible to concatenate words of the list together to form the string.
# You may reuse words of the list as many times as needed.
#
# test_00:
# canConcat("oneisnone", ["one", "none", "is"]); # -> true
# test_01:
# canConcat("oneisnone", ["on", "e", "is"]); # -> false
# test_02:
# canConcat("oneisnone", ["on", "e", "is", "n"]); # -> true
# test_03:
# canConcat("foodisgood", ["is", "g", "ood", "f"]); # -> true
# test_04:
# canConcat("santahat", ["santah", "hat"]); # -> false
# test_05:
# canConcat("santahat", ["santah", "san", "hat", "tahat"]); # -> true
# test_06:
# canConcat("rrrrrrrrrrrrrrrrrrrrrrrrrrx", ["r", "rr", "rrr", "rrrr", "rrrrr", "rrrrrr"]); # -> false


# [[[[[[[[[[[[[[[[[[[[[[[[[ #64 quickest concat ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, quickestConcat, that takes in a string and an list of words
# as arguments. The function should return the minimum number of words needed to
# build the string by concatenating the words.
# You may use words of the list as many times as needed.
#
# test_00:
# quickestConcat('caution', ['ca', 'ion', 'caut', 'ut']); # -> 2
# test_01:
# quickestConcat('caution', ['ion', 'caut', 'caution']); # -> 1
# test_02:
# quickestConcat('respondorreact', ['re', 'or', 'spond', 'act', 'respond']); # -> 4
# test_03:
# quickestConcat('simchacindy', ['sim', 'simcha', 'acindy', 'ch']); # -> 3
# test_04:
# quickestConcat('simchacindy', ['sim', 'simcha', 'acindy']); # -> -1
# test_05:
# quickestConcat('uuuuuu', ['u', 'uu', 'uuu', 'uuuu']); # -> 2
# test_06:
# quickestConcat('rongbetty', ['wrong', 'bet']); # -> -1
# test_07:
# quickestConcat('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', ['u', 'uu', 'uuu', 'uuuu', 'uuuuu']); # -> 7


# [[[[[[[[[[[[[[[[[[[[[[[[[ #65 paired parentheses ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, pairedParentheses, that takes in a string as an argument.
# The function should return a boolean indicating whether or not the string has
# well-formed parentheses.
# You may assume the string contains only alphabetic characters, '(', or ')'.
#
# test_00:
# pairedParentheses("(david)((abby))"); # -> true
# test_01:
# pairedParentheses("()rose(jeff"); # -> false
# test_02:
# pairedParentheses(")("); # -> false
# test_03:
# pairedParentheses("()"); # -> true
# test_04:
# pairedParentheses("(((potato())))"); # -> true
# test_05:
# pairedParentheses("(())(water)()"); # -> true
# test_06:
# pairedParentheses("(())(water()()"); # -> false
# test_07:
# pairedParentheses(""); # -> true


# [[[[[[[[[[[[[[[[[[[[[[[[[ #66 befitting brackets ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, befittingBrackets, that takes in a string as an argument.
# The function should return a boolean indicating whether or not the string
# contains correctly matched brackets.
# You may assume the string contains only characters: ( ) [ ] { }
#
# test_00:
# befittingBrackets('(){}[](())'); # -> true
# test_01:
# befittingBrackets('({[]})'); # -> true
# test_02:
# befittingBrackets('[][}'); # -> false
# test_03:
# befittingBrackets('{[]}({}'); # -> false
# test_04:
# befittingBrackets('[]{}(}[]'); # -> false
# test_05:
# befittingBrackets('[]{}()[]'); # -> true
# test_06:
# befittingBrackets(']{}'); # -> false
# test_07:
# befittingBrackets(''); # -> true


# [[[[[[[[[[[[[[[[[[[[[[[[[ #67 decompress braces ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, decompressBraces, that takes in a compressed string as an
# argument. The function should return the string decompressed.
# The compression format of the input string is 'n{subString}', where the
# subString within braces should be repeated n times.
# You may assume that every number n is guaranteed to be an integer between 1
# through 9.
# You may assume that the input is valid and the decompressed string will only
# contain alphabetic characters.
#
# test_00:
# decompressBraces("2{q}3{tu}v"); 
# -> qqtututuv 
# test_01:
# decompressBraces("ch3{ao}"); 
# -> chaoaoao
# test_02:
# decompressBraces("2{y3{o}}s"); 
# -> yoooyooos
# test_03:
# decompressBraces("z3{a2{xy}b}"); 
# -> zaxyxybaxyxybaxyxyb 
# test_04:
# decompressBraces("2{3{r4{e}r}io}"); 
# -> reeeerreeeerreeeerioreeeerreeeerreeeerio 
# test_05:
# decompressBraces("go3{spinn2{ing}s}"); 
# -> gospinningingsspinningingsspinningings 
# test_06:
# decompressBraces("2{l2{if}azu}l"); 
# -> lififazulififazul 
# test_07:
# decompressBraces("3{al4{ec}2{icia}}"); 
# -> alececececiciaiciaalececececiciaiciaalececececiciaicia 


# [[[[[[[[[[[[[[[[[[[[[[[[[ #68 nesting score ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, nestingScore, that takes in a string of brackets as an
# argument. The function should return the score of the string according to the
# following rules:
#
# [] is worth 1 point
# XY is worth m + n points where X, Y are substrings of well-formed brackets and m, n are their respective scores
# [S] is worth 2 * k points where S is a substring of well-formed brackets and k is the score of that substring
# You may assume that the input only contains well-formed square brackets.
#
# test_00:
# nestingScore("[]"); # -> 1
# test_01:
# nestingScore("[][][]"); # -> 3
# test_02:
# nestingScore("[[]]"); # -> 2
# test_03:
# nestingScore("[[][]]"); # -> 4
# test_04:
# nestingScore("[[][][]]"); # -> 6
# test_05:
# nestingScore("[[][]][]"); # -> 5
# test_06:
# nestingScore("[][[][]][[]]"); # -> 7
# test_07:
# nestingScore("[[[[[[[][]]]]]]][]"); # -> 129


# [[[[[[[[[[[[[[[[[[[[[[[[[ #69 subsets ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, subsets, that takes in an list an argument. The function
# should return a 2D list where each sublist represents one of the possible
# subsets of the list.
# The elements within the subsets and the subsets themselves may be returned in any order.
# You may assume that the input list contains unique elements.
#
# test_00:
# subsets(['a', 'b']); # ->
# [ 
#   [], 
#   [ 'b' ], 
#   [ 'a' ], 
#   [ 'a', 'b' ] 
# ]
# test_01:
# subsets(['a', 'b', 'c']); # ->
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
# subsets(['x']); # ->
# [ 
#   [], 
#   [ 'x' ] 
# ]
# test_03:
# subsets([]); # ->
# [ 
#   []
# ]
# test_04:
# subsets(['q', 'r', 's', 't']); # ->
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


# [[[[[[[[[[[[[[[[[[[[[[[[[ #70 permutations ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, permutations, that takes in an list an argument. The
# function should return a 2D list where each sublist represents one of the
# possible permutations of the list.
# The sublists may be returned in any order.
# You may assume that the input list contains unique elements.
#
# test_00:
# permutations(['a', 'b', 'c']); # -> 
# [ 
#   [ 'a', 'b', 'c' ], 
#   [ 'b', 'a', 'c' ], 
#   [ 'b', 'c', 'a' ], 
#   [ 'a', 'c', 'b' ], 
#   [ 'c', 'a', 'b' ], 
#   [ 'c', 'b', 'a' ] 
# ] 
# test_01:
# permutations(['red', 'blue']); # ->
# [ 
#   [ 'red', 'blue' ], 
#   [ 'blue', 'red' ] 
# ]
# test_02:
# permutations([8, 2, 1, 4]); # ->
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
# permutations([]); # ->
# [
#  [ ]
# ]


# [[[[[[[[[[[[[[[[[[[[[[[[[ #71 create combinations ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, createCombinations, that takes in an list and a length as
# arguments. The function should return a 2D list representing all of the
# combinations of the specifized length.
# The items within the combinations and the combinations themselves may be returned in any order.
# You may assume that the input list contains unique elements and 1 <= k <= items.length.
#
# test_00:
# createCombinations(["a", "b", "c"], 2); # ->
# [
#   [ 'a', 'b' ],
#   [ 'a', 'c' ],
#   [ 'b', 'c' ]
# ]
# test_01:
# createCombinations(["q", "r", "s", "t"], 2); # ->
# [
#   [ 'q', 'r' ],
#   [ 'q', 's' ],
#   [ 'q', 't' ],
#   [ 'r', 's' ],
#   [ 'r', 't' ],
#   [ 's', 't' ]
# ]
# test_02:
# createCombinations(['q', 'r', 's', 't'], 3)); # ->
# [
#   [ 'q', 'r', 's' ],
#   [ 'q', 'r', 't' ],
#   [ 'q', 's', 't' ],
#   [ 'r', 's', 't' ]
# ]
# test_03:
# createCombinations([1, 28, 94], 3); # ->
# [
#   [ 1, 28, 94 ]
# ]


# [[[[[[[[[[[[[[[[[[[[[[[[[ #72 parenthetical possibilities ]]]]]]]]]]]]]]]]]]]]]]]]]
# Write a function, parentheticalPossibilities, that takes in a string as an
# argument. The function should return an list containing all of the strings
# that could be generated by expanding all parentheses of the string into its
# possibilities.
# For example, the possibilities for 'x(mn)yz' are 'xmyz', 'xnyz'.
#
# test_00:
# parentheticalPossibilities('x(mn)yz'); # -> 
# [ 'xmyz', 'xnyz' ]
# test_01:
# parentheticalPossibilities("(qr)ab(stu)c"); # ->
# [ 'qabsc', 'qabtc', 'qabuc', 'rabsc', 'rabtc', 'rabuc' ]
# test_02:
# parentheticalPossibilities("taco"); # ->
# ['taco']
# test_03:
# parentheticalPossibilities(""); # ->
# ['']
# test_04:
# parentheticalPossibilities("(etc)(blvd)(cat)"); # ->
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


# [[[[[[[[[[[[[[[[[[[[[[[[[ #73 substituting synonyms ]]]]]]]]]]]]]]]]]]]]]]]]] !I
# Write a function, substitutingSynonyms, that takes in a sentence and an object
# as arguments. The object contains words as keys whose values are lists
# containing synonyms. The function should return an list containing all
# possible sentences that can be formed by substituting words of the sentence
# with their synonyms.
# You may return the possible sentences in any order, as long as you return
# all of them.
#
# test_00:
# sentence = "follow the yellow brick road";
# synonyms = {
#   follow: ["chase", "pursue"],
#   yellow: ["gold", "amber", "lemon"],
# };
# substituteSynonyms(sentence, synonyms);
# [
#   'chase the gold brick road',
#   'chase the amber brick road',
#   'chase the lemon brick road',
#   'pursue the gold brick road',
#   'pursue the amber brick road',
#   'pursue the lemon brick road'
# ]
# test_01:
# sentence = "I think it's gonna be a long long time";
# synonyms = {
#   think: ["believe", "reckon"],
#   long: ["lengthy", "prolonged"],
# };
# substituteSynonyms(sentence, synonyms);
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
# sentence = "palms sweaty knees weak arms heavy";
# synonyms = {
#   palms: ["hands", "fists"],
#   heavy: ["weighty", "hefty", "burdensome"],
#   weak: ["fragile", "feeble", "frail", "sickly"],
# };
# substituteSynonyms(sentence, synonyms);
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


# [[[[[[[[[[[[[[[[[[[[[[[[[ #74 linked palindrome ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, linkedPalindrome, that takes in the head of a linked list
# as an argument. The function should return a boolean indicating whether or
# not the linked list is a palindrome. A palindrome is a sequence that is the
# same both forwards and backwards.
#
# test_00:
# a = new Node(3);
# b = new Node(2);
# c = new Node(7);
# d = new Node(7);
# e = new Node(2);
# f = new Node(3);
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# e.next = f;
# 3 -> 2 -> 7 -> 7 -> 2 -> 3
# linkedPalindrome(a); # true
# test_01:
# a = new Node(3);
# b = new Node(2);
# c = new Node(4);
# a.next = b;
# b.next = c;
# 3 -> 2 -> 4
# linkedPalindrome(a); # false
# test_02:
# a = new Node(3);
# b = new Node(2);
# c = new Node(3);
# a.next = b;
# b.next = c;
# 3 -> 2 -> 3
# linkedPalindrome(a); # true
# test_03:
# a = new Node(0);
# b = new Node(1);
# c = new Node(0);
# d = new Node(1);
# e = new Node(0);
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# 0 -> 1 -> 0 -> 1 -> 0
# linkedPalindrome(a); # true
# test_04:
# a = new Node(0);
# b = new Node(1);
# c = new Node(0);
# d = new Node(1);
# e = new Node(1);
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# 0 -> 1 -> 0 -> 1 -> 1
# linkedPalindrome(a); # false
# test_05:
# a = new Node(5);
# 5
# linkedPalindrome(a); # true
# test_06:
# linkedPalindrome(None); # true


# [[[[[[[[[[[[[[[[[[[[[[[[[ #75 middle value ]]]]]]]]]]]]]]]]]]]]]]]]] 
# Write a function, middleValue, that takes in the head of a linked list as an
# argument. The function should return the value of the middle node in the
# linked list. If the linked list has an even number of nodes, then return the
# value of the second middle node.
# You may assume that the input list is non-empty.
#
# test_00:
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# a -> b -> c -> d -> e
# middleValue(a); # c
# test_01:
# a = new Node('a');
# b = new Node('b');
# c = new Node('c');
# d = new Node('d');
# e = new Node('e');
# f = new Node('f');
# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# e.next = f;
# a -> b -> c -> d -> e -> f
# middleValue(a); # d
# test_02:
# x = new Node('x');
# y = new Node('y');
# z = new Node('z');
# x.next = y;
# y.next = z;
# x -> y -> z
# middleValue(x); # y
# test_03:
# x = new Node('x');
# y = new Node('y');
# x.next = y;
# x -> y 
# middleValue(x); # y
# test_04:
# q = new Node('q');
# q
# middleValue(q); # q
