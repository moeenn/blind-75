package com.sandbox;

public class BuyStocks {
  public int maxProfit(final int[] prices) {
    assert(prices.length > 1);
    int max = 0;
    int first = 0;
    int second = 1;
    
    while (first < second) {
      int profit = prices[second] - prices[first];
      if (profit > max) {
        max = profit;
      }
      
      second++;
      if (second == prices.length) {
        first++;
        second = first + 1;
      }

      if (first >= prices.length || second >= prices.length) {
        break;
      }
    }
    
    return max;
  }
}
