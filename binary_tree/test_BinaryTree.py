from secrets import choice

from binary_tree.BinaryTree import BinaryTree


def test_class():
    test = BinaryTree()
    assert isinstance(test, BinaryTree)


def test_append():
    test = BinaryTree()
    test_case = [i for i in range(10)]
    for i in range(len(test_case)):
        test.append(choice(test_case))


def test_print():
    test = BinaryTree()
    test_case = [i for i in range(10)]
    for i in range(len(test_case)):
        test.append(choice(test_case))
    test.traverse()


def test_locate():
    test = BinaryTree()
    test_case = [i for i in range(10)]
    for i in range(len(test_case)):
        test.append(choice(test_case))
    assert test.locate(2) is not None


def test_locate_depth():
    test = BinaryTree()
    test_case = [i for i in range(10)]
    for i in test_case:
        test.append(i)
    assert test.locate(2) == 2
