def bs(arr, target, left, right):
    if left > right:
        return False

    mid = (left + right) // 2

    if arr[mid] == target:
        return True

    if arr[mid] < target:
        return bs(arr, target, mid + 1, right)

    return bs(arr, target, left, mid - 1)


def binary_search(arr: list[int], target: int) -> bool:
    return bs(arr, target, 0, len(arr) - 1)


def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 5) == True
    assert binary_search([1, 2, 3, 4, 5], 6) == False
    assert binary_search([], 3) == False
    assert binary_search([10], 10) == True
    assert binary_search([10], 5) == False
    assert binary_search([1, 3, 5, 7, 9, 11], 1) == True
    assert binary_search([1, 3, 5, 7, 9, 11], 11) == True
    assert binary_search([1, 3, 5, 7, 9, 11], 4) == False

    print("All tests passed!")


test_binary_search()
