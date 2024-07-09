package main

import (
	"testing"
)

type TestCase struct {
	input       []int
	target      int
	resultStart int
	resultEnd   int
}

func TestTwoSum(t *testing.T) {
	testCases := []TestCase{
		{
			input:       []int{2, 7, 11, 15},
			target:      9,
			resultStart: 0,
			resultEnd:   1,
		},
		{
			input:       []int{3, 2, 4},
			target:      6,
			resultStart: 1,
			resultEnd:   2,
		},
		{
			input:       []int{3, 3},
			target:      6,
			resultStart: 0,
			resultEnd:   1,
		},
		{
			input:       []int{3, 4, 5, 6},
			target:      12,
			resultStart: -1,
			resultEnd:   -1,
		},
	}

	for _, testCase := range testCases {
		start, end := TwoSum(testCase.input, testCase.target)
		if start != testCase.resultStart {
			t.Errorf("start mismatch: expected: %d, got: %d", testCase.resultStart, start)
		}

		if end != testCase.resultEnd {
			t.Errorf("end mismatch: expected: %d, got: %d", testCase.resultEnd, end)
		}
	}
}
