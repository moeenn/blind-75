from typing import Self, Generator
from dataclasses import dataclass


@dataclass
class Node[T]:
    data: T
    next: Self | None


class LinkedList[T]:
    __slots__ = ["head", "size"]
    head: Node[T] | None
    size: int

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __iter__(self) -> Generator[T]:
        current = self.head
        if current is None:
            return

        while current is not None:
            yield current.data
            current = current.next

    def __len__(self) -> int:
        return self.size

    def enumerate(self) -> Generator[tuple[int, T]]:
        index = 0
        current = self.head
        if current is None:
            return

        while current is not None:
            yield (index, current.data)
            current = current.next
            index += 1

    def append(self, value: T) -> None:
        new_node = Node(value, next=None)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        # traverse the list.
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        self.size += 1

    def prepend(self, value: T) -> None:
        new_node = Node(value, next=None)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def at(self, index: int) -> T | None:
        for idx, value in self.enumerate():
            if idx == index:
                return value

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False

        if index == 0:
            # this won't happend because we have already checked index and size.
            if self.head is None:
                return False

            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        prev: Node[T] | None = None
        i = 0

        while current is not None:
            if index == i:
                # this won't happend because index 0 is already handled above.
                if prev is None:
                    return False

                prev.next = current.next
                self.size -= 1
                return True

            prev = current
            current = current.next
            i += 1

        return False
