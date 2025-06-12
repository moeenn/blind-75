from unittest import TestCase
from .linked_list import LinkedList


class TestLinkedList(TestCase):
    def test_normal_usage(self) -> None:
        ll = LinkedList[int]()
        for i in range(1, 6):
            ll.append(i)

        ll.prepend(100)
        ll.prepend(200)

        self.assertEqual(7, len(ll))

        all_elements = list(ll.__iter__())
        expected_values = [200, 100, 1, 2, 3, 4, 5]
        self.assertEqual(expected_values, all_elements)

        ll.prepend(300)
        first = ll.at(0)
        self.assertEqual(300, first)

        non_existent = ll.at(10)
        self.assertIsNone(non_existent)

        is_removed = ll.remove(7)
        self.assertTrue(is_removed)

        last = ll.at(7)
        self.assertIsNone(last)
        self.assertEqual(7, len(ll))

        fourth = ll.at(3)
        self.assertEqual(1, fourth)
        self.assertTrue(ll.remove(3))
        fourth = ll.at(3)
        self.assertEqual(fourth, 2)

    def test_ops_on_empty_list(self) -> None:
        ll = LinkedList[int]()
        self.assertEqual(len(ll), 0)
        entries = list(ll.__iter__())
        self.assertEqual(entries, [])
        enumerated = list(ll.enumerate())
        self.assertEqual(enumerated, [])
        self.assertIsNone(ll.at(0))
        self.assertFalse(ll.remove(0))
