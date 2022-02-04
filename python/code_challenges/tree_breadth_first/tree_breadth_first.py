# output: [2,7,5,2,6,9,5,11,4]
from code_challenges.stack_and_queue.Queue import Queue

def breadth_first(tree):
  results = []
  Q = Queue()

  if tree.root is None:
    raise Exception('Tree has no value')

  if tree.root:
    Q.enqueue(tree.root)

  while Q.is_empty() == False:
    node = Q.dequeue()
    results.append(node.value)

    if node.left:
      Q.enqueue(node.left)
    if node.right:
      Q.enqueue(node.right)
  return results


  # def breadth_first(tree):
#   results = []
#   s1 = []
#   s2 = []

#   if tree.root is None:
#     raise Exception('Tree has no value')

#   if tree.root:
#     s1.append(tree.root)

#   while len(s1) > 0:
#       # load s2 as Q each time
#       # while len(s1) > 0:
#     s2.append(s1.pop())

#       # pop off s2 - load s1
#     while len(s2) > 0:
#       node = s2.pop()
#       if node:
#         results.append(node.value)

#       if node.left:
#         s1.append(node.left)
#       if node.right:
#         s1.append(node.right)
#   return results

