import pytest
from code_challenges.linked_list_zip.linked_list_zip import LinkedList, Node, zip_lists

@pytest.fixture
def L1():
    L1 = LinkedList()
    L1.insert(2)
    L1.insert(3)
    L1.insert(1)
    return L1

@pytest.fixture
def L2():
    L2 = LinkedList()
    L2.insert(4)
    L2.insert(9)
    L2.insert(5)
    return L2

@pytest.fixture
def L3():
    L = LinkedList()
    L.insert(3)
    L.insert(1)
    return L

@pytest.fixture
def L4():
    L = LinkedList()
    L.insert(9)
    L.insert(5)
    return L

@pytest.mark.zip
def test_empty_list():
    LL = LinkedList()
    actual = LL.size
    expected = 0
    assert actual == expected

@pytest.mark.zip
def test_equal_length_lists(L1, L2):
    newList= zip_lists(L1, L2)
    actual = newList.to_string()
    expected = "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> NULL"
    assert actual == expected

@pytest.mark.zip
def test_shorter_first(L3, L2):
    newList= zip_lists(L3, L2)
    actual = newList.to_string()
    expected = "{1} -> {5} -> {3} -> {9} -> {4} -> NULL"
    assert actual == expected


@pytest.mark.zip
def test_shorter_second(L1, L4):
    newList= zip_lists(L1, L4)
    actual = newList.to_string()
    expected = "{1} -> {5} -> {3} -> {9} -> {2} -> NULL"
    assert actual == expected
