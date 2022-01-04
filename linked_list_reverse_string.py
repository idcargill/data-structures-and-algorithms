class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            elif current.next == None:
                return False
            else:
                current = current.next

    def to_string(self):
        current = self.head
        result_string = ''
        while current:
            result_string += f'{ {current.value} } -> '
            current = current.next
        else:
            result_string += 'NULL'
        return result_string

    def all_values(self):
        current = self.head
        results = []
        while current:
            results.append(current.value)
            current = current.next
        return results

    def reverse_string(self):
      current = self.head
      reversed_string = ''

      while current:
        reversed_string = f'{reversed_string}{current.value}'
        current = current.next

      return reversed_string




class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



ll = LinkedList()
p = 'python'

for i in p:
  ll.insert(i)

print(ll.reverse_string())

print(ll.head.value)
