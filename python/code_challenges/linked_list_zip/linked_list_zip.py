
def handle_exceptions(method):
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except TypeError as te:
            print(f'TypeError with {method.__name__} method')
            return 'Method Error'
    return wrapper

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    @handle_exceptions
    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    @handle_exceptions
    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            elif current.next == None:
                return False
            else:
                current = current.next

    @handle_exceptions
    def to_string(self):
        current = self.head
        result_string = ''
        while current:
            result_string += f'{ {current.value} } -> '
            current = current.next
        else:
            result_string += 'NULL'
        return result_string

    @handle_exceptions
    def all_values(self):
        current = self.head
        results = []
        while current:
            results.append(current.value)
            current = current.next
        return results

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return self.head

        current = self.head

        while current.next:
            current = current.next
        current.next = node

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

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# def zip_lists(L1, L2):
#     newList = LinkedList()
#     values = []
#     p1 = L1.head
#     p2 = L2.head

#     while p1 and p2:
#         values.append(p1.value)
#         values.append(p2.value)
#         p1 = p1.next
#         p2 = p2.next
#     while p1:
#         values.append(p1.value)
#         p1 = p1.next
#     while p2:
#         values.append(p2.value)
#         p2 = p2.next
#     values.reverse()
#     for i in values:
#         newList.insert(i)
#     return newList

# Append
def zip_lists(L1, L2):
    newList = LinkedList()
    p1 = L1.head
    p2 = L2.head

    while p1 or p2:
        if p1:
            newList.append(p1.value)
            p1 = p1.next
        if p2:
            newList.append(p2.value)
            p2 = p2.next


    return newList

