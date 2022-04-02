from code_challenges.stack_and_queue.Queue import Queue
from code_challenges.trees.tree import Tree

class Node:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, item):
    self.children.append(item)

def fizz_buzz(value):
  if value % 3 == 0 and value % 5 == 0:
    return 'FizzBuzz'
  elif value % 3 == 0:
    return 'Fizz'
  elif value % 5 == 0:
    return 'Buzz'
  else: 
    return str(value)

def fizz_buzz_tree(tree):
  Q = Queue()
  T2 = Tree()

  if tree.root:
    Q.enqueue(tree.root)

  def check_node(curr):
    new_node = Node(fizz_buzz(curr.value))

    if T2.root is None:
      T2.root = new_node

    if len(curr.children) == 0:
      return new_node
    elif len(curr.children) > 0:
      for c in curr.children: 
        child_node = Node(fizz_buzz(c.value))
        new_node.add_child(child_node)
        Q.enqueue(c)
        check_node(c)
    
  while Q.is_empty() == False:
    curr = Q.dequeue()
    check_node(curr)

  return T2
