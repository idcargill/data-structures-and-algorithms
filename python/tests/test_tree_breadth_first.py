import pytest 
from code_challenges.trees.tree import Tree
from code_challenges.tree_breadth_first.tree_breadth_first import breadth_first

@pytest.fixture
def tt():
  tt = Tree()
  values = [2,7,5,2,6,9,5,11,4]
  for v in values:
    tt.add_breadth(v)
  return tt

@pytest.fixture
def loaded_tree():
  loaded_tree = Tree()
  loaded_tree.root = Tree.Node(2)
  loaded_tree.root.left = Tree.Node(7)
  loaded_tree.root.right = Tree.Node(5)
  loaded_tree.root.left.left = Tree.Node(2)
  loaded_tree.root.left.right = Tree.Node(6)
  loaded_tree.root.right.right = Tree.Node(9)
  loaded_tree.root.left.right.left = Tree.Node(5)
  loaded_tree.root.left.right.right = Tree.Node(11)
  loaded_tree.root.right.right.left = Tree.Node(4)
  return loaded_tree


@pytest.mark.bf
def test_empty_tree():
  T = Tree()
  assert T

@pytest.mark.bf
def test_tree_loaded():
  T = Tree()
  values = [2,7,5,2,6,9,5,11,4]
  for i in values:
    T.add_breadth(i)

  a = T.root.value
  b = T.root.left.value
  c = T.root.right.value
  d = T.root.left.left.value
  e = T.root.left.right.value
  f = T.root.right.right.value
  g = T.root.left.right.left.value
  h = T.root.left.right.right.value
  i = T.root.right.right.left.value
  actual = [a, b, c, d, e, f, g, h, i]
  expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
  assert actual == expected 


@pytest.mark.bf
def test_breadth_first(loaded_tree):
  actual = breadth_first(loaded_tree)
  expected = [2,7,5,2,6,9,5,11,4]
  assert actual == expected


@pytest.mark.bf
def test_bread_first_raise_exception():
  with pytest.raises(Exception):
    T = Tree()
    breadth_first(T)