from code_challenges.stack_and_queue.Stack import Stack

class PseudoQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.count = 0

    def enqueue(self, value):
        self.s1.push(value)
        self.count += 1

    def is_empty(self):
        self.count == 0

    ## Size
    def dequeue(self):
        if self.is_empty():
            return None

        if self.s2.size == 0:
            self.count -= 1
            return self.s1.pop()
        
        while self.s1.size > 0:
            value = self.s1.pop()
            self.s2.push(value)
        return self.s2.pop()

