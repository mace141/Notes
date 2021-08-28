# [[[[[[[[[[[[[[[[[[[[[[[[[ Binary Trees ]]]]]]]]]]]]]]]]]]]]]]]]]

# Definition
    # A tree is a graph that does not contain any cycles
    # A binary tree is a tree where nodes have at most 2 children
        # An empty graph
        # A single node
        # A linked list

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