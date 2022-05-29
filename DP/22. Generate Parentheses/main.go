package main

// compare to origin solution, use pointer to preventing reallocate memory for the sent-in parameters
func generateParenthesis(n int) []string {
	comb := []string{}
	gen(n*2, &comb, "")
	return comb
}

func gen(n int, comb *[]string, cur string) {
	if n == 0 {
		if isValid(&cur) {
			*comb = append(*comb, cur)
		}
		return
	}

	gen(n-1, comb, cur+"(")
	gen(n-1, comb, cur+")")
}

func isValid(cur *string) bool {
	diff := 0
	for _, c := range *cur {
		if c == '(' {
			diff++
		} else {
			diff--
		}

		if diff < 0 {
			return false
		}
	}

	if diff != 0 {
		return false
	}

	return true
}

// // origin
// func generateParenthesis(n int) []string {
// 	return gen(n*2, "")
// }

// func gen(n int, cur string) []string {
// 	if n == 0 {
// 		if isValid(cur) {
// 			return []string{cur}
// 		} else {
// 			return []string{}
// 		}
// 	}

// 	ret := []string{}
// 	ret = append(ret, gen(n-1, cur+"(")...)
// 	ret = append(ret, gen(n-1, cur+")")...)
// 	return ret
// }

// func isValid(cur string) bool {
// 	diff := 0
// 	for _, c := range cur {
// 		if c == '(' {
// 			diff++
// 		} else {
// 			diff--
// 		}

//         if diff < 0 {
//             return false
//         }
// 	}

// 	if diff != 0 {
// 		return false
// 	}

// 	return true
// }
