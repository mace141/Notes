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

print(min_change(8, [1, 5, 4, 12])) # -> 2, because 4+4 is the minimum coins possible
print(min_change(13, [1, 9, 5, 14, 30])) # -> 5
print(min_change(23, [2, 5, 7])) # -> 4
print(min_change(102, [1, 5, 10, 25])) # -> 6
print(min_change(200, [1, 5, 10, 25])) # -> 8
print(min_change(2017, [4, 2, 10])) # -1
print(min_change(271, [10, 8, 265, 24])) # -1
print(min_change(0, [4, 2, 10])) # 0
print(min_change(0, [])) # 0