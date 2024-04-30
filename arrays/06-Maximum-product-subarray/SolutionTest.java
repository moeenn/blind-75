package com.sandbox;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
  private final Solution instance = new Solution();
  
  private record TestCase(
    int[] numbers,
    int result
  ) {}
  
  @Test
  public void TestSolution() {
    TestCase[] testCases = {
      new TestCase(new int[]{2,3,-2,4}, 6),
      new TestCase(new int[]{-2,0,-1}, 0),
    };
    
    for (var testCase : testCases) {
      int result = instance.largestSubArrayProduct(testCase.numbers);
      assertEquals(result, testCase.result);
    }
  }
}