class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.len += 1
        return self.tail

    def push(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.len += 1
        return self.head

    def remove(self, index: int):
        if index > self.len or index < 0:
            return False
        prev = None
        curr = self.head
        s = 0
        while True:
            if s is index:
                rtv = curr
                curr = curr.next
                prev.next = curr
                return rtv
            else:
                s += 1
                prev = curr
                curr = curr.next

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.tail = self.head
        self.head = prev

    def insert(self, index, value):
        if index < 0 or index > self.len:
            return False

        new_node = Node(value)

        if index == 0:
            self.push(value)
        elif index == self.len:
            self.append(value)
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

        self.len += 1
        return True


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.insert(0, 50)
# ll.push(50)
# ll.remove(1)
# ll.reverse()

# Print the list
current = ll.head
# while current:
#     print(current.val)
#     current = current.next


def task(nums: list[int]) -> int:
    basket = dict()
    for num in nums:
        if num in basket:
            return num
        else:
            basket[num] = True
    return None


def rotate(nums: list[int], k: int):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]



print(rotate([2, 1, 1, 2, 3, 5, 1, 2, 4], 1))
