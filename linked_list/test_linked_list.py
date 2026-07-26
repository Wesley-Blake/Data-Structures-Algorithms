import pytest

from linked_list.LinkedList import (
    LinkedListDouble,
    LinkedListQueue,
    LinkedListStack,
)


# LinkedList tests as a LinkedListQueue
def test_contains_queue():
    test = LinkedListQueue()
    test.append(1)
    assert 1 in test


def test_contains_queue_head_is_none():
    test = LinkedListQueue()
    assert (1 in test) == False


def test_not_contains_queue():
    test = LinkedListQueue()
    test.append(1)
    assert 2 not in test


def test_next():
    test = LinkedListQueue()
    test.append(1)
    assert next(test) == 1


def test_next_empty():
    with pytest.raises(StopIteration):
        test = LinkedListQueue()
        next(test)


def test_queue_pop_empty():
    test = LinkedListQueue()
    assert test.pop() is None


def test_queue_pop_multiple():
    test = LinkedListQueue()
    test.append(1)
    test.append(2)
    test.append(3)
    assert test.pop() == 1


def test_queue_list():
    test_case = [1, 2, 3, 4]
    test = LinkedListQueue()
    for i in test_case:
        test.append(i)
    assert test.as_list() == test_case


def test_queue_list_empty():
    test = LinkedListQueue()
    assert test.as_list() == []


# LinkedListStack
def test_next_stack():
    test = LinkedListStack()
    test.append(1)
    test.append(2)
    test.append(3)
    test.append(4)
    assert next(test) == 4
    assert next(test) == 3


def test_stack_pop_multiple():
    test = LinkedListStack()
    test.append(1)
    test.append(2)
    test.append(3)
    assert test.pop() == 3


def test_stack_list():
    test_case = [1, 2, 3, 4]
    test = LinkedListStack()
    for i in test_case:
        test.append(i)
    test_case.reverse()
    assert test.as_list() == test_case


# LinkedListDouble
def test_double_append_next():
    test = LinkedListDouble()
    test.append(1)
    assert test.head.next_node is None


def test_double_append_previous():
    test = LinkedListDouble()
    test.append(1)
    assert test.head.previous is None


def test_double_append_multiple():
    test = LinkedListDouble()
    test.append(1)
    test.append(2)
    test.append(3)
    test.append(4)
    assert test.head.next_node is not None


def test_previous():
    test = LinkedListDouble()
    test.append(1)
    test.append(2)
    test.append(3)
    test.append(4)
    current = test.head.next_node
    test_int = 4
    while current:
        assert current.previous.data == test_int
        test_int -= 1
        current = current.next_node
