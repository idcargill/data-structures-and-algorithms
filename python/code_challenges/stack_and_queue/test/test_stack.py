import pytest
from code_challenges.stack_and_queue.stack import Stack

@pytest.fixture
def S():
    return Stack()

@pytest.fixture
def L():
    L = Stack()
    L.push('a')
    L.push('b')
    L.push('c')
    L.push('d')
    return L

@pytest.mark.stack
def test_empty_stack(S):
    actual = S.size
    expected = 0
    assert actual == expected

@pytest.mark.stack
def test_push_multiple(S):
    S.push(1)
    S.push(2)
    S.push(3)
    actual = S.size
    expected = 3
    assert expected == actual

@pytest.mark.stack
def test_pop_2(S):
    S.push(1)
    S.push(2)
    S.push(3)
    S.pop()
    S.pop()
    actual = S.head.value
    expected = 1
    assert expected == actual

@pytest.mark.stack
def test_pop_empty_stack(L):
    with pytest.raises(Exception):
        L.pop()
        L.pop()
        L.pop()
        L.pop()
        actual = L.peek()

@pytest.mark.stack
def test_peek(L):
    actual = L.peek()
    expected = 'd'
    assert expected == actual
