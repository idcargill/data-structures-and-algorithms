import pytest

try:
    from linked_list_kth import LinkedList, Node
except:
    from linked_list_kth.linked_list_kth import LinkedList, Node


@pytest.fixture
def loaded_list():
    loaded_list = LinkedList()
    loaded_list.insert('a')
    loaded_list.insert('b')
    loaded_list.insert('c')
    loaded_list.insert('d')
    return loaded_list

@pytest.mark.kth
def test_list_created():
    ll = LinkedList()
    actual = ll.head
    expected = None
    assert actual == expected

@pytest.mark.kth
def test_k_2nd_from_end(loaded_list):
    actual = loaded_list.kth_from_end(2)
    expected = 'c'
    assert actual == expected

@pytest.mark.kth
def test_k_greater_than_list_length(loaded_list):
    with pytest.raises(ValueError) as e:
        actual = loaded_list.kth_from_end(10)
        expected = ValueError
        assert actual == expected

@pytest.mark.kth
def test_negative_exception(loaded_list):
    with pytest.raises(ValueError) as e:
        actual = loaded_list.kth_from_end(-1)
        expected = e
        assert actual == expected


@pytest.mark.kth
def test_k_length_of_list():
    pass

@pytest.mark.kth
def test_linked_list_size_1():
    ll = LinkedList()
    ll.insert('One Kitten!')
    actual = ll.kth_from_end(0)
    expected = 'One Kitten!'
    assert actual == expected

@pytest.mark.kth
@pytest.mark.parametrize('input, output', [
    (0, 'a'),
    (1, 'b'),
    (2, 'c'),
    (3, 'd'),
])

def test_valid_inputs(input, output, loaded_list):
    assert loaded_list.kth_from_end(input) == output
