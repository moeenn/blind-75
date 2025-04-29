/**
Given an integer array `nums`, return an array answer such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

## Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

## Example 2:
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Constraints:
```
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
```
*/
fn product_array_except_index(nums: &Vec<i32>, index: usize) -> i32 {
    if nums.len() == 0 {
        return 0;
    }

    let mut result = 1;
    for i in 0..nums.len() {
        if i == index {
            continue;
        }
        result *= nums[i];
    }

    return result;
}

fn product_array_except_self(nums: &Vec<i32>) -> Vec<i32> {
    let mut result = vec![];
    for i in 0..nums.len() {
        let product = product_array_except_index(nums, i);
        result.push(product);
    }

    return result;
}

struct TestCase {
    nums: Vec<i32>,
    expected: Vec<i32>,
}

#[test]
fn test_product_array_except_self() {
    let test_cases = vec![
        TestCase {
            nums: vec![1, 2, 3, 4],
            expected: vec![24, 12, 8, 6],
        },
        TestCase {
            nums: vec![-1, 1, 0, -3, 3],
            expected: vec![0, 0, 9, 0, 0],
        },
    ];

    for test_case in test_cases {
        let got = product_array_except_self(&test_case.nums);
        assert_eq!(got, test_case.expected);
    }
}
