from unittest import TestCase
from .stack import Stack


class TestStack(TestCase):
    def test_normal_usage(self) -> None:
        s = Stack[int](capacity=5)
        self.assertEqual(s.capacity, 5)
        for i in range(4):
            s.push(i + 1)

        self.assertEqual(len(s), 4)
        self.assertEqual(s.capacity, 5)

        s.push(5)
        self.assertEqual(5, len(s))
        s.push(6)
        self.assertEqual(6, len(s))
        self.assertEqual(10, s.capacity)

        self.assertEqual(s.peek(), 6)
        self.assertEqual(len(s), 6)
        self.assertEqual(s.pop(), 6)
        self.assertEqual(len(s), 5)

    def test_empty_stack(self) -> None:
        s = Stack[int](10)
        self.assertEqual(len(s), 0)
        self.assertEqual(s.capacity, 10)

        values = list(s.__iter__())
        self.assertEqual(values, [])
        self.assertIsNone(s.pop())
        self.assertIsNone(s.peek())
