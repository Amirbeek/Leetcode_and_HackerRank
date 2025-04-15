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

    def remove(self, value):
        if not self.root:
            return False

        curr = self.root
        parr = None

        # Search for the node to delete
        while curr:
            if value < curr.val:
                parr = curr
                curr = curr.left
            elif value > curr.val:
                parr = curr
                curr = curr.right
            else:
                # Node with the value is found
                if not curr.left and not curr.right:  # Case 1: No children
                    if parr:  # If parent exists, update parent's pointer to None
                        if parr.left == curr:
                            parr.left = None
                        else:
                            parr.right = None
                    else:
                        self.root = None  # If the node to remove is the root
                elif not curr.left:  # Case 2: Only right child
                    if parr:
                        if parr.left == curr:
                            parr.left = curr.right
                        else:
                            parr.right = curr.right
                    else:
                        self.root = curr.right  # If the node to remove is the root
                elif not curr.right:  # Case 3: Only left child
                    if parr:
                        if parr.left == curr:
                            parr.left = curr.left
                        else:
                            parr.right = curr.left
                    else:
                        self.root = curr.left  # If the node to remove is the root
                else:  # Case 4: Two children
                    # Find the smallest node in the right subtree (in-order successor)
                    succ_parent = curr
                    succ = curr.right
                    while succ.left:
                        succ_parent = succ
                        succ = succ.left

                    # Replace current node's value with successor's value
                    curr.val = succ.val

                    # Now delete the in-order successor (it will have at most one child)
                    if succ_parent.left == succ:
                        succ_parent.left = succ.right
                    else:
                        succ_parent.right = succ.right
                return True  # Successfully removed node
        return False  # Value not found

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

    def breadthFirstSearch(self):
        if not self.root:
            return []
        curr = self.root
        lists = []
        queue = deque([curr])
        while len(queue) > 0:
            curr = queue.popleft()
            lists.append(curr.val)
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
        return lists

    def breadthFirstSearchR(self, queue, lists):
        if len(queue) == 0:
            return lists
        curr = queue.popleft()

        lists.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

        return self.breadthFirstSearchR(queue, lists)

    def levelOrder(self, root) -> list[int]:
        result = []
        i = 0

        def BFS(root):
            nonlocal i, result
            if len(root):
                return result
            curr = root.popleft()
            if curr:
                result[i].append(curr.val)
                root.append(curr.left)
                root.append(curr.right)
            return BFS(root)

        BFS(deque([self.root]))
        return result

    def DFSInorder(self):
        return traverseInOrder(self.root, [])

    def DFSPostOrder(self):
        return traversePoOrder(self.root, [])

    def DFSPreOrder(self):
        return traversePreOrder(self.root, [])

    def isValidBST(self, root) -> bool:
        if not root:
            return False
        curr = root
        queue = deque([curr])
        v = []
        while len(queue) > 0:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
                v.append(curr.val)
            else:
                v.append(None)
            if curr.right:
                queue.append(curr.right)
                v.append(curr.val)
            else:
                v.append(None)
        print(v)

    def isBalanced(self, root):
        if root is None: return 0

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        if left is None and right is None:
            return 0

        if left is None:
            return 1 + right

        if right is None:
            return 1 + left

        print(left, right)
        return


def traverseInOrder(node, list):
    if node:
        traverseInOrder(node.left, list)
        list.append(node.val)
        traverseInOrder(node.right, list)

    return list


def traversePreOrder(node, list):
    if node:
        list.append(node.val)
        traverseInOrder(node.left, list)
        traverseInOrder(node.right, list)

    return list


def traversePoOrder(node, list):
    if node:
        traverseInOrder(node.left, list)
        traverseInOrder(node.right, list)
        list.append(node.val)
    return list