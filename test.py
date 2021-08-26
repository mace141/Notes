def tribonacci(n, memo = {}):
  if n in memo:
    return memo[n]
  if n == 0 or n == 1:
    return 0
  if n == 2:
    return 1

  memo[n] = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)
  return memo[n]

print(tribonacci(0)) # -> 0
print(tribonacci(1)) # -> 0
print(tribonacci(2)) # -> 1
print(tribonacci(5)) # -> 4
print(tribonacci(7)) # -> 13
print(tribonacci(14)) # -> 927
print(tribonacci(20)) # -> 35890
print(tribonacci(37)) # -> 1132436852