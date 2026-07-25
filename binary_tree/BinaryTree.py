"""Binary Tree."""


class Node:
    """Node to Binary Tree."""

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def traverse(self) -> None:
        print(self.data, end=" ")
        if self.left:
            self.left.traverse()
        if self.right:
            self.right.traverse()


class BinaryTree:
    """Binary Tree implementation."""

    def __init__(self):
        self.root = None

    def append(self, value):
        """Append new values to the left or right, lesser is left and vise versa."""
        if self.root is None:
            self.root = Node(value)
            return
        current_leaf = self.root
        while current_leaf:
            if value == current_leaf.data:
                return
            if value < current_leaf.data:
                if current_leaf.left is None:
                    current_leaf.left = Node(value)
                    return
                current_leaf = current_leaf.left
                continue
            if current_leaf.right is None:
                current_leaf.right = Node(value)
                return
            current_leaf = current_leaf.right

    def traverse(self) -> None:
        """Recursive printing traversal."""
        self.root.traverse()

    def locate(self, value) -> int:
        if self.root is None:
            return
        current_leaf = self.root
        depth = 0
        while current_leaf:
            if value == current_leaf.data:
                return depth
            if value < current_leaf.data:
                if current_leaf.left:
                    current_leaf = current_leaf.left
                    depth += 1
                    continue
                return 0
            if current_leaf.right:
                current_leaf = current_leaf.right
                depth += 1
                continue
            return 0
