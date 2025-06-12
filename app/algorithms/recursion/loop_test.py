from unittest import TestCase
from .loop import loop


class TestLoop(TestCase):
    def test_recursive_loop(self) -> None:
        nums = [1, 2, 3, 4, 5, 6, 7]
        asc = list(loop(nums))
        self.assertEqual(asc, [1, 2, 3, 4, 5, 6, 7])

        # confirm original list is not modified.
        asc = list(loop(nums))
        self.assertEqual(asc, [1, 2, 3, 4, 5, 6, 7])
