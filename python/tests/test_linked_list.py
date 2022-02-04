from code_challenges.linked_list.linked_list import LinkedList, Node
import pytest


def test_empty_linked_list():
    result = LinkedList()
    assert result.head ==  None

def test_insert():
    ll = LinkedList()
    ll.insert('Fluffykins')
    assert ll.head.value == 'Fluffykins'

def test_multiple_nodes_insert():
    ll = LinkedList()
    ll.insert('Frank')
    ll.insert('kitten')
    result = ll.head.value
    assert result == 'kitten'

def test_return_true_search():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    result = ll.includes(2)
    assert result == True

def test_return_false_search():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    result = ll.includes(10)
    assert result == False

def test_to_string():
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    result = ll.to_string()
    string_test = "{'c'} -> {'b'} -> {'a'} -> NULL"
    assert result == string_test

def test_error_insert():
    cookie_dough = LinkedList()
    assert cookie_dough.insert() == 'Method Error'

def test_includes_to_string():
    ll = LinkedList()
    assert ll.includes() == 'Method Error'

def test_error_to_string():
    ll = LinkedList()
    assert ll.to_string() == 'NULL'


def test_get_all_values():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.all_values() == [3, 2, 1]
