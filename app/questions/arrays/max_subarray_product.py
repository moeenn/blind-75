"""
Given an integer array `nums`, find a subarray that has the largest `product`,
and return the `product`. The test cases are generated so that the answer will
fit in a 32-bit integer.

## Example 1:
```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

## Example 2:
```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

## Constraints:
```
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.
```
"""


def max_subarray_product(nums: list[int]) -> int:
    size = len(nums)
    match size:
        case 0:
            return 0
        case 1:
            return nums[0]

    result: int | None = None
    for i in range(size - 1):
        for j in range(i + 1, size):
            product = product_subarray(nums, start=i, end=j)
            if result is None or product > result:
                result = product

    if result is None:
        raise Exception("sub-array product calculation failure")

    return result


def product_subarray(nums: list[int], start: int, end: int) -> int:
    product = 1
    for i in range(start, end + 1):
        product *= nums[i]

    return product
