/**
You are given an integer array height of length `n`. There are n vertical lines drawn such that the two endpoints of the ith line are `(i, 0)` and `(i, height[i])`.
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

![Illustration](./10_container_with_most_water.jpg)

## Example 1:
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

## Example 2:
```
Input: height = [1,1]
Output: 1
```
*/

#include <array>
#include <cassert>
#include <functional>
#include <iostream>
#include <vector>

int most_water(const std::vector<int> &heights)
{
    if (heights.size() < 2)
    {
        return 0;
    }

    size_t left{0};
    size_t right{1};
    int max_volume{0};

    while (true)
    {
        int distance = right - left;
        int min_height = std::min(heights[left], heights[right]);
        int volume = distance * min_height;

        if (volume > max_volume)
        {
            max_volume = volume;
        }

        right++;
        if (right == heights.size())
        {
            left++;
            right = left + 1;
        }

        if (left == heights.size() - 1)
        {
            break;
        }
    }

    return max_volume;
}

struct TestCase
{
    std::vector<int> heights;
    int expected;
};

void test_most_water()
{
    std::array<TestCase, 2> test_cases{
        TestCase{
            .heights = std::vector<int>{1, 8, 6, 2, 5, 4, 8, 3, 7},
            .expected = 49,
        },
        TestCase{
            .heights = std::vector<int>{1, 1},
            .expected = 1,
        },
    };

    for (const auto &test_case : test_cases)
    {
        int got = most_water(test_case.heights);
        assert(got == test_case.expected);
    }
}
