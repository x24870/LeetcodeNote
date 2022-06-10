package main

type Node struct {
	word string
	nxt  *Node
}

func ladderLength(beginWord string, endWord string, wordList []string) int {
	// if end word not in the word list, there is no way to match the end word
	if indexOf(wordList, endWord) == -1 {
		return 0
	}

	// push begin word to the word list
	if indexOf(wordList, beginWord) == -1 {
		wordList = append(wordList, beginWord)
	}

	// build graph
	m := buildGraph(wordList)

	return bfs(m, beginWord, endWord)
}

// breadth first search
func bfs(m map[string][]string, beginWord, endWord string) int {
	count := 1
	traversed := make(map[string]struct{})
	q := []string{}

	// push starter node to the queue
	q = append(q, beginWord)

	for len(q) > 0 {
		size := len(q)
		for i := 0; i < size; i++ {
			// pop
			w := q[0]
			q = q[1:]

			// check if current word is the endWord
			if w == endWord {
				return count
			}

			// cehck if this node has been traversed
			if _, ok := traversed[w]; ok {
				continue
			} else {
				traversed[w] = struct{}{}
			}

			// traverse neighbors
			for _, neighbor := range m[w] {
				if _, ok := traversed[neighbor]; ok {
					continue
				}
				q = append(q, neighbor)
			}
		}
		count++
	}

	return 0
}

func buildGraph(wordList []string) map[string][]string {
	// build a graph base on the word list
	// if two words only differ one charactor, these two are adjancet
	// for example
	// m['abc'] = ['abd']
	// m['abd'] = ['abc', 'bbd']
	// m['bbd'] = ['abd']
	m := make(map[string][]string)
	for i := 0; i < len(wordList)-1; i++ {
		w1 := wordList[i]
		for j := i; j < len(wordList); j++ {
			w2 := wordList[j]
			if checkAdjancent(w1, w2) {
				m[w1] = append(m[w1], w2)
				m[w2] = append(m[w2], w1)
			}
		}
	}
	return m
}

func checkAdjancent(w1, w2 string) bool {
	r1 := []rune(w1)
	r2 := []rune(w2)
	diff := 0
	for i := 0; i < len(r1); i++ {
		if r1[i] != r2[i] {
			diff++
		}
		if diff > 1 {
			return false
		}
	}

	return true
}

func indexOf(words []string, target string) int {
	for i, w := range words {
		if target == w {
			return i
		}
	}
	return -1
}
