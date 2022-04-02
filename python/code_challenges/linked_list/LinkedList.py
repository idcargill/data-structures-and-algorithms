class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    class _Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def isEmpty(self):
        return self.head == None

    def insert(self, value):
        self.head = self._Node(value, self.head)
        self.size += 1

    def includes(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def to_string(self):
        curr = self.head
        result_string = ''
        while curr:
            result_string += f'{ {curr.value } } -> '
            curr = curr.next
        result_string += f'NULL'
        return result_string

    def all_values(self):
        curr = self.head
        results = []
        while curr:
            results.append(curr.value)
            curr = curr.next
        return results

    def append(self, value):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = self._Node(value)

    def insert_before(self, target,value):
        curr = self.head
        while curr.next:
            if curr.next.value != target:
                curr = curr.next
        curr.next = self._Node(value, curr.next)

    def insert_after(self, target, value):
        curr = self.head
        while curr:
            if curr.value == target:
                curr.next = self._Node(value, curr.next)
            curr = curr.next

    def kth_from_end(self, k):
        curr = self.head
        forward = self.head
        count = 1

        if k < 0:
            raise ValueError('position must be a positive int')

        while count < k:
            count += 1
            forward = forward.next

        while forward.next != None:
            forward = forward.next
            curr = curr.next

        if count < k:
            raise ValueError('kth postion is larger than list')
        return curr.value








