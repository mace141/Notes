nums = [1, 2, 3, 8, 5, 6, 7, 8]

def func(nums):
  singles = set()
  res = 0
  for n in nums:
    if n in singles:
      res += n
    singles.add(n)
  for i in range(1, len(nums)):
    if not i in singles:
      res += i
  return res

print(func(nums))