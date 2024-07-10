package main

import (
	"testing"
)

type TestCase struct {
	input  []int
	result int
}

func TestMaximumSubarray(t *testing.T) {
	testCases := []TestCase{
		{
			input:  []int{-2, 1, -3, 4, -1, 2, 1, -5, 4},
			result: 6,
		},
		{
			input:  []int{1},
			result: 1,
		},
		{
			input:  []int{5, 4, -1, 7, 8},
			result: 23,
		},
	}

	for _, testCase := range testCases {
		result := MaximumSubarray(testCase.input)
		if testCase.result != result {
			t.Errorf("expected: %d, got: %d", testCase.result, result)
		}
	}
}
