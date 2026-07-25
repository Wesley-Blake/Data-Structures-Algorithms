from linked_list.LinkedList import LinkedList, LinkedListQueue, LinkedListStack


# LinkedList
def test_class_list():
    test = LinkedList()
    assert isinstance(test, LinkedList)


def test_pop_empty():
    test = LinkedList()
    assert test.pop() is None


def test_pop_head():
    test = LinkedListQueue()
    test.append(1)
    assert test.pop() == 1


# LinkedListQueue
def test_class_queue():
    test = LinkedListQueue()
    assert isinstance(test, LinkedListQueue)


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
    assert test.list() == test_case


# LinkedListStack
def test_class_stack():
    test = LinkedListStack()
    assert isinstance(test, LinkedListStack)


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
    assert test.list() == test_case
