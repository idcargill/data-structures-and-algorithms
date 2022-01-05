
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
        current = self.head
        while current.next is not None:
            current = current.next
        node = Node(value)
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


def zip_lists(L1, L2):
    newList = LinkedList()
    values = []
    p1 = L1.head
    p2 = L2.head

    while p1 and p2:
        values.append(p1.value)
        values.append(p2.value)
        p1 = p1.next
        p2 = p2.next
    while p1:
        values.append(p1.value)
        p1 = p1.next
    while p2:
        values.append(p2.value)
        p2 = p2.next
    values.reverse()
    for i in values:
        newList.insert(i)
    return newList



# Return New list
# def zip_lists(L1, L2):
#     newList = LinkedList()
#     p1 = L1.head
#     p2 = L2.head

#     while p1 and p2:
#         newList.insert(p1.value)
#         newList.insert(p2.value)
#         p1 = p1.next
#         p2 = p2.next

#     while p1:
#         newList.insert(p1.value)
#         p1 = p1.next

#     while p2:
#         newList.insert(p2.value)
#         p2 = p2.next
#     return newList

# def zip_lists(L1, L2):
#     p1 = L1.head
#     p2 = L2.head
#     p3 = ''

#     while p1.next != None and p2.next != None:
#         p3 = p1.next
#         p1.next = p2
#         p1 = p3

#         p2_next = p2.next
#         p2.next = p3
#         p2 = p2_next
#     while p1.next:
#         p3 = p1.next
#         p1.next = p2
#         p1 = p3

#     return  L2


if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()
    l4 = LinkedList()

    l1.insert(2)
    l1.insert(3)
    l1.insert(1)

    l2.insert(4)
    l2.insert(9)
    l2.insert(5)

    l3.insert(3)
    l3.insert(1)

    l4.insert(9)
    l4.insert(5)


    # x1 = zip_lists(l1, l2)
    # print(x1.to_string())

    # x2 = zip_lists(l3, l2)
    # print(x2.to_string())


    x3 = zip_lists(l1, l4)
    print(x3.to_string())





