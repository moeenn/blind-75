from dataclasses import dataclass
from typing import Generator, Self
from enum import Enum, auto


@dataclass
class Node[T]:
    data: T
    left: Self | None = None
    right: Self | None = None


class TraverseOrder(str, Enum):
    PreOrder = auto()
    InOrder = auto()
    PostOrder = auto()


class BinaryTree[T]:
    __slots__ = ["root"]
    root: Node[T] | None

    def __init__(self, root: Node[T] | None) -> None:
        self.root = root

    @classmethod
    def from_array(cls, data: list[T]) -> Self:
        size = len(data)
        tree = cls(root=None)
        if size == 0:
            return tree

        tree.root = Node(data[0])
        queue: list[Node[T] | None] = [tree.root]
        i = 1

        while queue and i < size:
            current = queue.pop(0)
            if current is None:
                continue

            if i < size:
                current.left = Node(data[i])
                queue.append(current.left)
            i += 1

            if i < size:
                current.right = Node(data[i])
                queue.append(current.right)
            i += 1

        return tree

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

    # a binary is a full tree when all nodes either have no children
    # (left, right), or they have exactly two child nodes.
    def is_full_tree(self) -> bool:
        def is_full(root: Node[T] | None) -> bool:
            if root is None:
                return True

            if root.left is None and root.right is None:
                return True

            if root.right is not None and root.right is not None:
                return is_full(root.left) and is_full(root.right)

            return False

        return is_full(self.root)
