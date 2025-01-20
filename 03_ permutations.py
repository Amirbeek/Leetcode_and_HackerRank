import itertools

nums = [1,1,2]
def permute(nums):
    if len(nums) == 1: return [nums]
    list_permutations = list(itertools.permutations(nums))
    ans_permutations = [list(per) for per in list_permutations]
    return ans_permutations

print(permute(nums))