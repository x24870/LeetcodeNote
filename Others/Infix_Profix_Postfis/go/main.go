package main

import (
	"fmt"
	"strconv"
)

// do not considering priority
// assume all number is between 0-9
func infix2postfix(input string) string {
	stack := []uint8{}
	output := ""

	for idx := range input {
		if isNum(input[idx]) {
			output += string(input[idx])
		} else {
			for len(stack) > 0 {
				last := len(stack) - 1
				output += string(stack[last])
				stack = stack[:last]
			}

			stack = append(stack, input[idx])
		}
	}

	for len(stack) > 0 {
		lst := len(stack) - 1
		output += string(stack[lst])
		stack = stack[:lst]
	}

	return output
}

func isNum(c byte) bool {
	if _, err := strconv.Atoi(string(c)); err != nil {
		return false
	}

	return true
}

// assume all number is between 0-9
func calPostfix(input string) int {
	// this stack is for numbers
	stack := []int{}

	for idx := range input {
		fmt.Println(string(input[idx]))
		fmt.Println(stack)
		if isNum(input[idx]) {
			n, _ := strconv.Atoi(string(input[idx]))
			stack = append(stack, n)
		} else {
			// pop two numbers
			last := len(stack) - 1
			op1 := stack[last-1] // op1 is the number been pushed to the stack earlier
			op2 := stack[last]
			stack = stack[:last-1]

			switch input[idx] {
			case '+':
				op1 += op2
			case '-':
				op1 -= op2
			case '*':
				op1 *= op2
			case '/':
				op1 /= op2
			}

			// push back result to stack
			stack = append(stack, op1)
		}
	}

	return stack[0]
}

func main() {
	infix := "5+3-9"
	postfix := infix2postfix(infix)

	fmt.Println(postfix)
	fmt.Println(calPostfix(postfix))
}
