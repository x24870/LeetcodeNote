package main

import (
	"fmt"
	"strings"
)

// m = len(target), n = len(words)
// time complexity: O(n^m * m)
// space complexity: O(n^m)
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

// time complexity: O(n^m)
// space complexity: O(n^m)
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

// time complexity: O(n^m)
// space complexity: O(n^m)
func allConstructTable(target string, words []string) [][]string {
	table := make([][][]string, len(target)+1)

	for i := range table {
		table[i] = [][]string{}
	}

	// init table, considering if target is an empty string, which means it takes no word to match the target.
	// So the it will be [[]]
	table[0] = append(table[0], []string{})

	for i := 0; i < len(table); i++ {
		for _, w := range words {
			start := i
			end := start + len(w)
			if end < len(table) && w == target[start:end] {
				for _, way := range table[start] {
					// make a new slice, it may use the same pointer if append the word directly
					newWay := make([]string, len(way))
					copy(newWay, way)
					newWay = append(newWay, w)
					table[end] = append(table[end], newWay)
				}
			}
		}
	}

	return table[len(target)]
}

func main() {
	fmt.Println(allConstruct("abcdef", []string{"ab", "abc", "cd", "def", "abcd"}))
	fmt.Println(allConstruct("skateboard", []string{"bo", "rd", "ate", "t", "ska", "sk", "boar"}))
	fmt.Println(allConstruct("enterapotentpot", []string{"a", "p", "ent", "enter", "ot", "o", "t"}))
	// fmt.Println(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeez", []string{
	// 	"e",
	// 	"ee",
	// 	"eee",
	// 	"eeee",
	// 	"eeeee",
	// 	"eeeeee",
	// }))
	fmt.Println("---")

	memo := make(map[string][][]string)
	fmt.Println(allConstructMemo("eeeeeeeeeeeeeeeeeeeeeeeeeeez", []string{
		"e",
		"ee",
		"eee",
		"eeee",
		"eeeee",
		"eeeeee",
	}, memo))
	fmt.Println("---")

	fmt.Println(allConstructTable("abcdef", []string{"ab", "abc", "cd", "def", "ef", "abcd"}))
	fmt.Println(allConstructTable("skateboard", []string{"bo", "rd", "ate", "t", "ska", "sk", "boar"}))
	fmt.Println(allConstructTable("enterapotentpot", []string{"a", "p", "ent", "enter", "ot", "o", "t"}))
}
