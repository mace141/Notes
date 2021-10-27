# ========================= LeetCode 66 =========================

def plusOne(digits):
  digits[-1] += 1
  
  for i in range(len(digits) - 1, 0, -1):
    if digits[i] < 10:
      break
    digits[i] = 0
    digits[i - 1] += 1
  
  if digits[0] == 10:
    digits[0] = 0
    digits.insert(0, 1)
      
  return digits

# ========================= LeetCode 15 =========================

def three_sum(nums):
  res = set()
  nums.sort()
  for i, num1 in enumerate(nums):
    diff_1 = 0 - num1
    two = {}
    j = i + 1
    while j < len(nums):
      n = nums[j]
      if n in two:
        sorted_lst = sorted([num1, two[n], n])
        res.add(tuple(sorted_lst))
      diff_2 = diff_1 - n
      two[diff_2] = n
      j += 1
  return res

# ========================= LeetCode 70 =========================

def climbStairs(n):
  return _climb_stairs(n, {})
  
def _climb_stairs(n, memo):
  if n in memo:
    return memo[n]
  if n == 0:
    return 1
  if n < 0:
    return 0
  
  one_step = _climb_stairs(n - 1, memo)
  two_step = _climb_stairs(n - 2, memo)
  memo[n] = one_step + two_step
  return memo[n]

# ========================= LeetCode 198 =========================

def rob(nums):
  return _rob(nums, 0, {})
    
def _rob(nums, i, memo):
  if i in memo:
    return memo[i]
  if i >= len(nums):
    return 0
  
  first = nums[i] + _rob(nums, i + 2, memo)
  second = _rob(nums, i + 1, memo)
  
  memo[i] = max(first, second)
  return memo[i]

# ========================= LeetCode 213 =========================

def rob(nums):
  if len(nums) == 1:
    return nums[0]
  first = _rob(nums, 0, True, {})
  second = _rob(nums, 1, False, {})
  return max(first, second)

def _rob(nums, i, first, memo):
  if i in memo:
    return memo[i]
  if i + 1 == len(nums):
    if first:
      return 0
    else:
      return nums[i]
  if i >= len(nums):
    return 0
  
  take_1 = nums[i] + _rob(nums, i + 2, first, memo)
  skip_1 = _rob(nums, i + 1, first, memo)
  memo[i] = max(take_1, skip_1)
  return memo[i]

# ========================= LeetCode 55 =========================

def can_jump(nums):
  n = len(nums) - 2
  idx = n + 1

  for i in range(n, -1, -1):
    if i + nums[i] >= idx:
      idx = i

  return idx == 0

# ========================= LeetCode 45 =========================

def jump(nums):
  start = reach = jumps = 0
  
  while reach < len(nums) - 1:
    furthest_jump = max(i + nums[i] for i in range(start, reach + 1))
    start, reach = reach, furthest_jump
    jumps += 1
  
  return jumps

# ========================= LeetCode 11 =========================

def maxArea(height):
  max_area = float('-inf')
  i = 0
  j = len(height) - 1
  for w in range(j, 0, -1):
    h1 = height[i]
    h2 = height[j]
    area = min(h1, h2) * w
    max_area = max(max_area, area)
    if h1 > h2:
      j -= 1
    else:
      i += 1
  return max_area

# ========================= LeetCode 121 =========================

def maxProfit(prices):
  res = 0
  min_price = float('inf')
  for p in prices:
    min_price = min(min_price, p)
    res = max(res, p - min_price)
  return res

# ========================= LeetCode 207 =========================

def canFinish(numCourses, prerequisites):
  graph = build_graph(numCourses, prerequisites)
  visited = set()
  for node in graph:
    if inCycle(node, graph, visited, set()):
      return False
  return True
        
def build_graph(n, edges):
  graph = {}
  for i in range(n):
    graph[i] = []
  for pre, post in edges:
    graph[pre].append(post)
  return graph

def inCycle(node, graph, visited, visiting):
  if node in visiting:
    return True
  if node in visited:
    return False
  
  visiting.add(node)
  for neighbor in graph[node]:
    if inCycle(neighbor, graph, visited, visiting):
      return True
  visiting.remove(node)
  visited.add(node)
  
  return False

# ========================= LeetCode 128 =========================

def longestConsecutive(nums):
  num_set = set(nums)
  streak = 0
  for n in num_set:
    if n - 1 not in num_set:
      current_streak = 1
      num = n
      while num + 1 in num_set:
        current_streak += 1
        num += 1
      streak = max(streak, current_streak)
  
  return streak

# ========================= LeetCode 3 =========================

def lengthOfLongestSubstring(s):
  res = 0
  i = 0
  while i < len(s):
    j = i
    visited = set()
    while j < len(s):
      c = s[j]
      if c in visited:
        break
      visited.add(c)
      res = max(res, len(visited))
      j += 1
    i += 1
  return res

