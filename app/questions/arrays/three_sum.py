"""
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]`
such that `i != j, i != k, and j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
Notice that the solution set must not contain duplicate triplets.

## Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

## Example 2:
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

## Example 3:
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```
"""

from typing import Self
from dataclasses import dataclass


@dataclass
class Triplet:
    a: int
    b: int
    c: int

    def equals(self, other: Self) -> bool:
        self_sum = self.a + self.b + self.c
        other_sum = other.a + other.b + other.c
        self_product = self.a * self.b * self.c
        other_product = other.a * other.b * other.c
        return (self_product == other_product) and (self_sum == other_sum)

    def is_included(self, triplets: list[Self]) -> bool:
        for t in triplets:
            if t.equals(self):
                return True

        return False


def three_sum(nums: list[int]) -> list[Triplet]:
    size = len(nums)
    assert size >= 3
    result: list[Triplet] = []

    def are_unique(i, j, k) -> bool:
        return len({i, j, k}) == 3

    for i in range(size - 2):
        for j in range(i, size - 1):
            for k in range(j, size):
                a = nums[i]
                b = nums[j]
                c = nums[k]

                sum = a + b + c
                are_idx_unique = are_unique(i, j, k)

                if sum == 0 and are_idx_unique:
                    triplet = Triplet(nums[i], nums[j], nums[k])
                    if not triplet.is_included(result):
                        result.append(triplet)

    return result
