import pytest 
from code_challenges.stack_queue_animal_shelter.animal_shelter import Animal, AnimalShelter

@pytest.fixture 
def cat():
  cat = Animal('cat')
  return cat

@pytest.fixture
def dog():
  dog = Animal('dog')
  return dog

@pytest.fixture
def shelter():
  shelter = AnimalShelter()
  return shelter

@pytest.fixture
def full_shelter():
  full_shelter = AnimalShelter()
  full_shelter.enqueue('cat')
  full_shelter.enqueue('cat')
  full_shelter.enqueue('dog')
  full_shelter.enqueue('cat')
  full_shelter.enqueue('dog')
  return full_shelter


@pytest.mark.parametrize(
  "test_animal_caps, expected",
  [
    ('cat', 'cat'),
    ('dog', 'dog'),
    ('Dog', 'dog'),
    ('CaT', 'cat'),
    ('doG', 'dog')
  ]
)

@pytest.mark.shelter
def test_animal_creation_spelling(test_animal_caps, expected):
  c = Animal(test_animal_caps)
  assert c.type == expected

@pytest.mark.parametrize(
  "test_animal_error, raised",
  [
    ('fish', NameError),
    ('123', NameError)
  ]
)

@pytest.mark.shelter
def test_animal_error(test_animal_error, raised):
  with pytest.raises(NameError):
    Animal(test_animal_error)

@pytest.mark.shelter
def test_animal_number_error():
  with pytest.raises(AttributeError):
    Animal(123)

@pytest.mark.shelter
def test_node_create(shelter):
    node = shelter._Node('cat')
    actual = node.value
    expected = 'cat'
    assert actual == expected

@pytest.mark.shelter
def test_is_empty(shelter):
  actual = shelter.counter
  expected = 0
  assert actual == expected

@pytest.mark.shelter
def test_not_empty(shelter):
  shelter.enqueue('cat')
  actual = shelter.counter
  expected = 1
  assert actual == expected

## Shelter Tests
@pytest.mark.shelter
def test_shelter_enqueue(shelter):
  shelter.enqueue('cat')
  actual = shelter.counter
  expected = shelter.counter == 1
  assert actual == expected

@pytest.mark.shelter
def test_shelter_enqueue_front(shelter):
  shelter.enqueue('cat')
  shelter.enqueue('Dog')
  shelter.enqueue('dog')
  actual = shelter.front.value.type
  expected = 'cat'
  assert actual == expected

@pytest.mark.shelter
def test_shelter_enqueue_tail(shelter):
  shelter.enqueue('cat')
  shelter.enqueue('Dog')
  shelter.enqueue('dog')
  actual = shelter.tail.value.type
  expected = 'dog'
  assert actual == expected

@pytest.mark.shelter
def test_dequeue_one(full_shelter): 
  actual = full_shelter.dequeue('cat') 
  expected = 'cat'
  assert actual == expected
  
@pytest.mark.shelter
def test_dequeue_two(full_shelter):
  full_shelter.dequeue('cat')
  actual = full_shelter.dequeue('dog')
  expected = 'dog'
  assert actual == expected

@pytest.mark.shelter
def test_dequeue_empty_shelter(shelter):
  actual = shelter.dequeue('cat')
  expected = None
  assert actual == expected

@pytest.mark.shelter
def test_dequeue_3rd_match(full_shelter):
  actual = full_shelter.dequeue('dog')
  expected = 'dog'
  assert actual == expected     