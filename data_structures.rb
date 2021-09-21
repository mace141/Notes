# [[[[[[[[[[[[[[[[[[[[[[[[[ Binary Trees ]]]]]]]]]]]]]]]]]]]]]]]]]

# Definition
#     A tree is a graph that does not contain any cycles
#     A binary tree is a tree where nodes have at most 2 children
#         An empty graph
#         A single node
#         A linked list

class BiTreeNode
  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end
end

# ========================= In-Order =========================

def in_order(root, values = [])
  return if root == nil 

  in_order(root.left)
  values.push(root.val)
  in_order(root.right)

  values
end

# ========================= Pre-Order =========================

def pre_order(root, values = [])
  return if root == nil 

  values.push(root.val)
  pre_order(root.left)
  pre_order(root.right)

  values
end

# ========================= Post-Order =========================

def post_order(root, values = [])
  return if root == nil 

  post_order(root.left)
  post_order(root.right)
  values.push(root.val)

  values
end

# [[[[[[[[[[[[[[[[[[[[[[[[[ Binary Search Trees ]]]]]]]]]]]]]]]]]]]]]]]]]

# Definition
#     Given any node, the values of the left subtree must be less than the given 
#       node's value and the values of the right subtree must be greater than or
#       equal to the given node's value

# Balanced BST 
#     A BST with minimal height, where left and right subtrees differ in height
#       by at most 1
#     All left and right subtrees are balanced
#     Will have a time complexity of O(log(n))
#         An unbalanced BST will have a time complexity of O(log(n))

# Complete BST 
#     A BST where every node has 2 children except the leaf nodes

# An in order traversal will return the values in increasing order

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

# [[[[[[[[[[[[[[[[[[[[[[[[[ Binary Heaps ]]]]]]]]]]]]]]]]]]]]]]]]]

# Binary heap is a type of binary tree with partially sorted data. It is always
#   balanced and complete. Binary heaps are commonly used as priority queues. 

# Time complexity:
#     Insertion: O(n * log(n))
#     Extraction: O(n * log(n))

# ========================= Max Heap =========================

class MaxHeap
  def initialize
    @array = []
  end
  
  def parent(i)
    (i - 1) / 2 
  end
  
  def insert(n)
    @array << n
    self.sift_up(@array.length - 1)
  end
  
  def sift_up(i)
    return if i == 0
    
    arr = @array
    parent_idx = self.parent(i)
    parent = arr[parent_idx]
    current = arr[i]
    if parent < current
        arr[parent_idx], arr[i] = arr[i], arr[parent_idx]
        self.sift_up(parent_idx)
    end
  end
  
  def get_max
    return nil if @array.length == 0
    return @array.pop if @array.length == 1
    
    max = @array[0]
    @array[0] = @array.pop
    self.sift_down(0)
    return max
  end
  
  def sift_down(i)
    arr = @array
    left_idx = i * 2 + 1
    right_idx = i * 2 + 2
    left_child = arr[left_idx]
    right_child = arr[right_idx]
    
    left_child = -1.0/0 if left_child.nil?
    right_child = -1.0/0 if right_child.nil?
    
    return if arr[i] > left_child && arr[i] > right_child
    
    swap_idx = left_child < right_child ? right_idx : left_idx
    arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
    self.sift_down(swap_idx)
  end
end

# ========================= Min Heap =========================

class MinHeap
  def initialize
    @array = []
  end

  def parent(i)
    (i - 1) / 2
  end

  def left(i)
    i * 2 + 1
  end

  def right(i)
    i * 2 + 2
  end

  def insert(n)
    @array << n
    sift_up(@array.length - 1)
  end

  def sift_up(i)
    return if i == 0

    arr = @array
    parent_idx = parent(i)
    if arr[parent_idx] > arr[i]
      arr[i], arr[parent_idx] = arr[parent_idx], arr[i]
      sift_up(parent_idx)
    end
  end

  def get_min
    return nil if @array.length == 0
    return @array.pop if @array.length == 1
    
    min = @array[0]
    @array[0] = @array.pop
    sift_down(0)
    return min 
  end

  def sift_down(i)
    arr = @array
    current = arr[i]
    left_idx = left(i)
    right_idx = right(i)
    left_child = arr[left_idx]
    right_child = arr[right_idx]

    left_child = 1.0/0 if left_child.nil?
    right_child = 1.0/0 if right_child.nil?

    return if current < left_child && current < right_child 

    swap_idx = left_child < right_child ? left_idx : right_idx 
    arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
    sift_down(swap_idx)
  end
end