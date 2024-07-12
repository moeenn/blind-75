package main

func calculateVolume(startIdx int, endIdx int, startVal int, endVal int) int {
	delta := endIdx - startIdx
	min := min(startVal, endVal)
	return delta * min
}

func ContainerWithMostWater(heigths []int) int {
	lastIdx := len(heigths)
	start := 0
	end := lastIdx - 1
	currentVolume := 0
	maxVolume := 0

	for start < end {
		currentVolume = calculateVolume(start, end, heigths[start], heigths[end])
		if currentVolume > maxVolume {
			maxVolume = currentVolume
		}

		end++
		if end == lastIdx {
			start++
			end = start + 1
		}

		if start == lastIdx-1 {
			break
		}
	}

	return maxVolume
}
