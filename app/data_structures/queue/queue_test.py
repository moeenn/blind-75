from unittest import TestCase
from .queue import Queue


class TestQueue(TestCase):
    def test_normal_usage(self) -> None:
        q = Queue[int](capacity=5)
        self.assertTrue(q.is_empty())
        for i in range(4):
            q.enqueue(i + 1)

        self.assertEqual(q.size(), 4)
        self.assertEqual(q.capacity, 5)

        all_elements = q.values()
        self.assertEqual(list(all_elements), [1, 2, 3, 4])

        first = q.dequeue()
        self.assertEqual(first, 1)
        self.assertEqual(q.size(), 3)

        q.enqueue(5)
        q.enqueue(6)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.capacity, 5)
        self.assertTrue(q.is_full())

        q.enqueue(7)
        self.assertEqual(q.size(), 6)
        self.assertEqual(q.capacity, 10)

        peeked = q.peek()
        self.assertEqual(peeked, 2)
        self.assertEqual(q.size(), 6)

    def test_empty_list(self) -> None:
        q = Queue[int](capacity=5)
        items = q.values()
        self.assertEqual(list(items), [])
        self.assertIsNone(q.peek())
        self.assertIsNone(q.dequeue())
