
# input
arr = [2,4,6,-8,18]
num = 20

def insert_shift_array(arr, num):
    result = []
    middle = len(arr) // 2
    for i in range(len(arr)):
        if i < middle:
            result.append(arr[i])
        elif i == middle:
            result.append(num)
            result.append(arr[i])
        else:
            result.append(arr[i])
    return result


