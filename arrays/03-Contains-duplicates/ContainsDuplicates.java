package com.sandbox;

public class ContainsDuplicates {
  public boolean check(final int[] numbers) {
    assert(numbers.length > 1);
    int first = 0;
    int second = 1;
    
    while (first < second) {
      if (numbers[first] == numbers[second]) {
        return true;
      }
      
      second++;
      if (second == numbers.length) {
        first++;
        second = first + 1;
      }
      
      if (first >= numbers.length || second >= numbers.length) {
        break;
      }
    }
    
    return false;
  }
}
