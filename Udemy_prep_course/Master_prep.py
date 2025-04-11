def containsCommonItems(arr1: list, arr2: list) -> bool:
    con = {}
    for char in arr1:
        con[char] = True

    for char in arr2:
        if char in con:
            return True

    return False


print(containsCommonItems(['a', 'b', 'c', 'd'], ['x', 'y', 'x']))
