import pytest
from code_challenges.stack_and_queue.Queue import Queue

@pytest.fixture
def S():
    return Queue()

@pytest.fixture
def L():
    L = Queue()
    L.enqueue('a')
    L.enqueue('b')
    L.enqueue('c')
    L.enqueue('d')
    return L

@pytest.mark.queue
def test_empty_queue(S):
    actual = S.size
    expected = 0
    assert actual == expected

@pytest.mark.queue
def test_enqueue_multiple(S):
    S.enqueue(1)
    S.enqueue(2)
    S.enqueue(3)
    actual = S.size
    expected = 3
    assert expected == actual

@pytest.mark.queue
def test_dequeue_2(S):
    S.enqueue(1)
    S.enqueue(2)
    S.enqueue(3)
    S.dequeue()
    S.dequeue()
    actual = S.front.value
    expected = 3
    assert expected == actual

@pytest.mark.queue
def test_dequeue_empty_queue(L):
    with pytest.raises(Exception):
        L.dequeue()
        L.dequeue()
        L.dequeue()
        L.dequeue()
        actual = L.peek()

@pytest.mark.queue
def test_peek(L):
    L.dequeue()
    actual = L.peek()
    expected = 'b'
    assert expected == actual
