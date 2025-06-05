from typing import Generator


class Queue[T]:
    front: int = 0
    back: int = 0
    capacity: int
    data: list[T | None]

    def __init__(self, capacity=5) -> None:
        self.capacity = capacity
        self.data = [None] * capacity

    def size(self) -> int:
        return self.back - self.front

    def is_empty(self) -> bool:
        return self.size() == 0

    def is_full(self) -> bool:
        return self.size() == self.capacity

    def values(self) -> Generator[T]:
        for i in range(self.size()):
            value = self.data[i]
            if value is None:
                raise Exception(f"unexpected None value in data at index {i}")

            yield value

    def enqueue(self, value: T) -> None:
        if self.back < self.capacity:
            self.data[self.back] = value
            self.back += 1
            return

        # if there is space at the start of the queue, shift all elements forward.
        if self.front != 0:
            for i in range(self.size()):
                self.data[i] = self.data[i + self.front]

            self.back -= self.front
            self.front = 0
            self.data[self.back] = value
            self.back += 1
            return

        # resize operation.
        new_capacity = self.capacity * 2
        new_data: list[T | None] = [None] * new_capacity
        for i in range(self.front, self.back):
            new_data[i] = self.data[self.front + i]

        new_data[self.back] = value
        self.back += 1
        self.capacity = new_capacity
        self.data = new_data

    def dequeue(self) -> T | None:
        if self.is_empty():
            return None

        value = self.data[self.front]
        self.front += 1
        return value

    def peek(self) -> T | None:
        if self.is_empty():
            return None

        return self.data[self.front]
