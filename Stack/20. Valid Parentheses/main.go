package main

// n = len(s)
// time complexity: O(n)
// space complexity: O(n)
func isValid(s string) bool {
	stack := make([]rune, 0, len(s))

	for _, r := range s {
		if len(stack) == 0 || r == '(' || r == '[' || r == '{' {
			stack = append(stack, r)
			continue
		}

		// there is a close bracket but no open bracket
		if len(stack) == 0 {
			return false
		}

		// check if the last open bracket is match to current clost bracket
		if r == ')' && stack[len(stack)-1] == '(' ||
			r == ']' && stack[len(stack)-1] == '[' ||
			r == '}' && stack[len(stack)-1] == '{' {
			stack = stack[:len(stack)-1]
			continue
		}

		return false
	}

	// check if there is unclosed bracket
	if len(stack) != 0 {
		return false
	}

	return true
}
