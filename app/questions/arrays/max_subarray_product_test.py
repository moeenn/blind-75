from unittest import TestCase
from .max_subarray_product import max_subarray_product
from dataclasses import dataclass


@dataclass
class Scenario:
    nums: list[int]
    expected: int


class TestMaxSubarrayProduct(TestCase):
    scenarios = [
        Scenario(nums=[2, 3, -2, 4], expected=6),
        Scenario(nums=[-2, 0, -1], expected=0),
    ]

    def test_normal(self) -> None:
        for s in self.scenarios:
            got = max_subarray_product(s.nums)
            self.assertEqual(got, s.expected)
