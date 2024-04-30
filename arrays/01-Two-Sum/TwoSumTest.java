package com.sandbox;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TwoSumTest {
  private final TwoSum instance = new TwoSum();
  
  private record TestCase(
    int[] numbers,
    int target,
    Tuple result
  ) {}
  
  @Test
  public void  TestScenarios() {
    TestCase[] testCases = {
      new TestCase(new int[]{2, 7, 11, 15}, 9, new Tuple(0, 1)),
      new TestCase(new int[]{3,2,4}, 6, new Tuple(1, 2)),
      new TestCase(new int[]{3,3}, 6, new Tuple(0, 1)),
      new TestCase(new int[]{3,4,5,6}, 12, new Tuple(-1, -1)),
    };
    
    for (var testCase : testCases) {
      var result = instance.twoSum(testCase.numbers, testCase.target);
      assertEquals(testCase.result.a(), result.a());
      assertEquals(testCase.result.b(), result.b());
    }
  }
}