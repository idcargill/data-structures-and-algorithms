from code_challenges.stack_and_queue.Queue import Queue
# from code_challenges.trees.node import Node
class Tree:
  def __init__(self, values=None):
    self.root = None
    
    
  class Node:
    def __init__(self, value, left=None, right=None):
      self.value = value
      self.left = left
      self.right = right
    


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


  # def add_breadth(self, value):
  #   # breadth any value / binary
  #   s1 = []
  #   s2 = []
    
  #   if self.root is None:
  #     self.root = self.Node(value)
  #     return
    
  #   if self.root:
  #     s1.append(self.root)

  #   while len(s1) > 0:
  #       s2.append(s1.pop())
  #       node = s2.pop()
           
  #       if node.left is None:
  #         node.left = self.Node(value)
  #       elif node.right is None:
  #         node.right = self.Node(value)
  #       else:
  #         s1.append(node.left)
  #         s1.append(node.right)

  def add_breadth(self, value):
    Q = Queue()

    if self.root is None:
      self.root = self.Node(value)
      return 
    
    if self.root:
      Q.enqueue(self.root)

    while Q.is_empty() == False:
      node = Q.dequeue()
      if node.left is None:
        node.left = self.Node(value)
        return
      if node.right is None:
        node.right = self.Node(value)
      else:
        Q.enqueue(node.left)
        Q.enqueue(node.right)
        
      

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
    node = self.Node(value)
    
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
        self.root = self.Node(value)
        return
        
      if value > root.value:
        if root.right is None:
          root.right = self.Node(value)
        else:
          walk(root.right)
      if value < root.value:
        if root.left is None:
          root.left = self.Node(value)
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
