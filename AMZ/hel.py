import re
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


# print(topKFrequent(nums=[1, 2, 2, 3, 3, 3], k=1))


def isPalindrome(s: str) :
    s = re.sub(r"[^\w]", "", s).lower()

    start = 0
    end = len(s) - 1
    print(s)
    while start < end:
        if s[start] != s[end]:
            return False
        if start != end or start + 1 == end -1:
            start += 1
            end -= 1
    return True


print(isPalindrome("No lemon, no melon"))


