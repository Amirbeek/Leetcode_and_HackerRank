def maximumCount(nums):
    pos = len(nums) - BS(nums, 1)  # count of positives
    neg = BS(nums, 0)  # count of negatives
    return max(pos, neg)


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


print(maximumCount([-3, -2, -1, 0, 0, 1, 2]))
# print(maximumCount([-2, -1, -1, 1, 2, 3]))
