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

print(sum_possible(8, [5, 12, 4])) # -> true, 4 + 4
print(sum_possible(15, [6, 2, 10, 19])) # -> false
print(sum_possible(13, [6, 2, 1])) # -> true
print(sum_possible(103, [6, 20, 1])) # -> true
print(sum_possible(12, [])) # -> false
print(sum_possible(12, [12])) # -> true
print(sum_possible(0, [])) # -> true
print(sum_possible(271, [10, 8, 265, 24])) # -> false
print(sum_possible(2017, [4, 2, 10])) # -> false