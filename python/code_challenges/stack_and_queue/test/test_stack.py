import pytest
from Stack import Stack


pytest.mark.stack
def test_empty_stack():
    s = Stack()
    actual = s.size
    expected = -1
    assert actual == expected





