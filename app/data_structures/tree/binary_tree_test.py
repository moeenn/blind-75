from unittest import TestCase
from .binary_tree import BinaryTree, Node, TraverseOrder


class TestBinaryTree(TestCase):
    def test_normal_operations(self) -> None:
        """
                10
            20      30
        40    50  60   70
        """
        root = Node[int](
            data=10,
            left=Node(
                data=20,
                left=Node(data=40, left=None, right=None),
                right=Node(data=50, left=None, right=None),
            ),
            right=Node(
                data=30,
                left=Node(data=60, left=None, right=None),
                right=Node(data=70, left=None, right=None),
            ),
        )
        tree = BinaryTree[int](root)

        result = tree.traverse(TraverseOrder.InOrder)
        self.assertEqual(list(result), [40, 20, 50, 10, 60, 30, 70])

        result = tree.traverse(TraverseOrder.PreOrder)
        self.assertEqual(list(result), [10, 20, 40, 50, 30, 60, 70])

        result = tree.traverse(TraverseOrder.PostOrder)
        self.assertEqual(list(result), [40, 50, 20, 60, 70, 30, 10])
