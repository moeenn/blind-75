/**
Given an integer array `nums`, find the subarray with the largest `sum`, and return its `sum`.

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
*/
fn sum_subarray(nums: &Vec<i32>, start_idx: usize, end_idx: usize) -> i32 {
    assert!(end_idx < nums.len());
    assert!(start_idx < end_idx);

    let mut sum = nums[start_idx];
    for i in start_idx + 1..=end_idx {
        sum += nums[i];
    }

    return sum;
}

fn max_subarray_sum(nums: &Vec<i32>) -> i32 {
    if nums.len() == 0 {
        return 0;
    }

    if nums.len() == 1 {
        return nums[0];
    }

    let mut left = 0;
    let mut right = 1;
    let mut max_sum: Option<i32> = None;

    loop {
        let sum = sum_subarray(nums, left, right);
        if let None = max_sum {
            max_sum = Some(sum);
        }

        if let Some(current_max) = max_sum {
            if sum > current_max {
                max_sum = Some(sum);
            }
        }

        right += 1;
        if right == nums.len() {
            left += 1;
            right = left + 1;
        }

        if left == nums.len() - 1 {
            break;
        }
    }

    return max_sum.unwrap_or(0);
}

struct TestCase {
    nums: Vec<i32>,
    expected: i32,
}

#[test]
fn test_max_subarray_sum() {
    let test_cases = vec![
        TestCase {
            nums: vec![-2, 1, -3, 4, -1, 2, 1, -5, 4],
            expected: 6,
        },
        TestCase {
            nums: vec![1],
            expected: 1,
        },
        TestCase {
            nums: vec![5, 4, -1, 7, 8],
            expected: 23,
        },
    ];

    for test_case in test_cases {
        let got = max_subarray_sum(&test_case.nums);
        assert_eq!(got, test_case.expected);
    }
}
 
