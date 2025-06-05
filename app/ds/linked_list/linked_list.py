from typing import Self, Generator
from dataclasses import dataclass


@dataclass
class Node[T]:
    data: T
    next: Self | None


@dataclass
class ValueWithIndex[T]:
    index: int
    value: T


class LinkedList[T]:
    head: Node[T] | None
    size: int

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def values(self) -> Generator[T]:
        current = self.head
        if current is None:
            return

        while current is not None:
            yield current.data
            current = current.next

    def enumerate(self) -> Generator[ValueWithIndex[T]]:
        index = 0
        current = self.head
        if current is None:
            return

        while current is not None:
            yield ValueWithIndex(index, value=current.data)
            current = current.next

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
        for entry in self.enumerate():
            if entry.index == index:
                return entry.value

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
            if index == i and prev is not None:
                prev.next = current.next
                self.size -= 1
                return True

            prev = current
            i += 1

        return False
