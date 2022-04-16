from code_challenges.stack_and_queue.stack import Stack

def balanced_brackets(string):
  stack = Stack()
  pairs = {   '{' : '}',   '[': ']',   '(':')'   }
  closing = [ '}', ']', ')' ]

  for i in string:
    # open bracket in stack

    if i in pairs:
      stack.push(i)

    else:
      # check Stack
      if stack.is_empty():
        return False
      if i in closing:
        top = stack.pop()
        if pairs[top] != i:
          return False
  return True


text1 = '[{(cats)}]'

