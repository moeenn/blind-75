package main

import (
	"testing"
)

type TestCase struct {
	input  []int
	result []Triplet
}

func tripletSliceEquals(a, b []Triplet) bool {
	// TODO: complete implementation
	return true
}
func TestThreeSum(t *testing.T) {
	testCases := []TestCase{
		{
			input: []int{-1, 0, 1, 2, -1, -4},
			result: []Triplet{
				{-1, 0, 1},
				{-1, -1, 2},
			},
		},
		{
			input:  []int{0, 1, 1},
			result: []Triplet{},
		},
		{
			input: []int{0, 0, 0},
			result: []Triplet{
				{0, 0, 0},
			},
		},
	}

	for _, tc := range testCases {
		result := ThreeSum(tc.input)
		if !tripletSliceEquals(result, tc.result) {
			t.Errorf("expected: %+v, got: %+v", tc.result, result)
		}
	}
}
