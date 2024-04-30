package com.sandbox;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
  private final Solution instance = new Solution();
  
  private record TestCase(
    int[] numbers,
    int[] result
  ) {}
  
  @Test
  public void TestSolution() {
    TestCase[] testCases = {
      new TestCase(new int[]{1,2,3,4}, new int[]{24, 12, 8, 6}),
      new TestCase(new int[]{-1, 1, 0, -3, 3}, new int[]{0, 0, 9, 0, 0}),
    };
    
    for (var testCase : testCases) {
      int[] result = instance.productExceptSelf(testCase.numbers);
      assertArrayEquals(result, testCase.result);
    }
  }
}