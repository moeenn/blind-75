package main

func BestTimeToBuyStocks(prices []int) int {
	if len(prices) < 2 {
		return 0
	}

	start := 0
	end := 1
	maxProfit := 0
	profit := 0

	for start < end {
		profit = prices[end] - prices[start]
		if profit > maxProfit {
			maxProfit = profit
		}

		end++
		if end == len(prices) {
			start++
			end = start + 1
		}

		if start == len(prices)-1 {
			break
		}
	}

	return maxProfit
}
