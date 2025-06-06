from unittest import TestCase
from .vector import Vector


class TestVector(TestCase):
    def test_normal_usage(self) -> None:
        v = Vector[int](capacity=4)
        for i in range(4):
            v.push(i + 1)

        self.assertEqual(v.capacity, 4)
        self.assertEqual(len(v), 4)

        v.push(5)
        self.assertEqual(v.capacity, 8)
        self.assertEqual(len(v), 5)

        all_entries = list(v.__iter__())
        self.assertEqual(all_entries, [1, 2, 3, 4, 5])

        is_added = v.insert(index=2, value=100)
        self.assertTrue(is_added)

        self.assertEqual(v.capacity, 8)
        self.assertEqual(len(v), 6)
        self.assertEqual(list(v.__iter__()), [1, 2, 100, 3, 4, 5])

        popped = v.pop()
        self.assertEqual(popped, 5)
        self.assertEqual(len(v), 5)
        self.assertEqual(v.capacity, 8)

    def test_iter(self) -> None:
        v = Vector[int]()
        for i in range(5):
            v.push(i + 1)

        collected: list[int] = []
        for n in v:
            collected.append(n)

        self.assertEqual(collected, [1, 2, 3, 4, 5])
