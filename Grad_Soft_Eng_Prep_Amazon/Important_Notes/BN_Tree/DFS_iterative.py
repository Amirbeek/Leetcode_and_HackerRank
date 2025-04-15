from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: TreeNode = None
        self.right: TreeNode = None


def count_leaves_dfs(root: TreeNode) -> int:
    stack = []
    curr = root
    total = 0
    while stack or curr:
        while curr:
            total += 1
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        curr = curr.right

    return total

def test():
    # Building the following tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("DFS leaf count:", count_leaves_dfs(root))  # Output: 3
    # print("BFS leaf count:", count_leaves_bfs(root))  # Output: 3


test()


def minimal_distance(distances, k):
    # Edge case: if k is greater than the length of the array, return -1 (invalid case)
    if k > len(distances):
        return -1

    # Calculate the sum of the first 'k' elements (initial window)
    current_sum = sum(distances[:k])
    min_sum = current_sum

    # Slide the window across the array
    for i in range(k, len(distances)):
        # Add the next element and remove the first element of the previous window
        current_sum += distances[i] - distances[i - k]
        min_sum = min(min_sum, current_sum)

    return min_sum


# Example usage
distances = [1, 3, 5, 2, 8, 7]
k = 3
print(minimal_distance(distances, k))  # Output: 9

