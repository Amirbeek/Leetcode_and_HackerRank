from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: TreeNode = None
        self.right: TreeNode = None


def is_leaf(node):
    return not node.left and not node.right


def count_leaves_dfs(root: TreeNode) -> int:
    # DFS (Depth First Search)
    if not root:
        return 0

    if is_leaf(root):
        return 1

    return count_leaves_dfs(root.left) + count_leaves_dfs(root.right)


def count_leaves_bfs(root: TreeNode) -> int:
    # BFS (Breadth First Search)
    if not root:
        return 0

    total = 0
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if is_leaf(curr):
            total += 1
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
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
    print("BFS leaf count:", count_leaves_bfs(root))  # Output: 3

test()
