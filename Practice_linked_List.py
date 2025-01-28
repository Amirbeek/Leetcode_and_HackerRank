class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def printList(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def get_head(self):
        return self.head
    def findMiddle(self):
        fast = slow = self.head
        if not self.head:
            print("The list is empty.")
            return
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Middle:", slow.val)

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        self.head = prev

    def reverseBetween(self, left, right):
        if left == right:
            return

        prev = None
        curr = self.head
        pos = 1
        while pos < left:
            prev = curr
            curr = curr.next
            pos += 1

        tail = curr
        con = prev
        while pos <= right:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
            pos += 1

        if con:
            con.next = prev
        else:
            self.head = prev

        tail.next = curr
        return self

    def detectCycle(self, head):
        slow = head
        fast = head
        poss = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            poss += 1
            if slow == fast:
                return poss

        return -1
n = LinkedList()
n.append(1)
n.append(3)
n.append(2)
n.append(4)
# n.append(6)
# n.append(6)
# n.reverse()
# print(n.get_head())
# n.reverseBetween( 2, 5)
n.findMiddle()


