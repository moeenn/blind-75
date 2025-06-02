from dataclasses import dataclass
from unittest import TestCase
from app.arrays.two_sum import Pair, two_sum


@dataclass
class Scenario:
    nums: list[int]
    target: int
    expected: list[Pair]


class TestTwoSum(TestCase):
    scenarios = [
        Scenario(nums=[2, 7, 11, 15], target=9, expected=[Pair(0, 1)]),
        Scenario(nums=[3, 2, 4], target=6, expected=[Pair(1, 2)]),
        Scenario(nums=[3, 3], target=6, expected=[Pair(0, 1)]),
    ]

    def test_valid(self) -> None:
        for s in self.scenarios:
            got = two_sum(s.nums, s.target)
            self.assertEqual(got, s.expected)
