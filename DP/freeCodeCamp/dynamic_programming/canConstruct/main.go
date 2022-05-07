package main

import (
	"fmt"
	"strings"
)

// m = len(target), n = len(words)
// time complexity: O(n^m * m)
// space complexity: O(m * m) // each stack has to store a len(target) string
func canConstruct(target string, words []string) bool {
	if target == "" {
		return true
	}

	for _, w := range words {
		if strings.HasPrefix(target, w) {
			subStr := strings.TrimPrefix(target, w)
			if canConstruct(subStr, words) == true {
				return true
			}
		}
	}

	return false
}

// time complexity: O(n*m * m)
// space complexity: O(m * m)
func canConstructMemo(target string, words []string, memo map[string]bool) bool {
	if m, ok := memo[target]; ok == true {
		return m
	}
	if target == "" {
		return true
	}

	for _, w := range words {
		if strings.HasPrefix(target, w) {
			subStr := strings.TrimPrefix(target, w)
			if canConstructMemo(subStr, words, memo) == true {
				memo[target] = true
				return memo[target]
			}
		}
	}

	memo[target] = false
	return memo[target]
}

func main() {
	fmt.Println(canConstruct("abcdef", []string{"ab", "abc", "cd", "def", "abcd"}))                  // true
	fmt.Println(canConstruct("skateboard", []string{"bo", "rd", "ate", "t", "ska", "sk", "boar"}))   //false
	fmt.Println(canConstruct("enterapotentpot", []string{"a", "p", "ent", "enter", "ot", "o", "t"})) // true

	memo := make(map[string]bool)
	fmt.Println(canConstructMemo("abcdef", []string{"ab", "abc", "cd", "def", "abcd"}, memo))                  // true
	fmt.Println(canConstructMemo("skateboard", []string{"bo", "rd", "ate", "t", "ska", "sk", "boar"}, memo))   //false
	fmt.Println(canConstructMemo("enterapotentpot", []string{"a", "p", "ent", "enter", "ot", "o", "t"}, memo)) // true
	fmt.Println(canConstructMemo("eeeeeeeeeeeeeeeeeeeeeeeeeeef", []string{
		"e",
		"ee",
		"eee",
		"eeee",
		"eeeee",
		"eeeeee",
	}, memo)) // false
}
