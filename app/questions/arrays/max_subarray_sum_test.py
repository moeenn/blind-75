from unittest import TestCase
from .max_subarray_sum import max_subarray_sum
from dataclasses import dataclass


@dataclass
class Scenario:
    nums: list[int]
    expected: int


class TestMaxSubarraySum(TestCase):
    scenarios = [
        Scenario(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4], expected=6),
        Scenario(nums=[1], expected=1),
        Scenario(nums=[5, 4, -1, 7, 8], expected=23),
    ]

    def test_normal(self) -> None:
        for s in self.scenarios:
            got = max_subarray_sum(s.nums)
            self.assertEqual(got, s.expected)
