from unittest import TestCase
from .doubly_linked_list import DoublyLinkedList, LoopDirection


class TestDoublyLinkedList(TestCase):
    def test_normal_operations(self) -> None:
        ll = DoublyLinkedList[int]()
        self.assertEqual(len(ll), 0)

        for i in range(5):
            ll.append(i + 1)

        all_elements = list(ll.__iter__())
        self.assertEqual(len(ll), 5)
        self.assertEqual(all_elements, [1, 2, 3, 4, 5])
        self.assertTrue(ll.head is not None and ll.head.data == 1)
        self.assertTrue(ll.tail is not None and ll.tail.data == 5)

        ll.prepend(100)
        self.assertEqual(len(ll), 6)
        self.assertTrue(ll.head is not None and ll.head.data == 100)
        self.assertTrue(
            ll.head is not None and ll.head.next is not None and ll.head.next.data == 1
        )

        self.assertEqual(ll.at(2), 2)
        self.assertEqual(ll.at(4), 4)
        self.assertIsNone(ll.at(20))
        self.assertIsNone(ll.at(-1))

        is_removed = ll.remove(3)
        self.assertTrue(is_removed)
        self.assertEqual(len(ll), 5)
        self.assertEqual(ll.at(3), 4)
        self.assertFalse(ll.remove(20))
        self.assertFalse(ll.remove(-2))

    def test_loop_back_and_forth(self) -> None:
        ll = DoublyLinkedList[int]()
        for i in range(5):
            ll.append(i + 1)

        forward = list(ll.values(LoopDirection.Asc))
        self.assertEqual(forward, [i + 1 for i in range(5)])

        backwards = list(ll.values(LoopDirection.Desc))
        self.assertEqual(backwards, [i for i in range(5, 0, -1)])
