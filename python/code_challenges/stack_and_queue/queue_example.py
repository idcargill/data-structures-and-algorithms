class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None and self.tail == None

    def get_head(self):
        assert(not self.is_empty())
        return self.head.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def dequeue(self):
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next


if __name__ == '__main__':
    q= LinkedListQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    print(q.head.value)
