class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val: int):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")


def merge_sorted_lists(l1: Node, l2: Node) -> Node :
    dummy = Node(-1)
    tail = dummy
    while l1 and l2 is not None:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1 is not None:
        tail.next = l1
    if l2 is not None:
        tail.next = l2

    return dummy.next


# Example usage:
if __name__ == "__main__":
    # First sorted list
    list1 = LinkedList()
    for val in [1, 3, 5, 8,19]:
        list1.append(val)

    # Second sorted list
    list2 = LinkedList()
    for val in [2, 4, 6]:
        list2.append(val)

    print("List 1:")
    list1.print_list()
    print("List 2:")
    list2.print_list()

    # Merge and print result
    merged_head = merge_sorted_lists(list1.head, list2.head)

    print("Merged List:")
    cur = merged_head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")
