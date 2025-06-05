from unittest import TestCase
from .container_with_most_water import container_with_most_water
from dataclasses import dataclass


@dataclass
class Scenario:
    heights: list[int]
    expected: int


class TestContainerWithMostWater(TestCase):
    scenarios = [
        Scenario(heights=[1, 8, 6, 2, 5, 4, 8, 3, 7], expected=49),
        Scenario(heights=[1, 1], expected=1),
    ]

    def test_valid_case(self) -> None:
        for s in self.scenarios:
            got = container_with_most_water(s.heights)
            self.assertEqual(got, s.expected)
