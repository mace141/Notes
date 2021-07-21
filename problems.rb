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