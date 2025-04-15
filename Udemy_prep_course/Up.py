class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.len = 0

    def peek(self):
        if self.len is 0:
            return "Stack is Empty"
        return self.top

    def push(self, val):
        newStack = Node(val)
        if self.len == 0:
            self.top = newStack
            self.bottom = self.top
        else:
            newStack.next = self.top
            self.top = newStack
        self.len += 1
        return newStack

    def pop(self):
        if self.len < 1:
            self.top = None
        self.len -= 1
        next_note = self.top
        self.top = self.top.next
        if self.len == 0:
            self.bottom = None

        return next_note


class Queue:
    def __init__(self, value):
        self.first = None
        self.last = None
        self.len = 0

    def peek(self):
        if self.len == 0:
            return "Sorry The Queue is empty"
        return self.first

    def enqueue(self, val):
        newNode = Node(val)
        if self.len == 0:
            self.first = newNode
            self.last = self.first
        else:
            self.last.next = newNode
            self.last = newNode

        self.len += 1

    def dequeue(self):
        if not self.first:
            return "Sorry The Queue is empty"

        removed_Node = self.first
        self.first = self.first.next

        if self.len == 0:
            self.last = None
        return removed_Node









