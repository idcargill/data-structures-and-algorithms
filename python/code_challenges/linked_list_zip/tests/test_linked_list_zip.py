import pytest
from linked_list_zip.linked_list_zip import LinkedList, Node, zip_lists

@pytest.fixture
def L1():
    L1 = LinkedList()
    L1.insert('a')
    L1.insert('b')
    L1.insert('c')
    L1.insert('d')
    return L1

@pytest.fixture
def L2():
    L2 = LinkedList()
    L2.insert(1)
    L2.insert(2)
    L2.insert(3)
    L2.insert(4)
    return L2

@pytest.fixture
def L3():
    L3 = LinkedList()
    L3.insert('apple')
    L3.insert('banana')
    L3.insert('carrot')
    L3.insert('dragon fruit')
    L3.insert('endive')
    return L3

@pytest.mark.zip
def test_empty_list():
    LL = LinkedList()
    actual = LL.size
    expected = 0
    assert actual == expected

@pytest.mark.zip
def test_lists_have_value(L1, L2):
    v1 = L1.size
    v2 = L2.size
    expected = True
    actual = v1 == v2
    assert actual == expected

@pytest.mark.zip
def test_zip_equal_lists(L1, L2):
    newList = zip_lists(L1, L2)
    actual = newList.size
    expected = 8
    assert actual == expected

@pytest.mark.zip
def test_zip_larger_second(L1, L3):
    newList = zip_lists(L1, L3)
    actual = newList.size
    expected = 9
    assert actual == expected

@pytest.mark.zip
def test_zip_lists_string(L1, L3):
    newList = zip_lists(L1, L3)
    actual = newList.to_string()
    expected = "{'a'} -> {'apple'} -> {'b'} -> {'banana'} -> {'c'} -> {'carrot'} -> {'d'} -> {'dragon fruit'} -> {'endive'} -> NULL"
    print(actual)
    assert actual == expected
