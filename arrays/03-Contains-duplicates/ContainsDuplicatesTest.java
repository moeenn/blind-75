package com.sandbox;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ContainsDuplicatesTest {
  private final ContainsDuplicates instance = new ContainsDuplicates();
  
  private record TestCase(
    int[] numbers,
    boolean result
  ) {}
  
  @Test
  public void TestScenarios() {
    TestCase[] testCases = {
      new TestCase(new int[]{1,2,3,1}, true),
      new TestCase(new int[]{1,2,3,4}, false),
      new TestCase(new int[]{1,1,1,3,3,4,3,2,4,2}, true),
    };
    
    for (var testCase : testCases) {
      var result = instance.check(testCase.numbers);
      assertEquals(result, testCase.result);
    }
  }
}