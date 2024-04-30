package com.sandbox;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BuyStocksTest {
  private BuyStocks instance = new BuyStocks();
  
  private record TestCase(
    int[] numbers,
    int result
  ) {}
  
  @Test
  public void TestScenarios() {
    TestCase[] testCases = {
      new TestCase(new int[]{7,1,5,3,6,4}, 5),
      new TestCase(new int[]{7,6,4,3,1}, 0),
    };
    
    for (var testCase : testCases) {
      int result = instance.maxProfit(testCase.numbers);
      assertEquals(result, testCase.result);
    }
  }
}