# ========================= LeetCode 133 =========================

class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
  if not node:
    return node
  
  dct = {node: Node(node.val)}
  return _cloneGraph(node, dct)
  
def _cloneGraph(node, nodes):
  if node.val in nodes:
    return nodes[node.val]

  clone = Node(node.val)
  nodes[node.val] = clone
  for neighbor in node.neighbors:
    n = _cloneGraph(neighbor, nodes)
    clone.neighbors.append(n)
      
  return clone

# ========================= LeetCode 73 =========================

def set_zeroes(matrix):
  indices = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      num = matrix[i][j]
      if num == 0:
        indices.append((i, j))
  
  for row, col in indices:
    for c in range(len(matrix[0])):
      matrix[row][c] = 0
    for r in range(len(matrix)):
      matrix[r][col] = 0

# ========================= LeetCode 54 =========================

def spiral_order(matrix):
  dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  index = 0
  res = []
  visited = set()
  i = 0
  j = 0
  m = len(matrix[0]) - 1
  n = len(matrix) - 1
  first_space = True
  
  while len(visited) < (m + 1) * (n + 1):
    current = matrix[i][j]
    res.append(current)
    visited.add((i, j))
    top_right = i == 0 and j == m
    bot_right = i == n and j == m
    bot_left = i == n and j == 0 and not first_space
    
    dy, dx = dirs[index]
    if top_right or bot_right or bot_left or (i + dy, j + dx) in visited:
      index += 1
      if index == 4:
        index = 0
      dy, dx = dirs[index]
    
    new_y, new_x = i + dy, j + dx
    first_space = False
    i = new_y
    j = new_x
      
  return res

# ========================= LeetCode 48 =========================

