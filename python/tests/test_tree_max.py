import pytest 
from code_challenges.tree_max.tree_max import MaxTree

@pytest.mark.tree_max
def test_initialized_empty_BT():
  bt = MaxTree()
  assert bt

@pytest.mark.tree_max
def test_tree_add_one():
  bt = MaxTree()
  bt.add(5)
  actual = bt.root.value
  expected = 5
  assert actual == expected

@pytest.mark.tree_max
def test_orderd():
  bt = MaxTree()
  bt.add(1)
  bt.add(2)
  bt.add(3)
  bt.add(4)
  bt.add(5)
  actual = bt.max()
  expected = 5
  assert actual == expected

@pytest.mark.tree_max
def test_highest_first():
  bt = MaxTree()
  bt.add(100)
  bt.add(5)
  bt.add(50)
  actual = bt.max()
  expected = 100
  assert actual == expected


@pytest.mark.tree_max
def test_negative_nums():
  bt = MaxTree()
  bt.add(-5)
  bt.add(100)
  bt.add(-200)
  bt.add(15)
  expected = 100
  actual = bt.max()
  assert actual == expected