package main

import (
	"testing"
)

type TestCase struct {
	input  []int
	result int
}

func TestMaxProductSubarray(t *testing.T) {
	testCases := []TestCase{
		{
			input:  []int{2, 3, -2, 4},
			result: 6,
		},
		{
			input:  []int{-2, 0, -1},
			result: 0,
		},
	}

	for _, tc := range testCases {
		result := MaxProductSubarray(tc.input)
		if result != tc.result {
			t.Errorf("expected: %d, got: %d", tc.result, result)
		}
	}
}
