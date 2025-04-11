def sum_recursive(nums: list[int]) -> int:
    if not len(nums):
        return 0

    return nums.pop() + sum_recursive(nums)


# print(sum_recursive([1, 3, 5, 6, 7]))

def reverse_recursive(word: str) -> str:
    if word == "":
        return word
    reversed_str = reverse_recursive(word[1:])

    return reversed_str + word[0]


def reverse_str(word: str) -> str:
    return word[::-1]


print(reverse_recursive('amir'))
print(reverse_str('amir'))
