def np(nums: list):
    for i in range(len(nums) - 4):  # limit to avoid out-of-range
        index = nums[i + 1]
        if index < len(nums):
            print(nums[index])
        else:
            print(f"Index {index} out of range")


np([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
