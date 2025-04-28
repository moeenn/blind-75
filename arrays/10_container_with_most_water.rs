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
fn most_water(heights: &Vec<i32>) -> i32 {
    if heights.len() < 2 {
        return 0;
    }

    let mut left = 0;
    let mut right = 1;
    let mut max_volume = 0;

    loop {
        let distance: i32 = (right - left) as i32;
        let min_height = heights[left].min(heights[right]);
        let volume = distance * min_height;

        if volume > max_volume {
            max_volume = volume;
        }

        right += 1;
        if right == heights.len() {
            left += 1;
            right = left + 1;
        }

        if left == heights.len() - 1 {
            break;
        }
    }

    return max_volume;
}

struct TestCase {
    heights: Vec<i32>,
    expected: i32,
}

#[test]
fn test_most_water() {
    let test_cases = vec![
        TestCase {
            heights: vec![1, 8, 6, 2, 5, 4, 8, 3, 7],
            expected: 49,
        },
        TestCase {
            heights: vec![1, 1],
            expected: 1,
        },
    ];

    for test_case in test_cases {
        let got = most_water(&test_case.heights);
        assert_eq!(got, test_case.expected);
    }
}
