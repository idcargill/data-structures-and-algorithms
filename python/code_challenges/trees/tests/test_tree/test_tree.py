import pytest
from trees.node import Node
from trees.tree import Tree, BinaryTree

@pytest.fixture
def T():
  T = Tree()
  T.root = Node('A')
  T.root.left = Node('B')
  T.root.left.left = Node('D')
  T.root.left.right = Node('E')
  T.root.right = Node('C')
  T.root.right.left = Node('F')
  return T

@pytest.fixture
def BinaryT():
  BinaryT = BinaryTree()
  BinaryT.add(10)
  BinaryT.add(15)
  BinaryT.add(5)
  BinaryT.add(4)
  BinaryT.add(17)
  BinaryT.add(30)
  BinaryT.add(12)
  return BinaryT
  

def test_initial_empty_tree():
  T = Tree()
  assert T

def test_is_empty():
  T = Tree()
  actual = T.is_empty()
  expected = True
  assert actual == expected

def test_is_not_empty():
  T = Tree()
  T.root = Node('cats')
  assert T.is_empty() == False

def test_new_node():
  N = Node('fish')
  actual = N.value
  expected = 'fish'
  assert actual == expected

def test_new_node_fail():
  N = Node('fish')
  actual = N.value
  expected = 'FishSticks'
  assert actual != expected

def test_pre_order(T):
  expected = ['A', 'B', 'D', 'E', 'C', 'F']
  actual = T.pre_order()
  assert actual == expected

def test_in_order(T):
  expected = ['D', 'B', 'E', 'A', 'F', 'C']
  actual = T.in_order()
  assert actual == expected

def test_post_order(T):
  expected = ['D', 'E', 'B', 'F', 'C', 'A']
  actual  = T.post_order()
  assert actual == expected

def test_Binary_Tree():
  BT = BinaryTree()
  assert BT

def test_binary_tree_in_order(BinaryT):
  expected = [4, 5, 10, 12, 15, 17, 30]
  actual = BinaryT.in_order()
  assert actual == expected

def test_binary_tree_false(BinaryT):
  expected = False
  actual = BinaryT.contains(100)
  assert actual == expected

def test_binary_tree_false(BinaryT):
  expected = True
  actual = BinaryT.contains(15)
  assert actual == expected


@pytest.mark.parametrize(
  "test_input, expected",
  [
    (10, True),
    (30, True),
    (5, True),
    (4, True),
    (12, True),
    (100, False),
    (5000, False),
    (2, False)
  ])
def test_binary_contains(test_input, expected, BinaryT):
  assert BinaryT.contains(test_input) == expected

