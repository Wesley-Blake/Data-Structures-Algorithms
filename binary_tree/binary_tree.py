"""Binary tree implementation with a simple node class."""


class Node:
    """Represent a node in a binary tree."""

    def __init__(self, value):
        """Initialize a node with the provided value."""
        self.data = value
        self.left = None
        self.right = None

    def traverse(self) -> None:
        """Print the node and its subtree in preorder traversal."""
        print(self.data, end=" ")
        if self.left:
            self.left.traverse()
        if self.right:
            self.right.traverse()


class BinaryTree:
    """Binary tree implementation with sorted insertion behavior."""

    def __init__(self):
        """Initialize an empty binary tree."""
        self.root = None

    def __contains__(self, value) -> bool:
        """Return True when the value exists in the tree."""
        return isinstance(self.locate(value), int)

    def append(self, value) -> None:
        """Insert a value into the tree, placing smaller values to the left."""
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
        """Print the contents of the tree using preorder traversal."""
        self.root.traverse()

    def locate(self, value) -> int | None:
        """Return the depth of the value if it exists, otherwise None."""
        if self.root is None:
            return
        current_leaf = self.root
        depth = 0
        while current_leaf:
            if value == current_leaf.data:
                return depth
            if value < current_leaf.data:
                current_leaf = current_leaf.left
                depth += 1
                continue
            current_leaf = current_leaf.right
            depth += 1
            continue
        return
