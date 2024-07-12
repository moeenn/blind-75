package main

import (
	"testing"
)

type TestCase struct {
	input  []int
	result int
}

func TestContainerWithMostWater(t *testing.T) {
	testCases := []TestCase{
		{
			input:  []int{1, 8, 6, 2, 5, 4, 8, 3, 7},
			result: 49,
		},
		{
			input:  []int{1, 1},
			result: 1,
		},
	}

	for _, tc := range testCases {
		result := ContainerWithMostWater(tc.input)
		if result != tc.result {
			t.Errorf("expected: %d, got: %d", tc.result, result)
		}
	}
}
