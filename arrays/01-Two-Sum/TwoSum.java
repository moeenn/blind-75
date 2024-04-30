package com.sandbox;

public class TwoSum {
  public Tuple twoSum(final int[] numbers, int target) {
    assert(numbers.length >= 2);
    
    int first = 0;
    int second = 1;
    
    while (first < second) {
      int sum = numbers[first] + numbers[second];
      
      if (sum == target) {
        return new Tuple(first, second);
      }
      
      first++;
      
      if ((first + 1) == numbers.length) {
        break;
      }
      
      second = first + 1;
    }
    
    return new Tuple(-1, -1);
  }
}
