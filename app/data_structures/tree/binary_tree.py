from dataclasses import dataclass
from typing import Generator, Self
from enum import Enum, auto


@dataclass
class Node[T]:
    data: T
    left: Self | None
    right: Self | None


class TraverseOrder(str, Enum):
    PreOrder = auto()
    InOrder = auto()
    PostOrder = auto()


class BinaryTree[T]:
    __slots__ = ["root"]
    root: Node[T]

    def __init__(self, root: Node[T]) -> None:
        self.root = root

    def traverse(self, order: TraverseOrder) -> Generator[T]:
        match order:
            case TraverseOrder.PreOrder:
                return self.__traverse_preorder(self.root)

            case TraverseOrder.InOrder:
                return self.__traverse_inorder(self.root)

            case TraverseOrder.PostOrder:
                return self.__traverse_postorder(self.root)

    def __traverse_preorder(self, node: Node[T] | None) -> Generator[T]:
        if node is None:
            return

        yield node.data
        if node.left is not None:
            yield from self.__traverse_preorder(node.left)

        if node.right is not None:
            yield from self.__traverse_preorder(node.right)

    def __traverse_inorder(self, node: Node[T] | None) -> Generator[T]:
        if node is None:
            return

        if node.left is not None:
            yield from self.__traverse_inorder(node.left)

        yield node.data
        if node.right is not None:
            yield from self.__traverse_inorder(node.right)

    def __traverse_postorder(self, node: Node[T] | None) -> Generator[T]:
        if node is None:
            return

        if node.left is not None:
            yield from self.__traverse_postorder(node.left)

        if node.right is not None:
            yield from self.__traverse_postorder(node.right)

        yield node.data
