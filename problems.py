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