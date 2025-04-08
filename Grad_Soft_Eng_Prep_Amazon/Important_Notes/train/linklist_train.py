class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def print_list(head: Node):
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


def remove_node(head: Node, target):
    curr = head
    prev = None
    if curr and curr.val == target:
        head = curr.next
        return head

    while curr is not None:
        if curr.val == target:
            prev.next = curr.next
            return head
        prev = curr
        curr = curr.next

    return head


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

removed = remove_node(head, 6)

print(print_list(removed))









