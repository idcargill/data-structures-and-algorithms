class LinkedList:
    def __init__(self):
        self.size = 0

    class _Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next


