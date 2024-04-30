package com.sandbox;

public class Solution {
  public int largestSubArraySum(final int[] numbers) {
    assert (numbers.length > 0);
    if (numbers.length == 1) return numbers[0];
    
    int start = 0;
    int end = numbers.length - 1;
    int max = 0;
    int sum = 0;
    
    while (start != numbers.length - 1) {
      sum = sumSubArray(numbers, start, end);
      if (sum > max) {
        max = sum;
      }
      
      end--;
      if (end == start) {
        start++;
        end = numbers.length - 1;
      }
    }
    
    return max;
  }
  
  private int sumSubArray(final int[] numbers, int startIndex, int endIndex) {
    int sum = 0;
    for (int i = startIndex; i <= endIndex; i++) {
      sum += numbers[i];
    }
    
    return sum;
  }
}
