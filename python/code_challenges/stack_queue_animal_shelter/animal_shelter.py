from code_challenges.stack_and_queue.Stack import Stack
from code_challenges.stack_and_queue.test.test_stack import S

class Animal:
    def __init__(self, fluffy):
      self.fluffy = fluffy
      self.type = self._validate_fluffy()

    def _validate_fluffy(self):
      little_fluff = self.fluffy.lower()
      if little_fluff in ['cat', 'dog']:
        return little_fluff
      else:
        raise NameError("Shelter can only take a 'cat' or 'dog'")


class AnimalShelter:
  def __init__(self):
    self.counter = 0
    self.front = self.tail = None
    self.stack = Stack()

  class _Node:
    def __init__(self, value, next=None):
      self.value = value
      self.next = next

  def is_empty(self):
    return self.counter == 0

  def validate_input(self, input):
    little_fluff = input.lower()
    if little_fluff in ['cat', 'dog']:
      return little_fluff
    else:
      raise NameError("Shelter can only take a 'cat' or 'dog'")

  def enqueue(self, fluffy):
    fluffy = Animal(fluffy)
    fluffy_node = self._Node(fluffy)

    if self.is_empty():
      self.front = self.tail = fluffy_node
      self.counter += 1
    else:
      self.tail.next = fluffy_node
      self.tail = fluffy_node
      self.counter += 1
  
  def dequeue(self, fluffy):
    fluffy = self.validate_input(fluffy)
    
    if self.is_empty():
      return None
    
    if self.front.value.type == fluffy:
      self.counter -= 1
      pet = self.front.value.type
      self.front = self.front.next
      return pet

    while self.front.value.type != fluffy:
      self.stack.push(self.front)
      self.front = self.front.next

    if self.front.value.type == fluffy:
      pet = self.front.value.type
      self.counter -= 1
      while self.stack.peek():
        temp = self.stack.pop()
        temp.next = self.front
        self.front = temp
      return pet
    else:
      return None





