

class Animal:
    def __init__(self, fluffy):
      self.fluffy = fluffy
      self.type = self._validate_fluffy()

    def _validate_fluffy(self):
      little_fluff = self.fluffy.lower()
      if little_fluff in ['cat', 'dog']:
        return little_fluff
      else:
        raise Exception("Cat's and dogs only!")


class AnimalShelter:
  def __init__(self):
    self.counter = 0
    self.front = self.tail = None


