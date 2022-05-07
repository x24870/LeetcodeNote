package main

import (
	"fmt"
	"strings"
)

// m = len(target), n = len(words)
// time complexity: O(n^m * m)
// space complexity: O(m * m)
func countConstruct(target string, words []string) int {
	if target == "" {
		return 1
	}

	total := 0
	for _, w := range words {
		if strings.HasPrefix(target, w) {
			subStr := strings.TrimPrefix(target, w)
			total += countConstruct(subStr, words)
		}
	}

	return total
}

// time complexity: O(m * n * m)
// space complexity: O(m * m)
func countConstructMemo(target string, words []string, memo map[string]int) int {
	if m, ok := memo[target]; ok == true {
		return m
	}
	if target == "" {
		return 1
	}

	total := 0
	for _, w := range words {
		if strings.HasPrefix(target, w) {
			subStr := strings.TrimPrefix(target, w)
			total += countConstructMemo(subStr, words, memo)
		}
	}

	memo[target] = total
	return total
}

func main() {
	fmt.Println(countConstruct("abcdef", []string{"ab", "abc", "cd", "def", "abcd"}))                  // 1
	fmt.Println(countConstruct("skateboard", []string{"bo", "rd", "ate", "t", "ska", "sk", "boar"}))   // 0
	fmt.Println(countConstruct("enterapotentpot", []string{"a", "p", "ent", "enter", "ot", "o", "t"})) // 4
	fmt.Println(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeee", []string{
		"e",
		"ee",
		"eee",
		"eeee",
		"eeeee",
		"eeeeee",
	})) // 56058368

	m := make(map[string]int)
	fmt.Println(countConstructMemo("eeeeeeeeeeeeeeeeeeeeeeeeeee", []string{
		"e",
		"ee",
		"eee",
		"eeee",
		"eeeee",
		"eeeeee",
	}, m)) // 56058368
}
