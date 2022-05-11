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

// time complexity: O(m * n * m)
// space complexity: O(m)
func canConstructTable(target string, words []string) bool {
	table := make([]bool, len(target)+1)

	// considering target = "abcdef", if the index contains true which means
	// there is a way to construct the sub-string before current charactor
	// so the first value of the table always be true.
	// which means there is always a way to construct an empty string.
	//  0 1 2 3 4 5 6
	// |T|F|F|F|F|F|F|
	//  a b c d e f
	table[0] = true

	for idx, v := range table {
		if v == true {
			for _, w := range words {
				start := idx
				end := idx + len(w)
				if end <= len(target) && w == target[start:end] {
					table[end] = true
				}
			}
		}
	}

	return table[len(target)]
}

func main() {
	fmt.Println(canConstruct("abcdef", []string{"ab", "abc", "cd", "def", "abcd"}))                  // true
	fmt.Println(canConstruct("skateboard", []string{"bo", "rd", "ate", "t", "ska", "sk", "boar"}))   //false
	fmt.Println(canConstruct("enterapotentpot", []string{"a", "p", "ent", "enter", "ot", "o", "t"})) // true
	fmt.Println("---")

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
	fmt.Println("---")

	fmt.Println(canConstructTable("abcdef", []string{"ab", "abc", "cd", "def", "abcd"}))                  // true
	fmt.Println(canConstructTable("skateboard", []string{"bo", "rd", "ate", "t", "ska", "sk", "boar"}))   //false
	fmt.Println(canConstructTable("enterapotentpot", []string{"a", "p", "ent", "enter", "ot", "o", "t"})) // true
	fmt.Println(canConstructTable("eeeeeeeeeeeeeeeeeeeeeeeeeeef", []string{
		"e",
		"ee",
		"eee",
		"eeee",
		"eeeee",
		"eeeeee",
	})) // false
}
