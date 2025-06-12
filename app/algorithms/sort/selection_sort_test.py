from unittest import TestCase
from dataclasses import dataclass
from .selection_sort import selection_sort


@dataclass
class Scenario:
    nums: list[int]
    expected: list[int]


class TestSelectionSort(TestCase):
    scenarios = [
        Scenario(
            nums=[100, 90, 80, 70, 60, 50, 40],
            expected=[40, 50, 60, 70, 80, 90, 100],
        ),
        Scenario(
            nums=[-2, 45, 0, 11, -9],
            expected=[-9, -2, 0, 11, 45],
        ),
    ]

    def test_selection_sort(self) -> None:
        for s in self.scenarios:
            selection_sort(s.nums)
            self.assertEqual(s.nums, s.expected)
