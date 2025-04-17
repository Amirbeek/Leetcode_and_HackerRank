# buble sort time Big O(n^2), space Big O(1) , this is nested loop , PASS
def quick_sort(arr):
    len_ = len(arr) - 1
    for i in range(len_):
        for j in range(len_ - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# selection sort Time - Big O(n^2), Space(1)
def selection_sort(arr):
    len_ = len(arr)
    for i in range(len_):
        minimum = i
        for j in range(i, len_):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr


# merge sort Time Big O(log-n), Space Big O(n)
def merge_sort(arr):
    len_ = len(arr)
    if len_ <= 1:
        return arr
    midd = len_ // 2
    left = arr[0:midd]
    right = arr[midd:]
    return merge(
        merge_sort(left),
        merge_sort(right)
    )


def merge(left, right):
    leftIndex = 0
    rightIndex = 0
    result = []
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

    result.extend(left[leftIndex:])
    result.extend(right[rightIndex:])
    return result

def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
# Quick Sort - solve then this Leetcode Question: https://leetcode.com/problems/sort-an-array/
nums = [42, 7, 19, 3, 88, 15, 27, 63, 1, 34, 56, 90, 12, 75, 6]
print(merge_sort(nums))
