# INPUT   [8,4,23,42,16,15]
# OUTPUT  [4,8,15,16,23,42]

def insertion_sort(arr):
  length = len(arr)

  for i in range(len(arr)):
    min = 0
    n = i
    temp = n + 1

    while temp < length and arr[n] > arr[temp] and n >= 0:
      min = arr[temp]
      arr[temp] = arr[n]
      arr[n] = min
      n -= 1
      temp -= 1
  
  return arr
