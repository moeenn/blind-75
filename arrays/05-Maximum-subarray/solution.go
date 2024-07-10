package main

import (
	"fmt"
)

func sumSubarray(nums []int, startIdx int, endIdx int) int {
	sum := 0
	for i := startIdx; i <= endIdx; i++ {
		sum += nums[i]
	}
	return sum
}

func MaximumSubarray(nums []int) int {
	max := len(nums)
	if max == 1 {
		return nums[0]
	}

	start := 0
	end := max - 1
	result := 0
	current := 0

	for start < end {
		current = sumSubarray(nums, start, end)
		if current > result {
			result = current
		}

		end--
		if end == start {
			start++
			end = max - 1
		}

		if start == max-1 {
			break
		}
	}

	return result
}

func main() {
	input := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	result := MaximumSubarray(input)
	fmt.Println(result)
}
