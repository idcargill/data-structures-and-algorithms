
from code_challenges.trees.tree import BinaryTree

class MaxTree(BinaryTree):
  def __init__(self):
    self.root = None
    self.max_value = 0
    super()

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
      