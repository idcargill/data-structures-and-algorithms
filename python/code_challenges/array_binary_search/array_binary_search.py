# array is sorted

def array_binary_search(arr, value):
    low = arr[0]
    high = arr[len(arr)-1]
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif value < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1



