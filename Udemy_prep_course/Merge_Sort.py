def Merge_sort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    return merge(
        Merge_sort(left),
        Merge_sort(right)
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

    result.extend(left[leftIndex:])
    result.extend(right[rightIndex:])
    return result


arr1 = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = Merge_sort(arr1)
print("Sorted array:", sorted_arr)
