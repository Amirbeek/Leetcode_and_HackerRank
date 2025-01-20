def twoSum(nums, target):
    my_map = {}
    for i, n in enumerate(nums):
        pov = target - n
        if pov in my_map:
            return [my_map[pov], i]
        my_map[n] = i
    return []

print(twoSum([2, 7, 11, 15], 9))

# Output: [0, 1]
