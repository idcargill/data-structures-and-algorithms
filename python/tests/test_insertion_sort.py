import pytest
# from Sorting.insertion_sort import insertion_sort
from Sorting.insertion_sort.insertion_sort import insertion_sort

@pytest.fixture
def sample():
  sample = [8,4,23,42,16,15]
  return sample
  
@pytest.mark.inSort
def test_insertion_sort(sample):
  result = insertion_sort(sample)
  assert result[0] == 4



