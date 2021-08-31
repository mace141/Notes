def summing_squares(num):
  return _summing_squares(num, {})

def _summing_squares(num, memo):
  if num in memo:
    return memo[num]
  if num == 0:
    return 0
  if num == 1:
    return 1

  min = float('inf')
  for x in range(num / 2, 0, -1):
    if x**2 <= num:
      count = 1 + _summing_squares(num - x**2, memo)
      min = count if count < min else min 
  memo[num] = min
  return min

print(summing_squares(8)) # -> 2
print(summing_squares(9)) # -> 1
print(summing_squares(12)) # -> 3
print(summing_squares(1)) # -> 1
print(summing_squares(31)) # -> 4
print(summing_squares(50)) # -> 2
print(summing_squares(68)) # -> 2
print(summing_squares(87)) # -> 4