package com.sandbox;

public class Solution {
  public int mostWater(final int[] numbers) {
    assert(numbers.length > 1);
    int first = 0;
    int second = 1;
    int volume = 0;
    Integer maxVolume = null;
    
    while (first < second) {
      System.out.printf("first: %d, second: %d\n", first, second);
      volume = getVolume(first, second, numbers[first], numbers[second]);
      if (maxVolume == null) {
        maxVolume = volume;
      } else {
        if (volume > maxVolume) {
          maxVolume = volume;
        }
      }
      
      second++;
      if (second == numbers.length) {
        first++;
        second = first + 1;
      }
      
      if (first == numbers.length - 2 && second == numbers.length - 1) {
        break;
      }
    }
    
    return maxVolume.intValue();
  }
  
  private int getVolume(int startIndex, int endIndex, int startValue, int endValue) {
    assert(startIndex < endIndex);
    int delta = endIndex - startIndex;
    int min = Math.min(startValue, endValue);
    
    return min * delta;
  }
}
