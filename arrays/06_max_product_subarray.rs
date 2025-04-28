/**
Given an integer array `nums`, find a subarray that has the largest `product`, and return the `product`.
The test cases are generated so that the answer will fit in a 32-bit integer.

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
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
```
*/
fn product_subarray(nums: &Vec<i32>, start_idx: usize, end_idx: usize) -> i32 {
    assert!(end_idx < nums.len());
    assert!(start_idx < end_idx);

    let mut product = nums[start_idx];
    for i in start_idx + 1..=end_idx {
        product *= nums[i];
    }

    return product;
}

fn max_subarray_product(nums: &Vec<i32>) -> i32 {
    if nums.len() == 0 {
        return 0;
    }

    if nums.len() == 1 {
        return nums[0];
    }

    let mut left = 0;
    let mut right = 1;
    let mut max_product: Option<i32> = None;

    loop {
        let product = product_subarray(nums, left, right);
        if let None = max_product {
            max_product = Some(product);
        }

        if let Some(current_max) = max_product {
            if product > current_max {
                max_product = Some(product);
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

    return max_product.unwrap_or(0);
}

struct TestCase {
    nums: Vec<i32>,
    expected: i32,
}

#[test]
fn test_max_subarray_product() {
    let test_cases = vec![
        TestCase {
            nums: vec![2, 3, -2, 4],
            expected: 6,
        },
        TestCase {
            nums: vec![-2, 0, -1],
            expected: 0,
        },
    ];

    for test_case in test_cases {
        let got = max_subarray_product(&test_case.nums);
        assert_eq!(got, test_case.expected);
    }
} 
