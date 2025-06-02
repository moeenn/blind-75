from dataclasses import dataclass

"""
Given an array of integers `nums` and an integer `target`, return indices of
the two numbers such that they add up to `target`. You may assume that each
input would have exactly one solution, and you may not use the same element
twice. You can return the answer in any order.

## Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```
"""


@dataclass
class Pair:
    first: int
    second: int


def two_sum(nums: list[int], target: int) -> list[Pair]:
    size = len(nums)
    assert size >= 2
    result: list[Pair] = []

    for a in range(size - 1):
        for b in range(a + 1, size):
            if nums[a] + nums[b] == target:
                result.append(Pair(a, b))

    return result
