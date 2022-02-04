import pytest
from code_challenges.stack_queue_pseudo.PseudoQueue import PseudoQueue

@pytest.fixture
def pq():
    pq = PseudoQueue()
    return pq

@pytest.mark.pseudo
def test_enqueue_one():
    pq = PseudoQueue()
    pq.enqueue(1)
    actual = pq.s1.peek()
    expected = 1
    assert actual == expected


@pytest.mark.pseudo
def test_enqueue_two():
    pq = PseudoQueue()
    pq.enqueue(1)
    pq.enqueue('a')
    actual = pq.s1.peek()
    expected = 'a'
    assert actual == expected


@pytest.mark.pseudo
def test_empty_pq(pq):
    with pytest.raises(Exception):
        pq.dequeue()

@pytest.mark.pseudo
def test_dequeue_2(pq):
    pq.enqueue(20)
    pq.enqueue(15)
    pq.enqueue(10)
    pq.dequeue()
    actual = pq.dequeue()
    expected = 15
    assert actual == expected
