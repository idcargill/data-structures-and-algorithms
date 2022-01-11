class Queue:
    def __init__(self):
        self.front = None
        self.tail = None
        self.size = 0

    class _Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next
    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        node = self._Node(value)
        if self.is_empty():
            self.front = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('The queue is empty')
        else:
            result = self.front.value
            self.front = self.front.next
            self.size -= 1
            return result

    def peek(self):
        if self.front == None:
            raise Exception("Can't peek at an empty Queue")
        return self.front.value

    def all_items(self):
        front = self.front
        all_values = []
        while front:
            all_values.append(front.value)
            front = front.next
        return all_values


q = Queue()

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print(q.all_items())
