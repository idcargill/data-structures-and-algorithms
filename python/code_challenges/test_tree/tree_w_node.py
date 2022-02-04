
class Tree:
  def __init__(self):
    self.root = None

  @staticmethod 
  class TreeNode:
    def __init__(self, value=None, left=None, right=None):
      self.value = value
      self.left = left
      self.right = right

  
  def is_empty(self):
    return self.root is None
  
  def pre_order(self):
    order = []
    if self.root is None:
      return
    
    self.root.pre_order()
    def pre_order(root):
      if root:
        if root.left:
          pre_order(root.left)
        if root.right:
          pre_order(root.right)
    pre_order(self.root)
    return order
    

    

  def in_order(self):
    pass

  def post_order(self):
    pass

  def contains(self, value):
    pass

  def add_breadth(self, value):
    # level traversal 
    pass
    
  def level_load_list(self, list):
    # binary breadth first. load from middle postion of list
    pass


# t = Tree()
# t.root = Tree.TreeNode('a')
# t.root.left = Tree.TreeNode('b')
# t.root.right = Tree.TreeNode('c')
# t.root.left.left = Tree.TreeNode('d')

# print(t.pre_order())