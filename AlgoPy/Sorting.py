def BubleSort(arr: list):
    _len = len(arr)
    for i in range(_len - 1):
        for j in range(_len - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap Numbers
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    len_ = len(arr)
    middle = len_ // 2
    left = arr[0: middle]
    right = arr[middle:]

    return merge(
        mergeSort(left),
        mergeSort(right)
    )

def merge(left, right):
    result = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    print(left, right)
    result.extend(left[leftIndex:])
    result.extend(right[rightIndex:])

    return result


arr1 = [94, 65, 34, 2, 1, 7, 8]


def SelectionSort(arr: list):
    n = len(arr)
    for i in range(n):
        min_ = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_]:
                min_ = j
        arr[i], arr[min_] = arr[min_], arr[i]
    return arr


def InsertionSort(arr: list):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value
    return arr


