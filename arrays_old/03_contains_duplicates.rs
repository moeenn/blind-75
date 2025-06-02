/**
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

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
*/

fn contains_duplicates(nums: &Vec<i32>) -> bool {
    if nums.len() <= 1 {
        return false;
    }

    let mut start = 0;
    let mut end = 1;

    loop {
        if nums[start] == nums[end] {
            return true;
        }

        end += 1;
        if end == nums.len() {
            start += 1;
            end = start + 1;
        }

        if start == nums.len() - 1 {
            break;
        }
    }

    return false;
}

struct TestCase {
    nums: Vec<i32>,
    expected: bool,
}

#[test]
fn test_contains_duplicates() {
    let test_cases = vec![
        TestCase {
            nums: vec![1, 2, 3, 1],
            expected: true,
        },
        TestCase {
            nums: vec![1, 2, 3, 4],
            expected: false,
        },
        TestCase {
            nums: vec![1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
            expected: true,
        },
    ];

    for test_case in test_cases {
        let got = contains_duplicates(&test_case.nums);
        assert_eq!(got, test_case.expected);
    }
}
