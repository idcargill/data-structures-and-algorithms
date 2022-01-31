from code_challenges.trees.node import Node

class Tree:
  def __init__(self, values=None):
    self.root = None

  def pre_order(self):
    # root >> left >> right   a,b,d,e,c,f return array
    values = []
    
    def walk(root):
      if root is None:
        return
      values.append(root.value)
      walk(root.left)
      walk(root.right)
    walk(self.root)
    
    return values
      
  def in_order(self):
    #left >> root >> right    d,b,e,a,f,c
    values = []

    def walk(root):
      if root is None:
        return
      walk(root.left)
      values.append(root.value)
      walk(root.right)
    walk(self.root)

    return values


  def post_order(self):
    #left >> right >> root    d,e,b,f,c,a
    values = []

    def walk(root):
      if root is None:
        return
      walk(root.left)
      walk(root.right)
      values.append(root.value)
    walk(self.root)

    return values


  def add(self, value):
    node = Node(value)
    
    if self.is_empty():
      self.root = node

  def is_empty(self):
   try:
     self.root.value
     return False
   except:
    return True


class BinaryTree(Tree):

  def add(self, value):
    def walk(root):
      if self.root is None:
        self.root = Node(value)
        return
        
      if value > root.value:
        if root.right is None:
          root.right = Node(value)
        else:
          walk(root.right)
      if value < root.value:
        if root.left is None:
          root.left = Node(value)
        else:
          walk(root.left)
    walk(self.root)

  def contains(self, value):
    # return bool

    def walk(root):
      if root is None:
        return False

      if root.value == value:
        return True

      elif root.value < value:
          return walk(root.right)

      elif root.value > value:
        return walk(root.left)
      
      else:
        return False

    return walk(self.root)

