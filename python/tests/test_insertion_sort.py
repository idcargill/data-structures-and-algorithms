import pytest
from Sorting.insertion_sort.insertion_sort import insertion_sort

@pytest.fixture
def sample():
  sample = [8,4,23,42,16,15]
  return sample
  
@pytest.mark.inSort
def test_insertion_sort(sample):
  result = insertion_sort(sample)
  assert result[0] == 4

@pytest.mark.inSort
@pytest.mark.parametrize("test_data, expected", [
  ([8,4,23,42,16,15], [4, 8, 15, 16, 23, 42]),
  ([2,1,10], [1,2,10]),
  ([10,5,4,30,2,1], [1,2,4,5,10,30])
])
def test_insertion_sort_multiple_array(test_data, expected):
  assert insertion_sort(test_data) == expected
