package main

// tabulation
// n = len(s)
// time complexity: O(n*n)
// space complexity: O(n)
func longestPalindrome(s string) string {
	var max string
	for i := 0; i < len(s); i++ {
		maxPalindrome(s, i, i, &max)
		maxPalindrome(s, i, i+1, &max)
	}
	return max
}

func maxPalindrome(s string, i, j int, max *string) {
	for i >= 0 && j < len(s) && s[i] == s[j] {
		sub := s[i : j+1]
		if len(sub) > len(*max) {
			*max = sub
		}
		i--
		j++
	}
}
