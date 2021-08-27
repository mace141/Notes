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