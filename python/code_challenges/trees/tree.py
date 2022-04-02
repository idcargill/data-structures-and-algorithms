from code_challenges.stack_and_queue.Queue import Queue
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
  def __init__(self):
    self.root = None
    self.max = 0

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

  def max(self):

    def walk(root):
      if root is None:
        return

      if root.value > self.max_value:
        self.max_value = root.value

      walk(root.left)
      walk(root.right)
      return self.max

    walk(self.root)
    return self.max_value

T = Tree()

for i in range(20):
  T.add_breadth(i)

print(T.pre_order())
