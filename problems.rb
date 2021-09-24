def revrot(str, sz)
  # your code
  return "" if sz <= 0 || str.empty?
  chunks = []
  end_idx = sz
  
  while end_idx <= str.length - 1
    chunks << str[end_idx - sz...end_idx]
    end_idx += sz
  end

  chunks.map do |chunk|
    chunk_nums = chunk.split('').map { |el| el.to_i }
    cube_sum = chunk_nums.inject(0) { |acc, el| acc + el**3 }
    
    if cube_sum % 2 == 0
      chunk.reverse
    else
      chunk[1..-1] + chunk[0]
    end
  end.join('')
end

p revrot("1234", 0)
p revrot("", 0)
p revrot("1234", 5)
p revrot("733049910872815764", 5)

# ========================= LeetCode 110 =========================

def get_height(root)
  return 0 if !root 

  left = get_height(root.left)
  return -1 if left == -1

  right = get_height(root.right)
  if right == -1 || (left - right).abs > 1
      return -1
  end

  return 1 + [left, right].max
end

def is_balanced(root)
  return true if !root
  return get_height(root) != -1
end

def get_height(root)
  return 0 if !root 
  return 1 + [get_height(root.left), get_height(root.right)].max
end

def is_balanced(root)
  return true if !root
  height_diff = (get_height(root.left) - get_height(root.right)).abs
  return height_diff <= 1 && is_balanced(root.left) && is_balanced(root.right)
end

# ========================= LeetCode 108 =========================

def sorted_array_to_bst(nums)
  return nil if nums.length == 0
  middle = nums.length / 2
  root = TreeNode.new(nums[middle])
  root.left = sorted_array_to_bst(nums.take(middle))
  root.right = sorted_array_to_bst(nums.drop(middle + 1))
  return root
end

# ========================= LeetCode 1464 =========================

def max_product(nums)
  max = -1.0/0
  n = max
  m = max
  for num in nums
      if num >  n
          m = n
          n = num
      elsif num > m
          m = num
      end
  end
  return (n - 1) * (m - 1)
end

# ========================= LeetCode 121 =========================

def max_profit(prices)
  max = 0
  min = 1.0/0.0
  (0...prices.length).each do |i|
    if prices[i] < min
      min = prices[i]
    end
    if prices[i] - min > max
      max = prices[i] - min
    end
  end
  
  return max
end

# ========================= LeetCode 152 =========================

def max_product(nums)
  max = nums[0]
  min_so_far = nums[0]
  max_so_far = nums[0]
  
  nums[1..-1].each do |num|
      min_so_far, max_so_far = [num, min_so_far * num, max_so_far * num].minmax
      max = [min_so_far, max_so_far, max].max
  end
  
  return max
end

# ========================= LeetCode 238 =========================

def product_except_self(nums)
  answer = [1] * nums.length
  left = 1
  right = 1
  (0...nums.length).each do |i|
      answer[i] *= left
      answer[-1 - i] *= right
      left *= nums[i]
      right *= nums[-1 - i]
  end
  answer
end

# ========================= LeetCode 153 =========================

def find_min(nums)
  i = 0
  j = nums.length - 1
  if nums[i] < nums[j]
    return nums[i]
  end
  while i < j
    mid = i + (j - i) / 2
    if nums[mid] > nums[mid + 1]
      return nums[mid + 1]
    end
    if nums[mid - 1] > nums[mid]
      return nums[mid]
    end
    if nums[mid] > nums[0]
      i = mid + 1
    else
      j = mid - 1
    end
  end
  return nums[i]
end

# ========================= LeetCode 5 =========================

def longest_palindrome(s)
  max = ''
  (0...s.length).each do |idx|
    i = idx
    j = idx
    while s[i] == s[j + 1]
      j += 1
    end
    while s[i] == s[j]
      if s[i..j].length > max.length
        max = s[i..j]
      end
      i -= 1
      j += 1
    end
  end
  max
end