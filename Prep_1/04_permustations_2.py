import itertools

nums = [1,1,2]
def permute(nums):
    if len(nums) == 1: return [nums]
    list_permutations = list(itertools.permutations(nums))
    sorted_per = set()
    for perm in list_permutations:
        if perm not in sorted_per:
            sorted_per.add(perm)
    answer = [list(per) for per in sorted_per]
    return answer

print(permute(nums))