package main

import (
	"testing"
)

type TestCase struct {
	input  []int
	result bool
}

func TestContainsDuplicates(t *testing.T) {
	testCases := []TestCase{
		{
			input:  []int{1, 2, 3, 1},
			result: true,
		},
		{
			input:  []int{1, 2, 3, 4},
			result: false,
		},
		{
			input:  []int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2},
			result: true,
		},
	}

	for _, testCase := range testCases {
		result := ContainsDuplicates(testCase.input)
		if result != testCase.result {
			t.Errorf("expected: %v, got: %v", testCase.result, result)
		}
	}
}
