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

    def to_string(self):
        current = self.head
        result_string = ''
        while current:
            result_string += f'{ {current.value} } -> '
            current = current.next
        else:
            result_string += 'NULL'
        return result_string

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
