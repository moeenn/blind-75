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
      new TestCase(new int[]{1,8,6,2,5,4,8,3,7}, 49),
      new TestCase(new int[]{1,1}, 1),
    };
    
    for (var testCase : testCases) {
      int result = instance.mostWater(testCase.numbers);
      assertEquals(result, testCase.result);
    }
  }
}