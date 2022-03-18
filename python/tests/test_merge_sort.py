import pytest
from Sorting.merge_sort.merge_sort import merge_sort

@pytest.fixture
def s1():
  s1 = [8,4,23,42,16,15]
  return s1

@pytest.fixture
def s2():
  s2 = [20,18,12,8,5,-2]
  return s2

@pytest.fixture
def s3():
  s3 = [5,12,7,5,5,7]
  return s3

def s4():
  s4 = [2,3,5,7,13,11]
  return s4

@pytest.mark.ms
def test_ms_mid(s1):
  mid = len(s1) // 2
  assert mid == 3

@pytest.mark.ms 
def test_ms_left(s1):
  mid = len(s1) // 2
  left = s1[0:mid]
  assert left == [8,4,23]

@pytest.mark.ms 
def test_ms_right(s1):
  mid = len(s1) // 2
  right = s1[mid:]
  assert right == [42,16,15]

@pytest.mark.ms 
def test_ms2_right(s2):
  mid = len(s2) // 2
  right = s2[mid:]
  assert right == [8,5,-2]

@pytest.mark.ms
def test_ms(s1):
  result = merge_sort(s1)
  assert result == [4,8,15,16,23,42]

@pytest.mark.ms
def test_ms2(s2):
  result = merge_sort(s2)
  assert result == [-2,5,8,12,18,20]

@pytest.mark.ms
def test_ms3(s3):
  result = merge_sort(s3)
  assert result == [5,5,5,7,7,12]