from code_challenges.stack_and_queue.stack import Stack

class PseudoQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, value):
        self.s1.push(value)

    ## Size
    # def dequeue(self):
    #     while self.s1.size > 0:
    #         value = self.s1.pop()
    #         self.s2.push(value)
    #     return self.s2.pop()


    def dequeue(self):
        is_value = True
        while is_value:
            try:
                 if self.s1.peek() is not None:
                     value = self.s1.pop()
                     self.s2.push(value)
            except Exception as e:
                try:
                    self.s2.peek()
                except Exception as e2:
                    is_value = False
                    return None
                else:
                    is_value = False
                    return self.s2.pop()


if __name__ == '__main__':
    PQ = PseudoQueue()

    PQ.enqueue(20)
    PQ.enqueue(15)
    PQ.enqueue(10)
    PQ.enqueue(100)
    PQ.enqueue(50)
    print(PQ.dequeue())
    print(PQ.dequeue())
    print(PQ.dequeue())
    print(PQ.dequeue())

    print(f'stack_1: {PQ.s1.size}   stack_2: {PQ.s2.size}')



