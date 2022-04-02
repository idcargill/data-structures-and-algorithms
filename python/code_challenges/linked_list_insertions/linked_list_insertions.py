def handle_exceptions(method):
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except TypeError as te:
            print(f'TypeError with {method.__name__} method')
            return 'Method Error'
    return wrapper

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


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
            if value == current.value:
                return True
            else:
                current = current.next
        return False

    @handle_exceptions
    def to_string(self):
        current = self.head
        text = ''
        while current:
            text += f'{ {current.value} } -> '
            current = current.next
        text += 'NULL'
        return text

    @handle_exceptions
    def all_values(self):
        results = []
        current = self.head
        while current:
            results.append(current.value)
            current = current.next
        return results

    @handle_exceptions
    def append(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        node = Node(value)
        current.next = node

    def insert_before(self, value, new_value):
        # add new node before specified node
        try:
            current = self.head
            if current.value == value:
                node = Node(new_value, current)
                self.head = node
                return
            while current.next.value != value:
                current = current.next
            node = Node(new_value, current.next)
            current.next = node
        except:
            return Exception('Value not found')

    def insert_b(self, value, new_value):
        current = self.head
        while current.next.value != value:
            current = current.next
        node = Node(new_value, current.next)
        current.next = node




    def insert_after(self, value, new_Value):
        # add new node after specified node
        current = self.head
        while current:
            if current.value == value:
                node = Node(new_Value, current.next)
                current.next = node
                return
            current = current.next


