import math


def print_digits(num: int):
    result = 0
    while num != 0:
        result *= 10
        digits = num % 10
        result += digits
        num //= 10

    return result


# print(print_digits(45))


def is_palindrome(num: int) -> bool:
    result = 0
    original = num

    while num != 0:
        result *= 10
        digit = num % 10
        result += digit
        num //= 10

    return result == original


# Test
# print(is_palindrome(121))  # True
# print(is_palindrome(102))  # False
# print(is_palindrome(4884))  # True

def digital_root(num: int) -> int:
    while num >= 10:
        result = 0
        while num > 0:
            digit = num % 10
            result += digit
            num //= 10
        num = result
    return num


# print(digital_root(999))

def convert_to_binary(num: int) -> str:
    result = ""
    while num != 0:
        digit = num % 2
        result += str(digit)
        num //= 2

    return result[::-1]


# print(convert_to_binary(60))


def is_power_two(num: int) -> bool:
    bit_count = 0
    while num != 0:
        bit_count += num & 1
        num = num >> 1

    return bit_count == 1


def N_Root(n):
    return math.factorial(n)


# print(N_Root(3))


def first_count(k, target):
    return k % (target + 1)


def sum_of_odd_numbers(n) -> int:
    return 3


def is_palindrome(word: str):
    low, high = 0, len(word) - 1
    while low < high:
        if word[low] != word[high]:
            return False
        low += 1
        high -= 1

    return True


# print(is_palindrome('ama'))
# print(is_palindrome('ami'))


def merge_two_arrays(arr1: list[int], arr2: list[int]):
    i = j = 0
    n, m = len(arr1), len(arr2)
    result = []
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < n:
        result.append(arr1[1])
        i += 1

    while j < m:
        result.append(arr2[j])
        j += 1

    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid]
    return merge_two_arrays(
        merge_sort(left),
        merge_sort(right)
    )


print(merge_two_arrays([2, 3, 5], [1, 3, 6]))
