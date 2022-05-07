package main

import (
	"fmt"
	"strings"
)

// m = len(target), n = len(words)
// time complexity: O(n^m * m)
// space complexity: O(m * m * m)
func allConstruct(target string, words []string) [][]string {
	if target == "" {
		// return [[]]
		return make([][]string, 1)
	}

	var allWay [][]string // not initailize (nil)
	for _, w := range words {
		if strings.HasPrefix(target, w) {
			subStr := strings.TrimPrefix(target, w)
			ways := allConstruct(subStr, words)
			// append the prefix
			for i := range ways {
				// append to first
				ways[i] = append([]string{w}, ways[i]...)
			}

			allWay = append(allWay, ways...)
		}
	}

	return allWay
}

// time complexity: O(n*m * m)
// space complexity: O(m * m * m)
func allConstructMemo(target string, words []string, memo map[string][][]string) [][]string {
	if way, ok := memo[target]; ok == true {
		return way
	}
	if target == "" {
		// return [[]]
		return make([][]string, 1)
	}

	var allWay [][]string // not initailize (nil)
	for _, w := range words {
		if strings.HasPrefix(target, w) {
			subStr := strings.TrimPrefix(target, w)
			ways := allConstructMemo(subStr, words, memo)
			// append the prefix
			for i := range ways {
				// append to first
				ways[i] = append([]string{w}, ways[i]...)
			}

			allWay = append(allWay, ways...)

		}
	}

	memo[target] = allWay
	return allWay
}

func main() {
	fmt.Println(allConstruct("abcdef", []string{"ab", "abc", "cd", "def", "abcd"}))
	fmt.Println(allConstruct("skateboard", []string{"bo", "rd", "ate", "t", "ska", "sk", "boar"}))
	fmt.Println(allConstruct("enterapotentpot", []string{"a", "p", "ent", "enter", "ot", "o", "t"}))
	fmt.Println(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeez", []string{
		"e",
		"ee",
		"eee",
		"eeee",
		"eeeee",
		"eeeeee",
	}))

	memo := make(map[string][][]string)
	fmt.Println(allConstructMemo("eeeeeeeeeeeeeeeeeeeeeeeeeeez", []string{
		"e",
		"ee",
		"eee",
		"eeee",
		"eeeee",
		"eeeeee",
	}, memo))

}
