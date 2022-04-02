class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  class Node:
    def __init__(self, value, next=None):
      self.value = value
      self.next = next


  def add_node(self, value):
    if self.head is None:
      self.head = self.Node(value)
      self.size += 1
      return

    curr = self.head

    while curr.next:
      curr = curr.next
    
    curr.next = self.Node(value)
    self.size += 1

  def size(self):
    return self.size

  def all_values(self):
    values = ''
    curr = self.head

    while curr:
      values += f'{curr.value} -> '
      curr = curr.next
    return values
  


def reverse_linked_list(link):
  # Revers the pointer direction of each node
  curr = link.head
  tail = None
  temp = None

  while curr is not None:
    temp = curr.next
    curr.next = tail
    tail = curr
    curr = temp
  link.head = curr
  return link


# L = LinkedList()
# L.add_node(11) 
# L.add_node(5)
# L.add_node(8)
# L.add_node(10)
# L.add_node(15)
# L.add_node(8)
# L.add_node(1000)

# l_reversed = reverse_linked_list(L)
# print(l_reversed.all_values())


def filter_linkedlist(linked_list, k):
  # needs head check repoint
  
  while linked_list.head.value > k:
    linked_list.head = linked_list.head.next
  
  curr = linked_list.head
  prev = None

 
  while curr:
    if curr.value > k:   
      prev.next = curr.next    
      curr = curr.next 
    else:
      prev = curr
      curr = curr.next
  return linked_list

