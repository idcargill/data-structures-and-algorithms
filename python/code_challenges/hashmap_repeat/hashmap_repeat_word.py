import re

def repeated_word(text):
  first_duplicate = ''
  duplicate_found = False
  word_count = {}
  words = [word.lower() for word in re.findall('\w+', text, flags=re.I)]


  for word in words:
    if word in word_count:
      word_count[word] += 1
      if word_count[word] == 2:
        if duplicate_found == False:
          first_duplicate = word
          duplicate_found = True 
    else:
      word_count[word] = 1
    
  return {'first duplicate': first_duplicate, 'totals': word_count }
