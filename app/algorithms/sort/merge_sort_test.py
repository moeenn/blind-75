from unittest import TestCase
from dataclasses import dataclass
from .merge_sort import merge, merge_sort


@dataclass
class MergeScenario:
    a: list[int]
    b: list[int]
    expected: list[int]


class TestMerge(TestCase):
    scenarios = [
        MergeScenario(
            a=[1, 2, 3, 4],
            b=[5, 6, 7, 8],
            expected=[1, 2, 3, 4, 5, 6, 7, 8],
        ),
        MergeScenario(
            a=[2, 4, 6, 8],
            b=[1, 3, 5, 9],
            expected=[1, 2, 3, 4, 5, 6, 8, 9],
        ),
        MergeScenario(
            a=[10, 2, -3, 1, 5],
            b=[50, 10, 2],
            expected=[-3, 1, 2, 5, 10, 20, 50],
        ),
    ]

    def test_merge(self) -> None:
        for s in self.scenarios:
            got = merge(s.a, s.b)
            self.assertEqual(got, s.expected)


@dataclass
class MergeSortScenario:
    data: list[int]
    expected: list[int]


class TestMergeSort(TestCase):
    scenarios = [
        # MergeSortScenario(data=[7, 2, 6, 1, 5, 3, 4], expected=[1, 2, 3, 4, 5, 6, 7]),
    ]

    def test_merge_sort(self) -> None:
        for s in self.scenarios:
            got = merge_sort(s.data)
            self.assertEqual(got, s.expected)
