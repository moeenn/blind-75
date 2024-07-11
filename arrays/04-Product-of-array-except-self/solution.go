package main

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

// TODO: optimizie to run in O(n) time
func ProductOfArrayExcept(nums []int) []int {
	max := len(nums)
	result := []int{}

	for i := 0; i < max; i++ {
		result = append(result, productExcept(nums, i))
	}

	return result
}
