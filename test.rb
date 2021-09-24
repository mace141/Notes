def product_except_self(nums)
  answer = [1] * nums.length
  left = 1
  right = 1
  (0...nums.length).each do |i|
    answer[i] *= left
    answer[-1 - i] *= right
    left *= nums[i]
    right *= nums[-1 - i]
    p answer
    p left
    p right
  end
  answer
end

product_except_self([6, 7, 5, 4])