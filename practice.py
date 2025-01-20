def twoSum(nums, target):
    my_map = {}
    for i, n in enumerate(nums):
        current = target - n
        if current in my_map:
            return [my_map[current], i]
        my_map[n] = i
    return []
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]


def isHappy(num):
    my_set = set()
    current = num
    while current not in my_set:
        my_set.add(current)
        sums = 0
        for n in str(current):
            sums += int(n) ** 2
        if sums == 1: return True
        current = str(sums)

    return False

print(isHappy(2))
print(isHappy(19))