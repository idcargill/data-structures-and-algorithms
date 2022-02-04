import pytest 
from code_challenges.stack_and_queue.Stack import Stack
from code_challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets

@pytest.mark.brackets
@pytest.fixture
def S():
  S = Stack()
  return S

@pytest.mark.brackets
@pytest.mark.parametrize(
  'test_input, expected', 
  [
    ('{}', True),
    ('{}(){}', True),
    ('()[[Extra Characters]]', True),
    ('[({}]', False),
    ('(](', False),
    ('{(})', False),
    ('cats', True),
    ('', True)
  ]
)
def test_validate_brackets(test_input, expected):
  assert validate_brackets(test_input) == expected
