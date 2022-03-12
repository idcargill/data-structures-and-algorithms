import pytest
from code_challenges.hash_table.hash_table import HashTable

@pytest.fixture
def h():
  h = HashTable()
  return h

@pytest.mark.hash
def test_hash_single(h):
  assert h.hash('a') == 4

@pytest.mark.hash
def test_hash_get(h):
  h.set('cat', 100)
  h.set('tac', 200)
  assert h.get('cat') == 100

@pytest.mark.hash
@pytest.mark.parametrize('test, expected',
[
  ('cat', True),
  ('dolphin', False),
  ('CaT', False),
  ('shark', True),
  ('tac', True)
])
def test_hash_contains(test, expected, h):
    h.set('cat', 100)
    h.set('tac', 500)
    h.set('fish', 200)
    h.set('shark', 300)
    assert h.contains(test) == expected

@pytest.mark.hash
def test_hash_contains_key_error(h):
  with pytest.raises(TypeError):
    h.set(1000, 500)

@pytest.mark.hash
def test_hash_set_key_error(h):
  with pytest.raises(TypeError):
    h.set(555, 1000)

@pytest.mark.hash
def test_hash_get_keys(h):
  h.set('b', 200)
  h.set('a', 100)
  h.set('c', 300)
  h.set('dog', 100)
  h.set('god', 200)
  assert h.keys() == ['a', 'b', 'c', 'dog', 'god']

@pytest.mark.hash 
def test_hash_get_nothing(h):
  assert h.get('fish') == None