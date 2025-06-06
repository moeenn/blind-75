/*
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

## Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

## Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

## Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

## Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
*/
fn rotated_array_min(nums: &Vec<i32>) -> i32 {
    let mut i = 0;
    let len = nums.len();
    let mid_index = (len - 1) / 2;
    let mut min = nums[i];

    loop {
        if i == (mid_index + 1) {
            break;
        }

        if nums[i] < min {
            min = nums[i];
        }

        if nums[len - (i + 1)] < min {
            min = nums[len - (i + 1)];
        }

        i += 1;
    }

    return min;
}

struct TestCase {
    nums: Vec<i32>,
    expected: i32,
}

#[test]
fn test_rotated_array_min() {
    let test_cases = vec![
        TestCase {
            nums: vec![3, 4, 5, 1, 2],
            expected: 1,
        },
        TestCase {
            nums: vec![4, 5, 6, 7, 0, 1, 2],
            expected: 0,
        },
        TestCase {
            nums: vec![11, 13, 15, 17],
            expected: 11,
        },
    ];

    for test_case in test_cases.iter() {
        let got = rotated_array_min(&test_case.nums);
        assert_eq!(got, test_case.expected);
    }
}
 
