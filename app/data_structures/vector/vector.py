from typing import Generator


class Vector[T]:
    __slots__ = ["index", "capacity", "data"]

    index: int
    capacity: int
    data: list[T | None]

    def __init__(self, capacity: int = 4) -> None:
        self.index = 0
        self.capacity = capacity
        self.data = [None] * capacity

    def __len__(self) -> int:
        return self.index

    def __iter__(self) -> Generator[T]:
        for i in range(self.index):
            value = self.data[i]
            if value is None:
                continue
            yield value

    def push(self, item: T) -> None:
        if self.index != self.capacity:
            self.data[self.index] = item
            self.index += 1
            return

        # resize operation.
        self.__resize()
        self.data[self.index] = item
        self.index += 1

    def __resize(self) -> None:
        new_capacity = self.capacity * 2
        new_data: list[T | None] = [None] * new_capacity
        for index, entry in enumerate(self.data):
            new_data[index] = entry

        self.capacity = new_capacity
        self.data = new_data

    def pop(self) -> T | None:
        value = self.data[self.index - 1]
        self.index -= 1
        return value

    def insert(self, index: int, value: T) -> bool:
        if index >= self.index:
            return False

        # resize if doesn't fit within the current buffer.
        if self.index >= self.capacity:
            self.__resize()

        # shift elements forward one slot.
        for i in range(self.index - index):
            self.data[self.index - i] = self.data[self.index - i - 1]

        self.data[index] = value
        self.index += 1
        return True
