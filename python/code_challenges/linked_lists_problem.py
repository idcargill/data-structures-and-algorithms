# list of linked lists
# Total of each linked list = 599 + 211 + 141 == 951

# ll1: [5]->[9]->[9] = 599
# ll2: [2]->[1]->[1] = 211
# ll3: [1]->[4]->[1] = 141
# return 951

from code_challenges.linked_list.linked_list import LinkedList

def list_total(root):
  string_total = ''
  curr = root.head

  while curr is not None:
    string_total += str(curr.value)
    curr = curr.next
  return string_total

def sum_lists(list):
  total = 0
  for i in list:
    sum = list_total(i)
    total += int(sum)

  return total

# L1 = LinkedList()
# L2 = LinkedList()
# L3 = LinkedList()

# L1.insert(9)
# L1.insert(9)
# L1.insert(5)
# L2.insert(1)
# L2.insert(1)
# L2.insert(2)
# L3.insert(1)
# L3.insert(4)
# L3.insert(1)

# listArray = [ L1, L2, L3]

# print(sum_lists(listArray))
