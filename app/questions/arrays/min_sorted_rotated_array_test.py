from unittest import TestCase
from .min_sorted_rotated_array import min_sorted_rorated_array
from dataclasses import dataclass


@dataclass
class Scenario:
    nums: list[int]
    expected: int


class TestMinRotatedSortedArray(TestCase):
    scenarios = [
        Scenario(nums=[3, 4, 5, 1, 2], expected=1),
        Scenario(nums=[4, 5, 6, 7, 0, 1, 2], expected=0),
        Scenario(nums=[11, 13, 15, 17], expected=11),
    ]

    def test_normal(self) -> None:
        for s in self.scenarios:
            got = min_sorted_rorated_array(s.nums)
            self.assertEqual(got, s.expected)
