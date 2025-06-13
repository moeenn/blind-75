from unittest import TestCase
from dataclasses import dataclass
from .merge_sort import merge_sort


@dataclass
class Scenario:
    data: list[int]
    expected: list[int]


class TestMergeSort(TestCase):
    scenarios = [Scenario(data=[7, 6, 1, 5, 3, 4], expected=[1, 3, 4, 5, 6, 7])]

    def test_merge_sort(self) -> None:
        for s in self.scenarios:
            got = merge_sort(s.data)
            self.assertEqual(got, s.expected)
