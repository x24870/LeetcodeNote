package main

// time complexity: O(1+2+3+...n)
// space complexity: O(n)
func removeDuplicatesBrut(s string) string {
	idx := 0
	for idx < len(s)-1 {
		if s[idx] == s[idx+1] {
			s = s[:idx] + s[idx+2:]
			idx = 0
		} else {
			idx++
		}

	}

	return s
}

// time complexity: O(n)
// space complexity: O(n)
func removeDuplicates(s string) string {
	stack := make([]rune, 0, len(s))

	for _, v := range s {
		if len(stack) != 0 && stack[len(stack)-1] == v {
			// pop
			stack = stack[:len(stack)-1]
			continue
		}
		stack = append(stack, v)
	}

	return string(stack)
}
