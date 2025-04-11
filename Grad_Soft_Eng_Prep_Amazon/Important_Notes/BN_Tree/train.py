from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: TreeNode = None
        self.right: TreeNode = None





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

    # print("DFS leaf count:", count_leaves_dfs(root))  # Output: 3
    # print("BFS leaf count:", count_leaves_bfs(root))  # Output: 3


test()
