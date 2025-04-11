def BS(nums, target):
    left = 0
    right = len(nums) - 1
    result = len(nums)


    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            result = mid
            right = mid - 1
    return result


def countNegatives(grid):
    result = 0
    for arr in grid:
        reversed_ls = arr.reverse()
        print('reversed list: ', reversed_ls)
        result += BS(reversed_ls, 0)
    return result


print(countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
