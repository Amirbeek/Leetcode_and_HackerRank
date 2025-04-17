from collections import deque
def isValid(s: str) -> bool:
    stack = []
    bas = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    for char in s:
        if char in bas:
            if stack and stack[-1] == bas[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return False if stack else True


def maxProfit(prices: list[int]) -> None:
    l = 0
    r = 1
    maxPro = 0
    while r < len(prices):
        profit = prices[r] - prices[l]
        if profit > 0:
            maxPro += profit
        l += 1
        r += 1
    return maxPro


def majorityElement(nums: list[int]) -> int:
    bas = {}
    res = 0
    majority = 0
    for num in nums:
        bas[num] = 1 + bas.get(num, 0)
        if bas[num] > majority:
            res = num
            majority = bas[num]
    return res


# def decodeString( s: str) -> str:
#     result = ''
#     stack = []
#     i =0
#     while i < len(s):
#         if s[i] != "]":
#             stack.append(s[i])
#         else:




# print(decodeString("3[a]2[bc]"))
# print(maxProfit([7, 1, 5, 3, 6, 4]))
# print(isValid("(("))
