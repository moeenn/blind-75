package com.sandbox;

public class Solution {
  public int[] productExceptSelf(final int[] numbers) {
    assert (numbers.length > 1);
    int current = 0;
    int max = numbers.length - 1;
    int[] result = new int[numbers.length];
    Integer sum = null;
    
    while (true) {
      for (int i = 0; i <= max; i++) {
        if (i == current) continue;
        if (sum == null) {
          sum = numbers[i];
        } else {
          sum *= numbers[i];
        }
      }
      
      result[current] = sum;
      current++;
      sum = null;
      
      if (current == numbers.length) {
        break;
      }
    }
    
    return result;
  }
}
