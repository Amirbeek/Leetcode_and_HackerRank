# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if not head or not head.next:
#             return head
#         # Step 1: Find the length of the list
#         lenght = self.find_len(head)
#
#         # Step 2: Compute the effective rotation count
#         n = k % lenght
#
#         # Step 3: If the head is 0 , we should returl head
#         if n == 0:
#             return head
#         # Step 4: Find a tail and connect it to head
#         tail = head
#         while tail.next:
#             tail = tail.next
#         tail.next = head  # We are making it a circular linked list
#
#         # Step 5: Find new Tail
#         new_tail = head
#         for i in range(lenght - n - 1):
#             new_tail = new_tail.next
#
#         # Step 5: Create new Head
#         new_head = new_tail.next
#         new_tail.next = None
#
#         return new_head
#
#     def find_len(self, head: ListNode) -> int:
#         lenght = 0
#         while head:
#             head = head.next
#             lenght += 1
#         return lenght

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    my_hash = {}
    for i, num in enumerate(nums):
        if num in my_hash and my_hash[num] - i <= k:
            return True
        else:
            my_hash[num] = i
    return False


print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
print(containsNearbyDuplicate([1, 2, 3, 1], 3))
print(containsNearbyDuplicate([1], 1))
print(containsNearbyDuplicate([1, 0, 1, 1], 1))
