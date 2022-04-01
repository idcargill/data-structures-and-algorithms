def reverse1(text):
  reversed = ''
  end = len(text) -1
  for i in range(end+1):
    reversed += text[end]
    end -= 1
  return reversed

def reverse2(text):
  end = len(text)
  text_list = []
  for i in range(end):
    text_list.append(text[end-1])
    end -= 1
  return ''.join(text_list)

def reverse3(text):
  end = len(text) -1
  letters = [None for i in range(end)]

  for i in range(end):
    letters[i] = end
    letters[i] = text[end]
    end -= 1
  final = ''
  return ''.join(letters)
