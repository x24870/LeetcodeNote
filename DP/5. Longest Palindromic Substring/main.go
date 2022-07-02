package main

// recursive solution - limit time exceeded
func longestPalindrome(s string) string {
	if len(s) <= 1 {
		return s
	}
	var max string
	memo := make(map[string]bool)
	dfs(&s, 0, len(s)-1, &max, memo)
	return max
}

func dfs(s *string, i, j int, max *string, memo map[string]bool) bool {
	if i >= j {
		if j-i+1 > len(*max) {
			*max = (*s)[i : j+1]
		}
		return true
	}
	if v, ok := memo[(*s)[i:j+1]]; ok {
		return v
	}

	ret := false
	if (*s)[i] == (*s)[j] && dfs(s, i+1, j-1, max, memo) {
		if j-i+1 > len(*max) {
			*max = (*s)[i : j+1]
		}
		ret = true
	} else {
		dfs(s, i+1, j, max, memo)
		dfs(s, i, j-1, max, memo)
	}

	memo[(*s)[i:j+1]] = ret
	return ret
}

// tabulation
// n = len(s)
// time complexity: O(n*n)
// space complexity: O(n)
func longestPalindromeTable(s string) string {
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
