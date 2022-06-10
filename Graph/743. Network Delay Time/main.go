package main

import (
	"container/heap"
	"fmt"
)

type Node struct {
	idx  int
	cost int
}

type Heap []Node

// implement Len, Less, Swap for sort.Interface
func (h Heap) Len() int {
	return len(h)
}

func (h Heap) Less(i, j int) bool {
	return h[i].cost < h[j].cost
}

func (h Heap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

// implement Push Pop for heap.interface
func (h *Heap) Push(item interface{}) {
	(*h) = append((*h), item.(Node))
}

func (h *Heap) Pop() interface{} {
	item := (*h)[h.Len()-1]
	(*h) = (*h)[0 : h.Len()-1]
	return item
}

func networkDelayTime(times [][]int, n int, k int) int {
	// build graph
	graph := buildGraph(times)

	// a map for memoring traversed nodes and costs
	m := make(map[int]Node)

	// a heap for containing Nodes
	h := Heap{}
	// Push stater Node to the heap
	heap.Push(&h, Node{k, 0})

	// bfs - best first search
	for h.Len() > 0 {
		// pop
		n := heap.Pop(&h).(Node)

		// check if the node has been traversed
		if _, ok := m[n.idx]; ok {
			continue
		}

		// memorize the node
		m[n.idx] = Node{n.idx, n.cost}

		// traverse adjancent
		for _, neighbor := range graph[n.idx] {
			// check if the neighbor has been traversed
			if _, ok := m[neighbor.idx]; ok == false {
				// push to the heap
				heap.Push(&h, Node{neighbor.idx, n.cost + neighbor.cost})
			}
		}
	}

	// check if all nodes are been traversed
	if len(m) != n {
		return -1
	}

	// find max cost
	max := 0
	for _, node := range m {
		if node.cost > max {
			max = node.cost
		}
	}

	return max
}

func buildGraph(times [][]int) map[int][]Node {
	m := make(map[int][]Node)
	for _, edge := range times {
		lst, ok := m[edge[0]]
		if ok != true {
			m[edge[0]] = make([]Node, 0)
			lst = m[edge[0]]
		}
		m[edge[0]] = append(lst, Node{edge[1], edge[2]})
	}
	return m
}

func main() {
	delay := networkDelayTime([][]int{{2, 1, 1}, {2, 3, 1}, {3, 4, 1}}, 4, 2)
	fmt.Println(delay)
}
