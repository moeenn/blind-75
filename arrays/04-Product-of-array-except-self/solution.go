package main

import (
	"fmt"
)

func productExcept(nums []int, idx int) int {
	sum := 1

	for i := 0; i < len(nums); i++ {
		if i == idx {
			continue
		}

		sum *= nums[i]
	}

	return sum
}

func ProductOfArrayExcept(nums []int) []int {
	max := len(nums)
	result := []int{}

	for i := 0; i < max; i++ {
		result = append(result, productExcept(nums, i))
	}

	return result
}

func main() {
	nums := []int{1, 2, 3, 4}
	result := ProductOfArrayExcept(nums)
	fmt.Println(result)
}
