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

struct Pair(usize, usize);

impl Pair {
    fn equals(self: &Pair, other: &Pair) -> bool {
        self.0 == other.0 && self.1 == other.1
    }
}

fn get_pairs(nums: &Vec<i32>, target: i32) -> Vec<Pair> {
    let mut result = vec![];
    if nums.len() < 2 {
        return result;
    }

    let mut i = 0;
    let mut j = 1;

    loop {
        if nums[i] + nums[j] == target {
            result.push(Pair(i, j));
        }

        j += 1;
        if j == nums.len() {
            i += 1;
            j = i + 1;
        }

        if i == nums.len() - 1 {
            break;
        }
    }

    return result;
}

struct TestCase {
    nums: Vec<i32>,
    target: i32,
    expected: Vec<Pair>,
}

#[test]
fn test_get_pairs() {
    let test_cases = vec![
        TestCase {
            nums: vec![2, 7, 11, 15],
            target: 9,
            expected: vec![Pair(0, 1)],
        },
        TestCase {
            nums: vec![3, 2, 4],
            target: 6,
            expected: vec![Pair(1, 2)],
        },
        TestCase {
            nums: vec![3, 3],
            target: 6,
            expected: vec![Pair(0, 1)],
        },
    ];

    for test_case in test_cases.iter() {
        let got = get_pairs(&test_case.nums, test_case.target);
        assert_eq!(got.len(), test_case.expected.len());

        for i in 0..got.len() {
            assert!(got[i].equals(&test_case.expected[i]));
        }
    }
}
