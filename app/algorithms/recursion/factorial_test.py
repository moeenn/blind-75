from unittest import TestCase
from .factorial import factorial, factorial_tail_optimized
from dataclasses import dataclass


@dataclass
class Scenario:
    n: int
    expected: int


class TestFactorial(TestCase):
    scenarios = [
        Scenario(n=5, expected=120),
    ]

    def test_factorials(self) -> None:
        for s in self.scenarios:
            got = factorial(s.n)
            got_optimized = factorial_tail_optimized(s.n)
            self.assertEqual(got, s.expected)
            self.assertEqual(got_optimized, s.expected)
