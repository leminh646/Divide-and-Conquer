import random

def partition(arr, low, high):
    # random pivot
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickSort(arr, low=0, high=None):
    if high is None:
        high = len(arr)-1
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)
