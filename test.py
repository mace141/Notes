def jump(nums):
  start = reach = jumps = 0
  
  while reach < len(nums) - 1:
    print(start, reach) 
    furthest = max(i + nums[i] for i in range(start, reach + 1))
    start, reach = reach, furthest
    jumps += 1
    
  print(start, reach) 
  print(jumps)

jump([1, 1, 1, 1, 1, 1])