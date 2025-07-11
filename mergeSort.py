def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:] or right[j:])
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    L = mergeSort(arr[:mid])
    R = mergeSort(arr[mid:])
    return merge(L, R)
