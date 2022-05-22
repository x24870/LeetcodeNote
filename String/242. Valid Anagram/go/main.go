package main

func isAnagram(s string, t string) bool {
	ms := make(map[rune]int)
	mt := make(map[rune]int)

	for _, c := range s {
		ms[c] += 1
	}

	for _, c := range t {
		mt[c] += 1
	}

	if len(ms) != len(mt) {
		return false
	}

	for k, _ := range ms {
		if ms[k] != mt[k] {
			return false
		}
	}

	return true
}
