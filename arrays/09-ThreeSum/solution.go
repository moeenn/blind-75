package main

import (
	"fmt"
	"slices"
)

type Triplet [3]int

func SortedTriplet(a, b, c int) Triplet {
	s := []int{a, b, c}
	slices.Sort(s)
	return Triplet(s)
}

func ThreeSum(nums []int) []Triplet {
	lastIdx := len(nums)
	result := make(map[Triplet]bool)
	resultSlice := []Triplet{}
	if lastIdx < 3 {
		return resultSlice
	}

	a := 0
	b := 1
	c := 2
	sum := 0

	for a < lastIdx-2 {
		sum = nums[a] + nums[b] + nums[c]
		if sum == 0 {
			result[SortedTriplet(nums[a], nums[b], nums[c])] = true
		}

		c++
		if c == lastIdx {
			b++
			c = b + 1
			if b == lastIdx-1 {
				a++
				b = a + 1
				c = b + 1
			}
		}
	}

	// convert map/set to slice
	for key := range result {
		resultSlice = append(resultSlice, key)
	}

	return resultSlice
}

func main() {
	nums := []int{-1, 0, 1, 2, -1, -4}
	result := ThreeSum(nums)
	fmt.Println(result)
}
