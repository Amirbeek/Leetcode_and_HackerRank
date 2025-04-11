def two_sum(arr:list[int], target: int)-> bool:
    sum_hash = dict()
    for num in arr:
        if num - target in sum_hash:
            return True
        else:
            sum_hash[num] = 1

    return False


def twoSum(nums, target):
        my_map = {}
        for i, n in enumerate(nums):
            pov = target - n
            if pov in my_map:
                return [my_map[pov], i]

            else:
                my_map[n] = i

        return []

print(twoSum([1,4,5,2], 3))
print(two_sum([1,4,5,2], 8))