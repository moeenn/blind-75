package main

import "testing"

type TestCase struct {
	input  []int
	result []int
}

func matchSlices(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}

	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return false
		}
	}

	return true
}

func TestProductOfArrayExcept(t *testing.T) {
	testCases := []TestCase{
		{
			input:  []int{1, 2, 3, 4},
			result: []int{24, 12, 8, 6},
		},
		{
			input:  []int{-1, 1, 0, -3, 3},
			result: []int{0, 0, 9, 0, 0},
		},
	}

	for _, testCase := range testCases {
		result := ProductOfArrayExcept(testCase.input)
		if !matchSlices(testCase.result, result) {
			t.Errorf("expected: %v, got: %v", testCase.result, result)
		}
	}
}