def rotate(matrix):
  for i in range(len(matrix)):
    for j in range(i, len(matrix)):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  
  for i in range(len(matrix)):
    for j in range(len(matrix) // 2):
      matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

# ========================= LeetCode 79 =========================

def exist(board, word):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if search(board, i, j, word, 0, set()):
        return True

  return False

def search(board, r, c, word, i, visited):
  if i == len(word):
    return True
  if (r, c) in visited:
    return False
  if r == len(board) or c == len(board[0]):
    return False
  if r < 0 or c < 0:
    return False
  
  if board[r][c] == word[i]:
    visited.add((r, c))
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dy, dx in deltas:
      if search(board, r + dy, c + dx, word, i + 1, visited):
        return True
    visited.remove((r, c))

  return False

# ========================= LeetCode 57 =========================

def insert(intervals, new_interval):
  new_start, new_end = new_interval
  left, right = [], []
  for itvl in intervals:
    start, end = itvl
    if end < new_start:
      left.append(itvl)
    elif new_end < start:
      right.append(itvl)
    else:
      new_start = min(start, new_start)
      new_end = max(end, new_end)
  return left + [[new_start, new_end]] + right

# ========================= LeetCode 56 =========================

def merge(intervals):
  intervals.sort()
  res = []
  for i in range(len(intervals)):
    start, end = intervals[i]
    if not res or res[-1][1] < start:
      res.append(intervals[i])
    else:
      res[-1][1] = max(res[-1][1], end)
  return res

# ========================= LeetCode 453 =========================

def eraseOverlapIntervals(intervals):
  last = float('-inf')
  res = 0
  for itvl in sorted(intervals, key=lambda i: i[1]):
    if itvl[0] >= last:
      last = itvl[1]
    else:
      res += 1
  return res

# Codewars https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(seconds):
  if seconds == 0:
    return 'now'
  
  time = {
    'second': 1,
    'minute': 60,
    'hour': 60 * 60,
    'day': 24 * 60 * 60,
    'year': 365 * 24 * 60 * 60
  }
  time_lst = ['year', 'day', 'hour', 'minute', 'second']
  
  res_lst = []
  for t in time_lst:
    if seconds >= time[t]:
      n = seconds // time[t]
      s = str(n) + f' {t}' + ('s' if n > 1 else '')
      res_lst.append(s)
      seconds %= time[t]
  res = ''
  for i, s in enumerate(res_lst):
    res += s
    if i < len(res_lst) - 2:
      res += ', '
    elif i == len(res_lst) - 2:
      res += ' and '
  return res

# ========================= LeetCode 724 =========================

def pivotIndex(nums):
  S = sum(nums)
  left = 0
  for i, n in enumerate(nums):
    if left == (S - left - n):
      return i
    left += n
  return -1

# ========================= LeetCode 416 =========================

def canPartition(nums):
  total = sum(nums)
  if total % 2 == 1:
    return False
  target = total / 2
  dp = {0}
  for n in nums:
    if target in dp:
      return True
    dp |= {n + i for i in dp}
  return target in dp

# ========================= LeetCode 494 =========================

def findTargetSumWays(nums, target):
  def helper(nums, target, i, total, memo):
    if (i, total) in memo:
      return memo[(i, total)]
    if target == total and i == len(nums):
      return 1
    if i == len(nums):
      return 0
    
    count = 0
    count += helper(nums, target, i + 1, total - nums[i], memo)
    count += helper(nums, target, i + 1, total + nums[i], memo)
    memo[(i, total)] = count
    return count
  return helper(nums, target, 0, 0, {})

# ========================= LeetCode 26 =========================

def removeDuplicates(nums):
  i = 0
  j = 1
  while j < len(nums):
    if nums[i] != nums[j]:
      i += 1
      nums[i] = nums[j]
    j += 1
  return i + 1

# ========================= LeetCode 122 =========================

def maxProfit(prices):
  total = 0
  for i in range(len(prices) - 1):
    if prices[i] < prices[i + 1]:
      total += prices[i + 1] - prices[i]
  return total

# ========================= LeetCode 983 =========================

def mincostTickets(days, costs):
  passes = [1, 7, 30]
  
  def helper(i, memo):
    if i in memo:
      return memo[i]
    if i >= len(days):
      return 0
    
    low = float('inf')
    j = i
    for c, d in zip(costs, passes):
      while j < len(days) and days[j] < days[i] + d:
        j += 1
      cost = c + helper(j, memo)
      low = min(cost, low)
    memo[i] = low
    return low
  
  return helper(0, {})

# ========================= LeetCode 136 =========================

def single_number(nums):
  x = nums[0]
  for n in nums[1:]:
    x ^= n
  return x

# ========================= LeetCode 350 =========================

def intersect(nums1, nums2):
  count = collections.Counter(nums1)
  res = []
  for n in nums2:
    if count[n] > 0:
      res.append(n)
      count[n] -= 1
  return res

# ========================= LeetCode 283 =========================

def move_zeroes(nums):
  i = 0
  j = 0
  while j < len(nums):
    if nums[j] != 0:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
    j += 1

# ========================= LeetCode 36 =========================

def isValidSudoku(board):
  def valid_line(board, row, col):
    nums = set()
    for i in range(9):
      n = board[row][i] if col is None else board[i][col]
      if n in nums:
        return False
      if n != '.':
        nums.add(n)
    return True
  
  def valid_box(board, r, c):
    nums = set()
    for i in range(3):
      for j in range(3):
        n = board[r + i][c + j]
        if n in nums:
          return False
        if n != '.':
          nums.add(n)
    return True
  
  for i in range(9):
    if not valid_line(board, i, None) or not valid_line(board, None, i):
      return False
  
  box_starts = [0, 3, 6]
  for i in box_starts:
    for j in box_starts:
      if not valid_box(board, i, j):
        return False
  
  return True

# ========================= LeetCode 344 =========================

def reverse_string(s):
  i = 0
  j = len(s) - 1
  while i < j:
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1

# ========================= LeetCode 7 =========================

def reverse(x):
  s = str(x)
  if s[0] == '-':
    n = int(s[:0:-1])
    p = False
  else:
    n = int(s[::-1])
    p = True
  if n < -2**31 or n > 2**31 - 1:
    return 0
  return n if p else -n

# ========================= LeetCode 88 =========================

def merge_sorted_array(nums1, m, nums2, n):
  while m > 0 and n > 0:
    if nums2[n - 1] >= nums1[m - 1]:
      nums1[m + n - 1] = nums2[n - 1]
      n -= 1
    else:
      nums1[m + n - 1] = nums1[m - 1]
      m -= 1
  if n:
    nums1[:n] = nums2[:n]

# ========================= LeetCode 53 =========================

def max_subarray(nums):
  for i in range(1, len(nums)):
    if nums[i - 1] > 0:
      nums[i] += nums[i - 1]
  return max(nums)

# HackerRank: Minimum Processing Time

def minTime(processorTime, taskTime):
  tasks = sorted(taskTime, reverse=True)
  hi = 0
  task = 0
  for t in sorted(processorTime):
    for i in range(4):
      time = t + tasks[task]
      hi = max(time, hi)
      task += 1
  return hi

# HackerRank: Prison Break

def prison(n, m, h, v):
  def helper(nums):
    i = 0
    lst = [2]
    for idx, n in enumerate(nums):
      if nums[idx - 1] + 1 == n:
        lst[i] += 1
      else: 
        i += 1
        lst.append(2)
    return lst
  
  n = max(helper(sorted(h)))
  m = max(helper(sorted(v)))
  
  return n * m