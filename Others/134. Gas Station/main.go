package main

// origin solution
func canCompleteCircuit(gas []int, cost []int) int {
	start := 0
	length := len(gas)
	for start < length {
		tank := 0
		step := length
		cur := start
		for step > 0 {
			tank += gas[cur]
			tank -= cost[cur]
			// if ran out of gas,
			// means the start station to the end station are invalid
			if tank < 0 {
				// skip invalid stations
				if start < cur {
					start = cur
				}
				break
			}

			// if there is more steps to go after arrived last station,
			// go back to first station
			cur++
			if cur >= length {
				cur = 0
			}

			step--
		}

		// found the valid start station
		if step == 0 {
			return start
		}
		start++
	}

	// not found
	return -1
}

func canCompleteCircuitCandidate(gas []int, cost []int) int {
	length := len(gas)

	// find candidate
	start := 0
	cur := start
	tank := 0
	for cur < length {
		tank += gas[cur]
		tank -= cost[cur]
		cur++
		if tank < 0 {
			// skip invalid stations
			start = cur
			// reset tank
			tank = 0
		}
	}

	// start is the ONLY cadidate
	// so just needs to make sure:
	// from [0 to candidate-1] + [candidate to end] >= 0
	tank = 0
	for i := range gas {
		tank += gas[i]
		tank -= cost[i]
	}

	if tank >= 0 {
		return start
	}
	return -1
}
