def merge_arr(arr1: list[int], arr2: list[int]) -> list:
    i, j = 0, 0
    a, s = len(arr1), len(arr2)
    while i < a and j < s:
        if arr1[i] < arr2[j]:
            yield arr1[i]
            i += 1
        else:
            yield arr2[j]
            j += 1

    while i < a:
        yield arr1[i]
        i += 1

    while j < s:
        yield arr2[j]
        j += 1


print(list(merge_arr([2, 3, 5], [])))
