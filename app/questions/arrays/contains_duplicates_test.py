from unittest import TestCase
from dataclasses import dataclass
from .contains_duplicates import contains_duplicates


@dataclass
class Scenario:
    nums: list[int]
    expected: bool


class TestContainsDuplicates(TestCase):
    scenarios = [
        Scenario(nums=[1, 2, 3, 1], expected=True),
        Scenario(nums=[1, 2, 3, 4], expected=False),
        Scenario(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], expected=True),
    ]

    def test_valid_cases(self) -> None:
        for s in self.scenarios:
            got = contains_duplicates(s.nums)
            self.assertEqual(got, s.expected)
