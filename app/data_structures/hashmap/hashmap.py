from dataclasses import dataclass
from typing import Generator, Self
import zlib


@dataclass
class Node[T]:
    key: str
    value: T
    next: Self | None


class Hashmap[T]:
    __slots__ = ["capacity", "index", "buckets"]

    capacity: int
    index: int
    buckets: list[Node[T] | None]

    def __init__(self, capacity: int = 5) -> None:
        self.index = 0
        self.capacity = capacity
        self.buckets = [None] * capacity

    def __len__(self) -> int:
        return self.index

    def __iter__(self) -> Generator[tuple[str, T]]:
        for i in range(self.capacity):
            bucket = self.buckets[i]
            if bucket is None:
                continue

            current_node = bucket
            while current_node is not None:
                yield (current_node.key, current_node.value)
                current_node = current_node.next

    def __traverse_nodes(self) -> Generator[Node[T]]:
        for i in range(self.capacity):
            bucket = self.buckets[i]
            if bucket is None:
                continue

            current_node = bucket
            while current_node is not None:
                yield current_node
                current_node = current_node.next

    def contains(self, key: str) -> bool:
        for k, _ in self:
            if k == key:
                return True

        return False

    def get(self, key: str) -> T | None:
        for k, v in self:
            if k == key:
                return v

    @staticmethod
    def hash(key: str) -> int:
        # this hash is deterministic. hash() function generated unique hashes
        # on every program run.
        return abs(zlib.crc32(key.encode()))

    def put(self, key: str, value: T) -> None:
        hash = Hashmap.hash(key)
        index = hash % self.capacity
        target_bucket = self.buckets[index]
        new_node = Node(key=key, value=value, next=None)

        if target_bucket is None:
            self.buckets[index] = new_node
            self.index += 1
        else:
            # traverse the target bucket.
            current_node = target_bucket
            while current_node is not None:
                # update operation, because key already exists.
                if current_node.key == key:
                    current_node.value = value
                    return

                if current_node.next is None:
                    # append to last node.
                    current_node.next = new_node
                    self.index += 1
                    break

                current_node = current_node.next

        if self.index == self.capacity:
            # resize operation.
            new_capacity = self.capacity * 2
            new_buckets: list[Node[T] | None] = [None] * new_capacity

            for node in self.__traverse_nodes():
                new_index = Hashmap.hash(node.key) % new_capacity
                bucket = new_buckets[new_index]

                if bucket is None:
                    new_buckets[new_index] = node
                else:
                    current_node = bucket
                    while current_node.next is not None:
                        current_node = current_node.next

                    current_node.next = node

            self.capacity = new_capacity
            self.buckets = new_buckets

    def remove(self, key: str) -> bool:
        for i in range(self.capacity):
            bucket = self.buckets[i]
            if bucket is None:
                continue

            current_node = bucket
            prev_node: Node[T] | None = None

            while current_node is not None:
                if current_node.key == key:
                    if prev_node is None:
                        self.buckets[i] = current_node.next
                        self.index -= 1
                        return True
                    else:
                        prev_node.next = current_node.next
                        self.index -= 1
                        return True

                prev_node = current_node
                current_node = current_node.next

        return False
