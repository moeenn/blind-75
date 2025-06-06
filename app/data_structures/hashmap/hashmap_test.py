from unittest import TestCase
from .hashmap import Hashmap


class TestHashmap(TestCase):
    def test_normal_usage(self) -> None:
        h = Hashmap[int](capacity=5)
        self.assertEqual(len(h), 0)

        h.put("Lahore", 100)
        h.put("Islamabad", 200)
        h.put("Karachi", 300)
        h.put("Multan", 400)

        self.assertEqual(len(h), 4)
        self.assertEqual(h.capacity, 5)

        h.put("Karachi", 3_000)
        self.assertEqual(len(h), 4)
        karachi_value = h.get("Karachi")
        self.assertEqual(karachi_value, 3_000)

        h.put("Gawadar", 500)
        h.put("Quetta", 600)
        self.assertEqual(len(h), 6)
        self.assertEqual(h.capacity, 10)

        self.assertTrue(h.remove("Lahore"))
        self.assertEqual(len(h), 5)
        self.assertEqual(h.capacity, 10)
        self.assertIsNone(h.get("Lahore"))

    def test_empty_operations(self) -> None:
        h = Hashmap[int](capacity=5)
        self.assertEqual(len(h), 0)
        kvs = h.__iter__()
        self.assertEqual(list(kvs), [])
