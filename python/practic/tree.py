from code_challenges.stack_and_queue.Queue import Queue
from code_challenges.stack_and_queue.Stack import Stack

class BinaryTree:
  def __init__(self):
    self.root = None
    self.max = 0

  class Node:
    def __init__(self, value=None):
      self.value = value
      self.left = None
      self.right = None

  def add_node(self, value):
    if self.root is None:
      self.root = self.Node(value)
      return
    
    def walk(root):
      if root is None:
        root = self.Node(value)
        return
      
      if root.left is None:
        root.left = self.Node(value)
        return
      elif root.right is None:
        root.right = self.Node(value)
        return
      walk(root.left)
    return walk(self.root)


  def add_breadth(self,value):
    q = []
    if self.root is None:
      self.root = self.Node(value)
      return

    def walk(root):
      if root:
        q.append(root)
      
      while len(q) > 0:
        node = q.pop()

        if node.left:
          q.append(node.left)
        else:
          node.left = self.Node(value)
          return

        if node.right:
          q.append(node.right)
        else:
          node.right = self.Node(value)
          return
    walk(self.root)
        

  
  def breadth_first_traversal(self):
    values = []
    q = Queue()

    if self.root is None:
      return None
    
    if self.root:
      q.enqueue(self.root)
    
    while q.is_empty() == False:
      node = q.dequeue()

      if node is not None:
        values.append(node.value)
      if node.left:
        q.enqueue(node.left)
      if node.right:
        q.enqueue(node.right)
    return values


  def depth_first_traversal(self):
    # all values / max value / search
    # needs a stack or call stack
    values = []
    if self.root is None:
      return None
 
    def walk(root):
      if root is None:
        return
        # values.append(root.value)   # pre order first
      walk(root.left)
        # values.append(root.value)     # in order 
      walk(root.right)
      values.append(root.value)       # post order

      return  values
    return walk(self.root)
 

      


if __name__ == '__main__':
   
  T = BinaryTree()
  for i in range(1,7):
    T.add_breadth(i)

  print(T.breadth_first_traversal())
  print(T.depth_first_traversal())
  