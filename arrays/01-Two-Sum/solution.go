package main

func safeIncrement(n int, max int) int {
	if (n + 1) == max {
		return n
	}

	return n + 1
}

func TwoSum(nums []int, target int) (start int, end int) {
	max := len(nums)

	if len(nums) < 2 {
		return -1, -1
	}

	start = 0
	end = 1

	for start < end {
		if nums[start]+nums[end] == target {
			return start, end
		}

		end = safeIncrement(end, max)
		start = safeIncrement(start+1, max-1)

		if start == max-1 {
			break
		}
	}

	return -1, -1
}
