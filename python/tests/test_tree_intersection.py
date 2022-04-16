import pytest
from code_challenges.tree_intersection.tree_intersection import tree_intersection
from code_challenges.trees.tree import BinaryTree

s1 = [150, 100, 250, 75, 160, 125, 175, 200, 350, 300, 500]
s2 = [42, 100, 600, 15, 160, 125, 175, 200, 350, 4, 500] 
# 100, 160, 125, 175, 200, 350, 500

@pytest.mark.tree_intersect
@pytest.fixture
def bs1():
  bs1 = BinaryTree()
  for i in s1:
    bs1.add(i)
  return bs1

@pytest.mark.tree_intersect
@pytest.fixture
def bs2():
  bs2 = BinaryTree()
  for i in s2:
    bs2.add(i)
  return bs2

@pytest.mark.tree_intersect
def test_bs1_root(bs1):
  actual = bs1.root.value
  expected = 150
  assert actual == expected

@pytest.mark.tree_intersect
def test_bs1_pre(bs1):
  actual = bs1.pre_order()
  expected = [150, 100, 75, 125, 250, 160, 175, 200, 350, 300, 500]
  assert actual == expected

# @pytest.mark.tree_intersect
# def test_tree_intersect(bs1, bs2):
#   actual = tree_intersection(bs1, bs2)
#   expected = [100, 160, 125, 175, 200, 350, 500]
#   assert actual == expected
