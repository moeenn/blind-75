from dataclasses import dataclass
from unittest import TestCase
from app.arrays.best_time_to_buy_stocks import best_time_to_buy_stocks


@dataclass
class Scenario:
    prices: list[int]
    expected: int


class BestTimeToBuyStocks(TestCase):
    scenarios = [
        Scenario(prices=[7, 1, 5, 3, 6, 4], expected=5),
        Scenario(prices=[7, 6, 4, 3, 1], expected=0),
    ]

    def test_normal_cases(self) -> None:
        for s in self.scenarios:
            got = best_time_to_buy_stocks(s.prices)
            self.assertEqual(got, s.expected)
