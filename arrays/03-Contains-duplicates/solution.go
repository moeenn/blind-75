package main

func ContainsDuplicates(input []int) bool {
	if len(input) < 2 {
		return false
	}

	start := 0
	end := 1
	max := len(input)

	for start < end {
		if input[start] == input[end] {
			return true
		}

		end++
		if end == max {
			start++
			end = start + 1
		}

		if start == max-1 {
			break
		}
	}

	return false
}
