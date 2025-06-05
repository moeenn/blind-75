from typing import Generator


class Stack[T]:
    capacity: int
    index: int
    data: list[T | None]

    def __init__(self, capacity=5) -> None:
        self.capacity = capacity
        self.index = 0
        self.data = [None] * capacity

    def size(self) -> int:
        return self.index

    def values(self) -> Generator[T]:
        for i in range(self.index):
            value = self.data[i]
            if value is None:
                raise Exception(f"unexpected None in data at index {i}")

            yield value

    def push(self, value: T) -> None:
        if self.index < self.capacity:
            self.data[self.index] = value
            self.index += 1
            return

        # resize operation.
        new_capacity = self.capacity * 2
        new_data: list[T | None] = [None] * new_capacity
        for i in range(self.index):
            new_data[i] = self.data[i]

        new_data[self.index] = value
        self.data = new_data
        self.capacity = new_capacity
        self.index += 1

    def pop(self) -> T | None:
        if self.index == 0:
            return None

        value = self.data[self.index - 1]
        self.index -= 1
        return value

    def peek(self) -> T | None:
        if self.index == 0:
            return None

        return self.data[self.index - 1]
