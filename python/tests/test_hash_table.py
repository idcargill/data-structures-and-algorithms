import pytest
from code_challenges.hash_table.hash_table import HashTable

@pytest.fixture
def h():
  h = HashTable()
  return h

# @pytest.mark.hash
# def test_hash_single(h):
#   assert h.hash('a') == 4

@pytest.mark.hash
def test_hash_get(h):
  h['cat'] = 100
  h['tac'] = 200
  assert h['cat'] == 100

@pytest.mark.hash
@pytest.mark.parametrize('test, expected',
[
  ('cat', True),
  ('dolphin', False),
  ('CaT', False),
  ('shark', False),
  ('tac', True)
])
def test_hash_contains(test, expected, h):
    h['cat'] =  100
    h['tac'] =  500
    h['fish'] = 200
    h['shark'] = 300
    assert h.contains(test) == expected

@pytest.mark.hash
def test_hash_contains_key_error(h):
  with pytest.raises(TypeError):
    h[1000] = 500

@pytest.mark.hash
def test_hash_set_key_error(h):
  with pytest.raises(TypeError):
    h[555] = 1000

@pytest.mark.hash
def test_hash_get_keys(h):
  h['b'] = 200
  h['a'] = 100
  h['c'] =  300
  h['dog'] = 100
  h['god'] = 200
  assert h.keys() == ['a', 'b', 'c', 'dog', 'god']

@pytest.mark.hash 
def test_hash_get_nothing(h):
  assert h['fish'] == None