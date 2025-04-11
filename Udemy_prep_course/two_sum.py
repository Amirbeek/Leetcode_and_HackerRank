# Solution 1
# [1, 4, 5, 2] t = 9
# 1 ,2, 4 O(n^2)

# Solution 2
"""{
    1: True,
    4: True,

}"""

# Solution 2
# [1, 4, 5, 2] t = 9
#  9-1 = 8 O(N)

twoSum = [1, 4, 5, 2]


def TwoSum(nums: list[int], target: int) -> list:
    basket = dict()
    for num in nums:
        t = target - num
        if t in basket:
            yield [t, num]
            break
        basket[num] = 1


print(list(TwoSum(twoSum, 6)))
