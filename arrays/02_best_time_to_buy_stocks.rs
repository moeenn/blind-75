/**
You are given an array prices where `prices[i]` is the price of a given stock on the `ith` day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

Example 2:
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

Constraints:
```
1 <= prices.length <= 105
0 <= prices[i] <= 104
```
*/

fn get_max_profit(prices: &Vec<i32>) -> i32 {
    if prices.len() < 2 {
        return 0;
    }

    let mut max_profit = 0;
    let mut profit = 0;
    let mut buy = 0;
    let mut sell = 1;

    loop {
        profit = prices[sell] - prices[buy];
        if profit > max_profit {
            max_profit = profit;
        }

        sell += 1;
        if sell == prices.len() {
            buy += 1;
            sell = buy + 1;
        }

        if buy == prices.len() -1 {
            break;
        }
    }

    return max_profit
}

struct TestCase {
    prices: Vec<i32>,
    expected: i32
}

#[test]
fn test_get_max_profit() {
    let test_cases = vec![
        TestCase {
            prices: vec![7,1,5,3,6,4],
            expected: 5,
        },
        TestCase {
            prices: vec![7,6,4,3,1],
            expected: 0,
        },
    ];

    for test_case in test_cases {
        let got = get_max_profit(&test_case.prices);
        assert_eq!(got, test_case.expected);
    }
}
