from typing import Iterable


def marge_two(arr1: list[int], arr2: list[int]) -> Iterable[int]:
    n = m = 0
    i, j = len(arr1), len(arr2)
    while n < i and m < j:
        if arr1[n] < arr2[m]:
            yield arr1[n]
            n += 1
        else:
            yield arr2[m]
            m += 1

        while n < i:
            yield arr1[n]
            n += 1
        while m < j:
            yield arr2[m]
            m += 1


print(marge_two([2, 3, 5], [1, 3, 6]))
