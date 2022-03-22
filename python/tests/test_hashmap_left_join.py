import pytest
from code_challenges.hashmap_left_join.hashmap_left_join import left_join
from code_challenges.hash_table.hash_table import HashTable

@pytest.mark.hashleft
@pytest.fixture
def h1():
  h1 = HashTable()
  h1['diligent']= 'employed'
  h1['wrath'] = 'anger'
  h1['kitten'] = 'meow'
  return h1

@pytest.mark.hashleft
@pytest.fixture
def h2():
  h2 = HashTable()
  h2['diligent'] = 'idle'
  h2['wrath'] = 'delight'
  h2['Chuck Norris'] = 'Round house'
  return h2

@pytest.mark.hashleft
def test_key_diligent(h1):
  key = h1.keys()
  assert('diligent' in key)

@pytest.mark.hashleft
def test_key_wrath(h1):
  key = h1.keys()
  assert('wrath' in key)

@pytest.mark.hashleft
def test_key_kitten(h1):
  key = h1.keys()
  assert('kitten' in key)

@pytest.mark.hashleft
def test_left_join(h1, h2):
  h3 = left_join(h1, h2)
  assert h3['diligent'] == ['employed', 'idle']

@pytest.mark.hashleft
def test_left_join_wrath(h1, h2):
  h3 = left_join(h1, h2)
  assert h3['wrath'] == ['anger', 'delight']

@pytest.mark.hashleft
def test_left_join_no_match(h1, h2):
  h3 = left_join(h1, h2)
  assert h3['warrior'] == None

@pytest.mark.hashleft
def test_left_join_chuck(h1, h2):
  h3 = left_join(h1, h2)
  assert 'Chuck Norris' not in h3.keys()


@pytest.mark.hashleft
def test_left_join_kitten_left(h1, h2):
  h3 = left_join(h1, h2)
  assert h3['kitten'] == ['meow', None]