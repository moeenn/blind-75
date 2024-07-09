package main

import (
	"testing"
)

type TestCase struct {
	Input  []int
	Result int
}

func TestBestTimeToBuyStocks(t *testing.T) {
	testCases := []TestCase{
		{
			Input:  []int{7, 1, 5, 3, 6, 4},
			Result: 5,
		},
		{
			Input:  []int{7, 6, 4, 3, 1},
			Result: 0,
		},
	}

	for _, testCase := range testCases {
		result := BestTimeToBuyStocks(testCase.Input)
		if result != testCase.Result {
			t.Errorf("invalid result: %d, expected: %d", result, testCase.Result)
		}
	}
}
