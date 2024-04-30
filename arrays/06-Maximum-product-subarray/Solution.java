package com.sandbox;

public class Solution {
  public int largestSubArrayProduct(final int[] numbers) {
    assert (numbers.length > 0);
    if (numbers.length == 1) return numbers[0];
    
    int start = 0;
    int end = numbers.length - 1;
    int max = 0;
    int product = 0;
    
    while (start != numbers.length - 1) {
      product = productSubArray(numbers, start, end);
      if (product > max) {
        max = product;
      }
      
      end--;
      if (end == start) {
        start++;
        end = numbers.length - 1;
      }
    }
    
    return max;
  }
  
  private int productSubArray(final int[] numbers, int startIndex, int endIndex) {
    assert(startIndex < endIndex);
    assert(startIndex > -1);
    assert(numbers.length > startIndex);
    assert(numbers.length > endIndex);
    
    int product = numbers[startIndex];
    for (int i = startIndex + 1; i <= endIndex; i++) {
      product *= numbers[i];
    }
    return product;
  }
}
