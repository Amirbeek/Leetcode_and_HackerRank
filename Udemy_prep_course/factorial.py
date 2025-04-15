# def factorial_recursive(num: int) -> int:
#     return num * factorial_recursive(num - 1) if num > 0 else 1


# def factorial_Iterative(num: int):
#     if num <= 1:
#         return num
#
#     result = num
#
#     while num > 2:
#         result = result * (num - 1)
#         num -= 1
#
#     return result
#
#
# print(factorial_Iterative(3))
#
# print(factorial_recursive(3))


# def fibonacciIterative(n):
#     arr = [0,1]
#     for i in range(2, n):
#         arr.push([arr[i-2] + arr[i-1]])
#     return arr[n]
#
#
# def fibonacciRecursive(n):
#     if n < 2:
#         return n
#     return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
#
#
# print(fibonacciRecursive(40))

import numpy as np





arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = mergeSort(arr)
print("Sorted array:", sorted_arr)

