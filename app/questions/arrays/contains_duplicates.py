"""
Given an integer array `nums`, return `true` if any value appears at least
twice in the array, and return `false` if every element is distinct.

## Example 1:
```
Input: nums = [1,2,3,1]
Output: true
```

## Example 2:
```
Input: nums = [1,2,3,4]
Output: false
```

## Example 3:
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 ```
"""


def contains_duplicates(nums: list[int]) -> bool:
    size = len(nums)
    assert size >= 2

    for start_idx in range(size - 1):
        for end_idx in range(start_idx + 1, size):
            if nums[start_idx] == nums[end_idx]:
                return True

    return False
