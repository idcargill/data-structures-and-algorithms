from code_challenges.hash_table.hash_table import HashTable
from code_challenges.trees.tree import BinaryTree

def tree_intersection(bt1, bt2):
  intersections = []
  h = HashTable()

  def tree_traversal(root):
    if h.contains(str(root.value)) == True:
      intersections.append(root.value)
    else:
      h.set(str(root.value), 1)
    if root.left:
      tree_traversal(root.left)
    if root.right:
      tree_traversal(root.right)  
    
  tree_traversal(bt1.root)
  tree_traversal(bt2.root)
  
  return intersections


# s1 = [150, 100, 250, 75, 160, 125, 175, 200, 350, 300, 500]
# s2 = [42, 100, 600, 15, 160, 125, 175, 200, 350, 4, 500] 

# def bs1():
#   bs1 = BinaryTree()
#   for i in s1:
#     bs1.add(i)
#   return bs1

# def bs2():
#   bs2 = BinaryTree()
#   for i in s2:
#     bs2.add(i)
#   return bs2

# b1 = bs1()
# b2 = bs2()
# print(tree_intersection(b1, b2))