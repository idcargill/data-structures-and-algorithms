from code_challenges.tree_breadth_first.tree_breadth_first import breadth_first
class TreeNode:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None
    self.o1 = []
    self.o2 = []
  
  def add_breadth(self, value):
    if self.data is None:
      self.data = TreeNode(value)
      self.o1.append(self.data)
      return
    if self.left is None:
      self.left = TreeNode(value)
      return
    elif self.right is None:
      self.right = TreeNode(value)
      return

    if self.left:
      self.o1.append(self.left)
      
    elif self.right:
      self.o1.append(self.right)
      

    for i in self.o1:
      self.o2.append(self.o1.pop())

    for i in self.o2:
      node = self.o2.pop()
      if node.left is None:
        node.left = TreeNode(value)
      elif node.right is None:
        node.right = TreeNode(value)



   

T = TreeNode()

T.add_breadth('A')
T.add_breadth('B')
T.add_breadth('C')
T.add_breadth('D')
T.add_breadth('E')
T.add_breadth('F')


print(breadth_first(T))