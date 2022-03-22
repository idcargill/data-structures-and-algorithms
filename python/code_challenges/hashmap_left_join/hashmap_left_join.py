from code_challenges.hash_table.hash_table import HashTable

def left_join(h1, h2):
  h3 = HashTable()
  key1 = h1.keys()
  key2 = h2.keys()
  
  for k in key1:
    if k in key2:
      h3[k] = [h1[k], h2[k]]
    else:
      h3[k] = [h1[k], None ]
  return h3
