from code_challenges.stack_and_queue.Stack import Stack

open = ['(', '{', '[']
close= [')', '}', ']']

pairs = dict(zip(open, close))

def validate_brackets(string):
  S = Stack()

  for char in string:
    if char in open:
      S.push(char)
    elif char in close:
      if S.is_empty():
        return False
      if char != pairs[S.pop()]:
        return False
  return True
