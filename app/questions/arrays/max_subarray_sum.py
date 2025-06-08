"""
Given an integer array `nums`, find the subarray with the largest `sum`, and
return its `sum`.

## Example 1:
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

Example 2:
```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

Example 3:
```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

Constraints:
```
1 <= nums.length <= 105
-104 <= nums[i] <= 104
```
"""


def max_subarray_sum(nums: list[int]) -> int:
    size = len(nums)
    match size:
        case 0:
            return 0
        case 1:
            return nums[0]

    result: int | None = None
    for i in range(size - 1):
        for j in range(i + 1, size):
            sum = sum_subarray(nums, start=i, end=j)
            if result is None or sum > result:
                result = sum

    if result is None:
        raise Exception("sub-array sum calculation failure")

    return result


def sum_subarray(nums: list[int], start: int, end: int) -> int:
    sum = 0
    for i in range(start, end + 1):
        sum += nums[i]

    return sum
