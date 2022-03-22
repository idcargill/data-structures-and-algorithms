from code_challenges.hash_table.hash_table import HashTable
from code_challenges.trees.tree import BinaryTree

def tree_intersection(bt1, bt2):
  intersections = []
  h = HashTable()

  def tree_traversal(root):
    if h.contains(str(root.value)) == True:
      intersections.append(root.value)
    else:
      h[str(root.value)] = 1
    if root.left:
      tree_traversal(root.left)
    if root.right:
      tree_traversal(root.right)  
    
  tree_traversal(bt1.root)
  tree_traversal(bt2.root)
  
  return intersections

