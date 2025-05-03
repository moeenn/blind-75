/**
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

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
*/

#include <array>
#include <cassert>
#include <functional>
#include <iostream>
#include <vector>

typedef std::pair<size_t, size_t> Pair;
bool pair_equals(const Pair &a, const Pair &b)
{
    return (a.first == b.first && a.second == b.second);
}

std::vector<Pair> get_pairs(const std::vector<int> &nums, int target)
{
    std::vector<Pair> result{};
    if (nums.size() < 2)
    {
        return result;
    }

    size_t i = 0;
    size_t j = 1;

    while (true)
    {
        if (nums[i] + nums[j] == target)
        {
            result.push_back(Pair{i, j});
        }

        j++;
        if (j == nums.size())
        {
            i++;
            j = i + 1;
        }

        if (i == nums.size() - 1)
        {
            break;
        }
    }

    return result;
}

struct TestCase
{
    std::vector<int> nums;
    int target;
    std::vector<Pair> expected;
};

void test_get_pairs()
{
    std::array<TestCase, 3> test_cases{
        TestCase{
            .nums = std::vector{2, 7, 11, 15},
            .target = 9,
            .expected = std::vector<Pair>{Pair{0, 1}},
        },
        TestCase{
            .nums = std::vector{3, 2, 4},
            .target = 6,
            .expected = std::vector<Pair>{Pair{1, 2}},
        },
        TestCase{
            .nums = std::vector{3, 3},
            .target = 6,
            .expected = std::vector<Pair>{Pair{0, 1}},
        },
    };

    for (const auto &test_case : test_cases)
    {
        std::vector<Pair> got = get_pairs(test_case.nums, test_case.target);
        assert(got.size() == test_case.expected.size());

        for (size_t i{0}; i < got.size(); i++)
        {
            assert(pair_equals(got[i], test_case.expected[i]));
        }
    }
}

typedef std::function<void()> Test;
std::array<Test, 1> tests{test_get_pairs};

void run_tests()
{
    for (const auto &test : tests)
    {
        test();
    }
    std::cout << "-- all tests pass --\n";
}
