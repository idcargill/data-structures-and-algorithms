class HashTable:
  def __init__(self):
    self.MAX = 5
    self.array = [ None for i in range(self.MAX)]

  def hash(self, key):
    if type(key) is not str:
      raise TypeError

    total = 0
    for i in key:
      total += ord(i)    
    total = total * 3457 % self.MAX
    return total

  def set(self, key, value):
    h = self.hash(key)

    if self.array[h]:
      self.array[h].append((key, value))
    else:
      self.array[h] = [(key, value)]
  
  def get(self, key):
    h = self.hash(key)
    if self.array[h] is None:
      return None

    if len(self.array[h]) > 1:
      for i in self.array[h]:
        if i[0] == key:
          return i[1]
    elif self.array[h] is not None:
      return (self.array[h][0], self.array[h][0][1])

  def contains(self, key):
    h = self.hash(key)
    if self.array[h] is None:
      return False
    if len(self.array[h]) > 1:
      for i in self.array[h]:
        if i[0] == key:
          return True
    return False

  def keys(self):
    keys = []
    for bucket in self.array:
      if bucket is not None:  
        if len(bucket) > 1:
          for k in bucket:
            keys.append(k[0])
        else:
          keys.append(bucket[0][0])
    keys.sort()
    return keys