

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

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def zip_lists(L1, L2):
    newList = LinkedList()
    p1 = L1.head
    p2 = L2.head

    while True:
        if p1 is None and p2 is None:
            break
        elif p1 is None:
            newList.insert(p2.value)
            p2 = p2.next
        elif p2 is None:
            newList.insert(p1.value)
            p1 = p1.next
        else:
            newList.insert(p1.value)
            newList.insert(p2.value)
            p1 = p1.next
            p2 = p2.next
    return newList


l1 = LinkedList()
l2 = LinkedList()

l1.insert('a')
l1.insert('b')
l1.insert('c')

l2.insert(0)
l2.insert(1)
l2.insert(2)
l2.insert(3)
l2.insert(4)

x = zip_lists(l1, l2)

print(x.to_string())
print(x.size)
























    # while p1 != None and p2 != None:

    #     if p1 != None and p2 != None:
    #         newList.insert(p1.value)
    #         newList.insert(p2.value)
    #         p1 = p1.next
    #         p2 = p2.next
    #     elif p1 != None:
    #         newList.insert(p1.value)
    #         p1 = p1.next
    #     elif p2 != None:
    #         newList.insert(p2.value)
    #         p2 = p2.next

    # return newList

