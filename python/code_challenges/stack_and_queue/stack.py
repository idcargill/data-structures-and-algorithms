class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    class _Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def peek(self):
        if self.head == None:
            return None
            # raise AttributeError("Stack is empty")
        return self.head.value

    def push(self, value):
        self.head = self._Node(value, self.head)
        self.size +=1

    def pop(self):
        if self.is_empty():
            raise Exception("Nothing to pop")
        temp = self.head.value
        self.head = self.head.next
        return temp
