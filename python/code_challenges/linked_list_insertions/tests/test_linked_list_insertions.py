import pytest
from linked_list_insertions.linked_list_insertions import LinkedList, Node

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    return ll

@pytest.fixture
def empty_list():
    empty_list = LinkedList()
    return empty_list

def test_node_setup():
    result = Node('Fluffykins')
    assert result.value == 'Fluffykins'

# @pytest.mark.skip
def test_empty_linked_list(empty_list):
    result = empty_list.head
    assert result ==  None

# @pytest.mark.skip
def test_insert_one(empty_list):
    empty_list.insert('Fluffykins')
    assert empty_list.head.value == 'Fluffykins'

def test_insert_multiple(ll):
    ll.insert('fish cakes')
    ll.insert('Fluffykins')
    assert ll.head.value == 'Fluffykins'

# @pytest.mark.skip
def test_includes_true(ll):
    result = ll.includes(2)
    assert result == True

def test_includes_false(ll):
    result = ll.includes('A False Value')
    assert result == False

# @pytest.mark.skip
def test_to_string(ll):
    result = ll.to_string()
    string_test = "{3} -> {2} -> {1} -> NULL"
    assert result == string_test


def test_get_all_values_empty(empty_list):
    result = empty_list.all_values()
    assert result == []

# @pytest.mark.skip
def test_get_all_values(ll):
    assert ll.all_values() == [3, 2, 1]

# Append
def test_append_once(ll):
    ll.append('Fluffykins')
    result = ll.all_values()[-1]
    assert result == 'Fluffykins'

def test_append_multiple(ll):
    ll.append('fish')
    ll.append('tiger')
    ll.append('Fluffykins the great')
    result = ll.all_values()[-1]
    assert result == 'Fluffykins the great'



def test_insert_before_index1(ll):
    ll.insert_before(2, 'Fluffykins')
    results = ll.all_values()
    assert results[1] == 'Fluffykins'

def test_insert_before_last_item(ll):
    ll.insert_before(1, 'Pancakes')
    results = ll.all_values()
    assert results[2] == 'Pancakes'

def test_insert_before_first_item(ll):
    ll.insert_before(3, 'Fluffykins')
    results = ll.all_values()
    assert results[0] == 'Fluffykins'


def test_insert_after(ll):
    ll.insert_after(1, 'Fluffykins')
    results = ll.all_values()
    assert results[3] == 'Fluffykins'








## ERROR TESTING
def test_error_insert():
    cookie_dough = LinkedList()
    assert cookie_dough.insert() == 'Method Error'

def test_error_includes_to_string():
    ll = LinkedList()
    assert ll.includes() == 'Method Error'

def test_error_to_string():
    ll = LinkedList()
    assert ll.to_string() == 'NULL'

def test_error_insert_before_not_found(ll):
    with pytest.raises(Exception) as e_info:
        ll.insert_before(1, 'Fluffykins')
        assert e_info[0] == 'Value was not found'
