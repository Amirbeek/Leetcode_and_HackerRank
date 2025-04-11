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
