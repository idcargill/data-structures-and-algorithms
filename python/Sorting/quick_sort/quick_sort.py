def partition(arr, lower, upper):
  if (upper <= lower):
    return
  pivot = arr[lower]
  start = lower
  end = upper

  while (lower < upper):
    while (arr[lower] <= pivot and lower < upper):
      lower += 1
    while (arr[upper] >= pivot and lower <= upper):
      upper -= 1
 
    if lower < upper:
      swap(arr, upper, lower)
    swap(arr, upper, start)

 



def swap(arr, i, low):
  temp = arr[i]
  arr[i] = arr[low]
  arr[low] = temp


arr = [8,4,23,42,16,15]






