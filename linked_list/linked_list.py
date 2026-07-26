"""Implementation of a singly linked list and related list variants."""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    """Represent a node in a singly linked list."""

    data: None | Any = None
    next_node: None | Node = None


class LinkedList(ABC):
    """Base implementation for linked-list behavior."""

    def __contains__(self, value) -> bool:
        """Return True when the value is present in the list."""
        if self.head is None:
            return False
        current = self.head
        while current:
            if value == current.data:
                return True
            current = current.next_node
        return False

    def __next__(self) -> Any:
        """Return the next item from the list or raise StopIteration."""
        result = self.pop()
        if result is None:
            raise StopIteration
        return result

    def pop(self) -> Any:
        """Remove and return the value at the head of the list."""
        if self.head is None:  # pylint: disable=access-member-before-definition
            return
        result = self.head  # pylint: disable=access-member-before-definition
        self.head = self.head.next_node  # pylint: disable=attribute-defined-outside-init
        return result.data

    def as_list(self) -> list:
        """Return the linked list contents as a Python list."""
        if self.head is None:
            return []
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next_node
        return result


class LinkedListQueue(LinkedList):
    """Linked list that appends values to the end of the list."""

    def __init__(self):
        """Initialize an empty queue-backed linked list."""
        self.head = None

    def append(self, value) -> None:
        """Append a value to the end of the list."""
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current:
            if current.next_node is None:
                current.next_node = Node(value)
                return
            current = current.next_node


class LinkedListStack(LinkedList):
    """Linked list used as a stack."""

    def __init__(self):
        """Initialize an empty stack-backed linked list."""
        self.head = None

    def append(self, value):
        """Push a value onto the front of the list."""
        if self.head is None:
            self.head = Node(value)
            return
        temp = self.head
        self.head = Node(value)
        self.head.next_node = temp


@dataclass
class NodeDouble(Node):
    """Represent a node in a doubly linked list."""

    previous: None | NodeDouble = None


class LinkedListDouble(LinkedList):
    """A doubly linked list used as a stack."""

    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None

    def append(self, value) -> None:
        """Push a value onto the front of the doubly linked list."""
        if self.head is None:
            self.head = NodeDouble(value)
            return
        temp = self.head
        self.head = NodeDouble(value)
        self.head.next_node = temp
        self.head.next_node.previous = self.head  # pylint: disable=attribute-defined-outside-init
