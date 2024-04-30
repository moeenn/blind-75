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
      new TestCase(new int[]{-2,1,-3,4,-1,2,1,-5,4}, 6),
      new TestCase(new int[]{1}, 1),
      new TestCase(new int[]{5,4,-1,7,8}, 23),
    };
    
    for (var testCase : testCases) {
      int result = instance.largestSubArraySum(testCase.numbers);
      assertEquals(result, testCase.result);
    }
  }
}