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