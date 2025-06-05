/**
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j, i != k, and j != k`, and `nums[i] + nums[j] + nums[k] == 0`. Notice that the solution set must not contain duplicate triplets.

## Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

## Example 2:
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

## Example 3:
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```
*/
struct Triplet(i32, i32, i32);

impl Triplet {
    fn equals(self: &Triplet, other: &Triplet) -> bool {
        let sum = other.0 + other.1 + other.2;
        let self_sum = self.0 + self.1 + self.2;

        let product = other.0 * other.1 * other.2;
        let self_product = self.0 * self.1 * self.2;

        return self_product == product && self_sum == sum;
    }
}

#[test]
fn test_triplet_equals() {
    struct TestCase {
        a: Triplet,
        b: Triplet,
        expected: bool,
    }

    let test_cases = vec![
        TestCase {
            a: Triplet(3, 2, 1),
            b: Triplet(1, 2, 3),
            expected: true,
        },
        TestCase {
            a: Triplet(1, 2, 3),
            b: Triplet(2, 3, 1),
            expected: true,
        },
        TestCase {
            a: Triplet(-1, 0, 1),
            b: Triplet(0, 1, -1),
            expected: true,
        },
        TestCase {
            a: Triplet(4, 5, 6),
            b: Triplet(2, 3, 1),
            expected: false,
        },
    ];

    for test_case in test_cases {
        let got = test_case.a.equals(&test_case.b);
        assert_eq!(got, test_case.expected);
    }
}

fn vec_includes_triplet(v: &Vec<Triplet>, target: &Triplet) -> bool {
    for item in v.iter() {
        if item.equals(target) {
            return true;
        }
    }
    false
}

fn three_sum(nums: &Vec<i32>, target: i32) -> Vec<Triplet> {
    let mut result = vec![];
    if nums.len() < 3 {
        return result;
    }

    let mut a = 0;
    let mut b = 1;
    let mut c = 2;

    loop {
        let sum = nums[a] + nums[b] + nums[c];
        if sum == target {
            let triplet = Triplet(nums[a], nums[b], nums[c]);
            if !vec_includes_triplet(&result, &triplet) {
                result.push(Triplet(nums[a], nums[b], nums[c]));
            }
        }

        c += 1;
        if c == nums.len() {
            b += 1;
            c = b + 1;
        }

        if b == nums.len() - 1 {
            a += 1;
            b = a + 1;
            c = b + 1;
        }

        if a == nums.len() - 2 {
            break;
        }
    }

    return result;
}

#[test]
fn test_three_sum() {
    struct TestCase {
        input: Vec<i32>,
        expected: Vec<Triplet>,
    }

    let test_cases = vec![
        TestCase {
            input: vec![-1, 0, 1, 2, -1, -4],
            expected: vec![Triplet(-1, -1, 2), Triplet(-1, 0, 1)],
        },
        TestCase {
            input: vec![0, 1, 1],
            expected: vec![],
        },
        TestCase {
            input: vec![0, 0, 0],
            expected: vec![Triplet(0, 0, 0)],
        },
    ];

    for test_case in test_cases {
        let got = three_sum(&test_case.input, 0);
        assert_eq!(got.len(), test_case.expected.len());

        for got_triplet in got.iter() {
            let is_found = vec_includes_triplet(&test_case.expected, got_triplet);
            assert!(is_found);
        }
    }
}

