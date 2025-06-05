"""
You are given an integer array height of length `n`. There are n vertical lines
drawn such that the two endpoints of the ith line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store. Notice that you may
not slant the container.

![Illustration](./10_container_with_most_water.jpg)

## Example 1:
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
```

## Example 2:
```
Input: height = [1,1]
Output: 1
```
"""


def container_with_most_water(heights: list[int]) -> int:
    size = len(heights)
    assert size >= 2
    max_volume = 0

    for i in range(size - 1):
        for j in range(i + 1, size):
            min_heigth = min(heights[i], heights[j])
            delta = j - i
            volume = min_heigth * delta
            if volume > max_volume:
                max_volume = volume

    return max_volume
