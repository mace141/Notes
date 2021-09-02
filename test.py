def counting_change(num, coins):
  return _counting_change(num, coins, {})

def _counting_change(num, coins, memo):
  if num in memo:
    return memo[num]
  if num == 0:
    return 1
  
  count = 0
  for c in coins:
    if c <= num:
      count += _counting_change(num - c, coins, memo)
  memo[num] = count
  return count

print(counting_change(4, [1, 2, 3])) # -> 4
print(counting_change(8, [1, 2, 3])) # -> 10
print(counting_change(24, [5, 7, 3])) # -> 5
print(counting_change(13, [2, 6, 12, 10])) # -> 0
print(counting_change(512, [1, 5, 10, 25])) # -> 20119
print(counting_change(1000, [1, 5, 10, 25])) # -> 142511
print(counting_change(240, [1, 2, 3, 4, 5, 6, 7, 8, 9])) # -> 1525987916