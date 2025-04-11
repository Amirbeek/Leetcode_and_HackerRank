from collections import defaultdict, Counter


def build_counter(word):
    counter = defaultdict()
    for char in word:
        counter[char] += 1
    return counter


# Solution one

# def is_anagram(word1: str, word2: str) -> bool:
#     counter1 = Counter(word1)
#     counter2 = Counter(word2)
#     return counter1 == counter2

# Solution two

# def is_anagram(word1: str, word2: str) -> bool:
#     counter1 = Counter(word1)
#     for char in word2:
#         counter1[char] -= 1
#     for val in counter1.values():
#         if val != 0:
#             return False
#     return True

# Solution three
def is_anagram(word1: str, word2: str) -> bool:
    counter = Counter(word1)
    for char in word2:
        counter[char] -= 1
    return all(val == 0 for val in counter.values())


# ✅ Testing
print(is_anagram("listen", "silent"))  # True
print(is_anagram("triangle", "integral"))  # True
print(is_anagram("apple", "pale"))  # False
print(is_anagram("rat", "car"))  # False
