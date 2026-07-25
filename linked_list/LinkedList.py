"""This is my implementation of a linked list. It appened to the end like a queue."""


class Node:
    """Node to a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def list(self) -> None:
        """Returns a list of the elements in the linked list."""
        if self.head is None:
            return []
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result

    def pop(self) -> Node | None:
        if self.head is None:
            return
        result = self.head
        self.head = self.head.next
        return result.data


class LinkedListQueue(LinkedList):
    """Linked List, appened to the end of the list."""

    def __init__(self):
        self.head = None

    def append(self, value) -> None:
        """Append to the right or end of the list."""
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current:
            if current.next is None:
                current.next = Node(value)
                return
            current = current.next


class LinkedListStack(LinkedList):
    """Linked list as a stack."""

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
