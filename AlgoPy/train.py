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


print(maxProfit([7, 1, 5, 3, 6, 4]))
# print(isValid("(("))
