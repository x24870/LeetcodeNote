package main

import (
	"fmt"
	"strings"
)

func main() {
	ans := isPalindrome("A man, a plan, a canal: Panama")
	fmt.Println(ans)
}

func isPalindrome(s string) bool {
	s = strip(s)
	s = strings.ToLower(s)

	left := 0
	right := len(s) - 1

	for left <= right {
		if s[left] != s[right] {
			return false
		}

		left++
		right--
	}

	return true
}

func strip(s string) string {
	new := ""

	for _, b := range s {
		if 'a' <= b && b <= 'z' ||
			'A' <= b && b <= 'Z' ||
			'0' <= b && b <= '9' {
			new += string(b)
		}
	}

	return new
}
