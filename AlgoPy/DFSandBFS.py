from collections import deque


class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
        else:
            curr = self.root
            while True:
                if value < curr.val:
                    # Left
                    if not curr.left:
                        curr.left = newNode
                        break
                    curr = curr.left
                else:
                    # Right
                    if not curr.right:
                        curr.right = newNode
                        break
                    curr = curr.right
        return self

    def isBalanced(self):
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(self.root) != -1

    def bfs(self):

        result = []
        que = deque([self.root])
        while len(que) > 0:
            curr = que.popleft()
            result.append(curr.val)

            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)

        return result


# Testing the tree
bt = BinaryTree()
bt.insert(5).insert(1).insert(4).insert(3).insert(6)
print(bt.isBalanced())