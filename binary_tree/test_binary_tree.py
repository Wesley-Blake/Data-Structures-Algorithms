from secrets import choice

from binary_tree.BinaryTree import BinaryTree


def test_class():
    test = BinaryTree()
    assert isinstance(test, BinaryTree)


def test_append():
    test = BinaryTree()
    test_case = [i for i in range(10)]
    for i in range(len(test_case)):
        assert test.append(choice(test_case)) is None


def test_print():
    test = BinaryTree()
    test_case = [i for i in range(10_000)]
    test.append(5_000)
    for i in range(10_000):
        test.append(choice(test_case))
    test.traverse()


def test_locate():
    test = BinaryTree()
    test_case = [i for i in range(10)]
    for i in range(len(test_case)):
        test.append(choice(test_case))
    test.append(2)
    assert test.locate(2) is not None


def test_locate_head_is_none():
    test = BinaryTree()
    assert test.locate(1) is None


def test_locate_depth_left():
    test = BinaryTree()
    test.append(50)
    test.append(1)
    test.append(100)
    assert 1 in test


def test_locate_depth_left_not_in():
    test = BinaryTree()
    test.append(50)
    test.append(1)
    test.append(100)
    assert (2 in test) == False


def test_locate_depth_right():
    test = BinaryTree()
    test.append(50)
    test.append(1)
    test.append(100)
    assert 100 in test


def test_locate_depth_right_not_in():
    test = BinaryTree()
    test.append(50)
    test.append(1)
    test.append(100)
    assert (56 in test) == False
