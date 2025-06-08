from unittest import TestCase
from dataclasses import dataclass
from .three_sum import three_sum, Triplet


@dataclass
class Scenario:
    nums: list[int]
    expected: list[Triplet]


class TestThreeSum(TestCase):
    scenarios = [
        Scenario(
            nums=[-1, 0, 1, 2, -1, -4], expected=[Triplet(-1, -1, 2), Triplet(-1, 0, 1)]
        ),
        Scenario(nums=[0, 1, 1], expected=[]),
        Scenario(nums=[0, 0, 0], expected=[Triplet(0, 0, 0)]),
    ]

    def test_usage(self) -> None:
        for s in self.scenarios:
            got = three_sum(s.nums)
            self.assertEqual(len(got), len(s.expected))
            for triplet in got:
                self.assertTrue(triplet.is_included(s.expected))
