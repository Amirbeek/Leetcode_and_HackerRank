# def sort_arr(arr: list[int]) -> list:


def applyOperations(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    is_zero = 0
    for i in range(len(nums)):
        if i + 1 != len(nums) and nums[i] == nums[i + 1] :
            print(i, i+1, len(nums))
            nums[i], nums[i + 1] = nums[i] * 2, 0
        if nums[i] != 0:
            nums[i], nums[is_zero] = nums[is_zero], nums[i]
            is_zero += 1

    return nums
# print(applyOperations([1,2,2,1,1,0].s))
from collections import defaultdict


def addedInteger(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    num1 = sorted(nums1)[0]
    num2 = sorted(nums2)[0]
    result = num1 - num2
    return result


# print(addedInteger([2,6,4],[9,7,5]))


def longestPalindrome(words):
    basket = defaultdict()
    unpaired = ans = 0
    for w in words:
        if w[0] == w[1]:
            if basket[w] > 0:
                unpaired -= 1
                basket[w] -= 1
                ans += 4
            else:
                basket[w] += 1
                unpaired += 1
        else:
            if basket[w[::-1]] > 0:
                ans += 4
                basket[w[::-1]] -= 1
            else:
                basket[w] += 1
    if unpaired > 0:
        ans += 2

    return ans

    # print([words[0][::-1] in words[1::]])


# longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"])
# longestPalindrome(["lc", "cl", "gg"])

def longestPalindrome(s: str):
    basket = set()
    result = 0
    for char in s:
        if char in basket:
            basket.remove(char)
            result += 2
        else:
            basket.add(char)

    if basket:
        result +=1

    return result


print(longestPalindrome("bananas"))
