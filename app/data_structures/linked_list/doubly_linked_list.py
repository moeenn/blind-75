from dataclasses import dataclass
from enum import Enum
from typing import Generator, Self


@dataclass
class Node[T]:
    data: T
    prev: Self | None = None
    next: Self | None = None


class LoopDirection(Enum):
    Asc = "asc"
    Desc = "desc"


class DoublyLinkedList[T]:
    __slots__ = ["head", "tail", "size"]
    head: Node[T] | None
    tail: Node[T] | None
    size: int

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    # loop forward.
    def __iter__(self) -> Generator[T]:
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __loop_backwards(self) -> Generator[T]:
        current = self.tail
        while current is not None:
            yield current.data
            current = current.prev

    def values(self, direction: LoopDirection = LoopDirection.Asc) -> Generator[T]:
        match direction:
            case LoopDirection.Asc:
                for v in self:
                    yield v

            case LoopDirection.Desc:
                yield from self.__loop_backwards()

    def append(self, data: T) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next

        new_node.prev = current
        current.next = new_node
        self.tail = new_node
        self.size += 1

    def prepend(self, data: T) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def at(self, index: int) -> T | None:
        if index < 0 or index >= self.size:
            return None

        back_delta = self.size - index
        direction = LoopDirection.Asc if index < back_delta else LoopDirection.Desc

        match direction:
            case LoopDirection.Asc:
                i = 0
                for v in self:
                    if i == index:
                        return v
                    i += 1

            case LoopDirection.Desc:
                i = self.size - 1
                for v in self.__loop_backwards():
                    if i == index:
                        return v
                    i -= 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        if index == 0:
            if self.head is None:
                return False

            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

            self.size -= 1
            return True

        i = 0
        current = self.head
        prev: Node[T] | None = None

        if current is not None:
            while current.next is not None:
                if i == index:
                    if prev is not None:
                        prev.next = current.next
                        if current.next is not None:
                            current.next.prev = prev

                    self.size -= 1
                    return True

                prev = current
                current = current.next
                i += 1

        return False
