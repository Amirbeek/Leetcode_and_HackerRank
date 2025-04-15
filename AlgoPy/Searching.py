def binary_search_Recursive(arr, target) -> bool:
    def helper(start, end):
        if start > end:
            return False

        mid = (start + end) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            return helper(start, mid - 1)
        else:
            return helper(mid + 1, end)

    return helper(0, len(arr) - 1)


def binary_search(arr, target):
    if len(arr) == 0:
        return False
    start = 0
    end = len(arr) - 1

    while start <= end:
        midd = (start + end) // 2
        if arr[midd] == target:
            return True
        elif arr[midd] < target:
            start = midd + 1
        else:
            end = midd - 1

    return False


arr = [1, 3, 5, 7, 9, 11]

print(binary_search(arr, 7))  # True
print(binary_search(arr, 4))  # False
print(binary_search(arr, 1))  # True
print(binary_search(arr, 11))  # True
print(binary_search(arr, 12))  # False
print(binary_search([], 1))  # False
