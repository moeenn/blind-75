package com.sandbox;

//int[] numbers = {1,8,6,2,5,4,8,3,7};

public class Solution {
  public int mostWater(final int[] heights) {
    assert(heights.length > 1);

    int first = 0;
    int second = 1;
    int maxVolume = 0;
    int volume;

    while (first < second) {
      volume = getVolume(first, second, heights[first], heights[second]);
      if (volume > maxVolume) {
        maxVolume = volume;
      }

      second++;
      if (second == heights.length) {
        first++;
        second = first + 1;
      }

      if (first == heights.length - 1) {
        break;
      }
    }

    return maxVolume;
  }

  private int getVolume(int startIndex, int endIndex, int startValue, int endValue) {
    assert(startIndex < endIndex);

    int delta = endIndex - startIndex;
    int minHeight = Math.min(startValue, endValue);

    return minHeight * delta;
  }
}

