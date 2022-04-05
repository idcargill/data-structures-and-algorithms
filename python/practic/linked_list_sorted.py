from code_challenges.linked_list.linked_list import LinkedList
#Linked List
# edge cases

# Returns True for ascending or descending

# Word soup problems type of solvers 


def is_sorted(linked_list):
  asc = True
  dec = True
  curr = linked_list.head

  while curr.next is not None:
    if curr.next.value <= curr.value:
      asc = False

    if curr.next.value >= curr.value:
      dec = False

    curr = curr.next

  return asc | dec 


if __name__ == '__main__':
  LL = LinkedList()
  values = [1, 2, 5, 10, 3]
  values.reverse()
  
  for i in values:
      LL.insert(i)
  
  print(is_sorted(LL))