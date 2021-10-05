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