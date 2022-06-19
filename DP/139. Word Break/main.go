package main

import "strings"

// m = len(s), n = len(wordDict)
// time complexity: O(m*n * m)
// space complexity: O(m*m + m*n)
// top down - recursive
func wordBreakRecursive(s string, wordDict []string) bool {
	memo := make(map[string]bool)
	return dfs(s, wordDict, memo)
}

func dfs(s string, wordDict []string, memo map[string]bool) bool {
	if m, ok := memo[s]; ok {
		return m
	}

	if s == "" {
		return true
	}

	for _, w := range wordDict {
		if strings.HasPrefix(s, w) && len(s) >= len(w) {
			subStr := s[len(w):]
			if dfs(subStr, wordDict, memo) {
				memo[subStr] = true
				return true
			}
		}
	}

	memo[s] = false
	return false
}

// bottom up - iteration
// m = len(s), n = len(wordDict)
// time complexity: O(m*n)
// space complexity: O(m)
func wordBreak(s string, wordDict []string) bool {
	table := make([]bool, len(s)+1)
	table[0] = true

	for i := 0; i < len(table); i++ {
		if table[i] == true {
			subStr := s[i:]
			for _, w := range wordDict {
				if strings.HasPrefix(subStr, w) && i+len(w) < len(table) {
					table[i+len(w)] = true
				}
			}
		}
	}

	return table[len(table)-1]
}
