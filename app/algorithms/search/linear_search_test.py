from unittest import TestCase
from dataclasses import dataclass
from .linear_search import linear_search


@dataclass
class Scenario:
    nums: list[int]
    target: int
    expected: int | None


class TestBinarySearch(TestCase):
    scenarios = [
        Scenario(nums=[1, 2, 3, 4, 5], target=3, expected=2),
        Scenario(nums=[10, 20, 30, 40, 50, 60], target=50, expected=4),
        Scenario(nums=[6, 7, 8, 9, 100], target=6, expected=0),
        Scenario(nums=[4, 5, 6, 7, 8], target=3, expected=None),
        Scenario(nums=[20, 30, 40, 50], target=100, expected=None),
    ]

    def test_binary_search(self) -> None:
        for s in self.scenarios:
            got = linear_search(s.nums, s.target)
            self.assertEqual(got, s.expected)
