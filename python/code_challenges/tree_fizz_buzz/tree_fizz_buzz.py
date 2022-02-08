import queue
from code_challenges.stack_and_queue.Queue import Queue
from code_challenges.trees.tree import Tree

class ChildNode:
  def __init__(self, value, children = None):
    self.value = value
    self.children = children


def fizz_buzz(value):
  if value % 3 == 0 and value %5 == 0:
    return 'FizzBuzz'
  elif value % 3 == 0:
    return 'Fizz'
  elif value % 5 == 0:
    return 'Buzz'
  else:
    return str(value)


# def check_node(node):
#   if node.children is None:
#     return ChildNode(fizz_buzz(node.value))
#   else:
#     for c in node.children:
#       check_node(c) 


def fizz_buzz_tree(tree):
  Q = Queue()
  T2 = Tree()

  if tree.root:
    Q.enqueue(tree.root)

  while Q.is_empty() == False:
    curr = Q.dequeue()
   
    if curr.childen == None:
      node = ChildNode(fizz_buzz(curr.value))
      T2.add(node)
      return
    else:
      for c in curr.children:
        Q.enqueue(c)
        node = ChildNode(fizz_buzz(curr.value))
      
    
    


