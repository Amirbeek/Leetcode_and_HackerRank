# def twoSum(nums, target):
#     my_map = {}
#     for i, n in enumerate(nums):
#         current = target - n
#         if current in my_map:
#             return [my_map[current], i]
#         my_map[n] = i
#     return []
# print(twoSum([2, 7, 11, 15], 9))
#
#
# def isHappy(num):
#     my_set = set()
#     current = num
#     while current not in my_set:
#         my_set.add(current)
#         sums = 0
#         for n in str(current):
#             sums += int(n) ** 2
#         if sums == 1: return True
#         current = str(sums)
#
#     return False
#
# print(isHappy(2))
# print(isHappy(19))
#
# from collections import Counter
#
#
# def findScore(userID1, userID2, p):
#     countUserID2 = Counter(userID2)
#     user2_len = len(userID2)
#     user1_len = len(userID1)
#
#     max_len = (user2_len - 1) * p + 1
#
#     result = 0
#     for start in range(p):
#         if start + (user2_len - 1) * p >= user1_len:
#             break
#
#         currentCount = Counter()
#         for j in range(start, start + max_len, p):
#             if j >= user1_len:
#                 break
#             currentCount[userID1[j]] += 1
#
#         if currentCount == countUserID2:
#             result += 1
#
#         for j in range(start + p, user1_len, p):
#             if j + (user2_len - 1) * p >= user1_len:
#                 break
#
#             eChar = userID1[j - p]
#             currentCount[eChar] -= 1
#             if currentCount[eChar] == 0:
#                 del currentCount[eChar]
#             nChar = userID1[j + (user2_len - 1) * p]
#             currentCount[nChar] += 1
#             if currentCount == countUserID2:
#                 result += 1
#
#     return result


# # def findMedian(arr):
# #     # Write your code here
# #     sorted_arr = sorted(arr)
#     print(arr)
# #     return sorted_arr[int(len(arr)/2)]
# #
#  print(findMedian([0 ,1 ,2 ,4 ,6 ,5 ,3]))
#
#
#
#
# def single_num(num):
#     numbers = {}
#     for n in num:
#         if n in numbers:
#             numbers[n] += 1
#         else:
#             numbers[n] = 1
#
#
# print(single_num([4, 1, 2, 1, 2]))


