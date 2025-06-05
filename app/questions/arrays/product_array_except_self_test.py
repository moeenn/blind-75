from unittest import TestCase
from dataclasses import dataclass
from .product_array_except_self import product_except_self


@dataclass
class Scenario:
    nums: list[int]
    expected: list[int]


class TestProductExceptSelf(TestCase):
    scenarios = [
        Scenario(nums=[1, 2, 3, 4], expected=[24, 12, 8, 6]),
        Scenario(nums=[-1, 1, 0, -3, 3], expected=[0, 0, 9, 0, 0]),
    ]

    def test_valid_cases(self) -> None:
        for s in self.scenarios:
            got = product_except_self(s.nums)
            self.assertEqual(got, s.expected)
