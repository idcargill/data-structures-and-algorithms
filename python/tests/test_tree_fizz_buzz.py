import pytest
from code_challenges.tree_fizz_buzz.tree_fizz_buzz import fizz_buzz, fizz_buzz_tree, Node

@pytest.fixture
def tree():
  tree.root = Node(10)
  tree.root.add_child(Node(2))
  tree.root.add_child(Node(3))
  tree.root.add_child(Node(15))
  tree.root.children[0].add_child(Node(5))
  tree.root.children[0].add_child(Node(3))
  return tree

@pytest.mark.fizzbuzz
@pytest.mark.parametrize(
  'test_input, expected',
  [
    (1,'1'),
    (3, 'Fizz'),
    (5, 'Buzz'),
    (15, 'FizzBuzz'),
    (127, '127')
  ])
def test_fizz_buzz(test_input, expected):
  assert fizz_buzz(test_input) == expected

@pytest.mark.fizzbuzz
@pytest.mark.parametrize(
  'test_input, expected',
  [
    (1, 1),
    (fizz_buzz(3), 'Fizz'),
    (fizz_buzz(5), 'Buzz'),
    (fizz_buzz(15), 'FizzBuzz'),
    (fizz_buzz(17), '17')
  ]
)
def test_node(test_input, expected):
  N = Node(test_input)
  assert N.value == expected

@pytest.mark.fizzbuzz
def test_add_children():
  N = Node('Fizz')
  child = Node('Buzz')
  N.add_child(child)
  N.add_child(Node(4))
  assert len(N.children) == 2

@pytest.mark.fizzbuzz
def test_tree(tree):
  expected = 10
  actual = tree.root.value
  assert actual == expected

@pytest.mark.fizzbuzz
def test_tree_children(tree):
  expected = 3
  actual = len(tree.root.children)
  assert actual == expected

@pytest.mark.fizzbuzz
def test_fizz_buzz_tree_child(tree):
  expected = 2
  actual = tree.root.children[0].value
  assert actual == expected

@pytest.mark.fizzbuzz
def test_fizz_buzz_tree_root(tree):
  expected = 'Buzz'
  t = fizz_buzz_tree(tree)
  actual = t.root.value
  assert actual == expected

@pytest.mark.fizzbuzz
def test_fizz_buzz_children_2(tree):
  expected  = '2'
  t = fizz_buzz_tree(tree)
  actual = t.root.children[0].value
  assert actual == expected

@pytest.mark.fizzbuzz
def test_fizz_buzz_children_5(tree):
  expected = 'Fizz'
  t = fizz_buzz_tree(tree)
  actual = t.root.children[1].value
  assert actual == expected