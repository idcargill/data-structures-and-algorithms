class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def kth_from_end(self, k):
        current = self.head
        forward = self.head
        count = 0

        if k < 0:
            raise ValueError('No negative kth value')

        while count < k and forward.next is not None:
            forward = forward.next
            count += 1

        while forward.next is not None:
            forward = forward.next
            current = current.next

        if count < k:
            raise ValueError('k is larger than list')
        return current.value

