def searchRange(nums, target):
    if len(nums) == 0: return []
    answer = []
    low = 0
    high = len(nums) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] < target:
            low = mid + 1

        elif nums[mid] > target:
            high = mid - 1

        else:
            answer.append(nums[mid].index(target))

    return answer


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))