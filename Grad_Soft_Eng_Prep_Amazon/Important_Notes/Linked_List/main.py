class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def print_element(head: Node) -> None:
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


def find_middle(head: Node) -> None:
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    print(slow.val)


def reverse_list(head: Node) -> None:
    prev = None
    curr = head

    while curr is not None:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_

    return prev


def remove_node(head: Node, target: int)-> None:
    curr = head
    prev = None

    while curr is not None:
        next_ = curr
        if curr.val == target:
            curr.next = prev
            return next_
        prev = curr
        curr = curr.next





# 🧪 Build a longer linked list: 1 → 2 → 3 → 4 → 5 → 6
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(6)

# Linking them together
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven

head = one

# ✅ Print the full linked list
# print_element(head)
# reversed_head = reverse_list(head)
print("\nDeleted List:")
insert_val(head, 5)