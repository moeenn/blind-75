package main

func arrayProduct(nums []int, startIdx int, endIdx int) int {
	product := 1
	for i := startIdx; i <= endIdx; i++ {
		product *= nums[i]
	}
	return product
}

func MaxProductSubarray(nums []int) int {
	maxIdx := len(nums)
	first := 0
	second := maxIdx - 1
	product := 0
	maxProduct := 0

	for first < second {
		product = arrayProduct(nums, first, second)
		if product > maxProduct {
			maxProduct = product
		}

		second--
		if second == first {
			second = maxIdx - 1
			first++
		}

		if first == maxIdx-1 {
			break
		}
	}

	return maxProduct
}
