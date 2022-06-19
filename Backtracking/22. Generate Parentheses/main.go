package main

// time complexity: O(2^n)
// space complexity: O(n)
func generateParenthesis(n int) []string {
	rets := []string{}
	dfs(&rets, "(", n*2)
	return rets
}

func dfs(rets *[]string, cur string, length int) {
	if len(cur) == length {
		if valid(cur) {
			(*rets) = append((*rets), cur)
		}
		return
	}

	dfs(rets, cur+"(", length)
	dfs(rets, cur+")", length)
}

func valid(s string) bool {
	if s[len(s)-1] == '(' {
		return false
	}

	diff := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
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
