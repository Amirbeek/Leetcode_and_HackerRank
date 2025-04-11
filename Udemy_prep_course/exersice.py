def task(nums: list[int]) -> int:
    basket = dict()
    for num in nums:
        if num in basket:
            return num
        else:
            basket[num] = True
    return None


print(task([2, 1, 1, 2, 3, 5, 1, 2, 4]))
