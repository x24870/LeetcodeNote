// This example demonstrates an integer heap built using the heap interface.
package main

import (
	"container/heap"
	"sort"
)

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h *IntHeap) Len() int {
	return len(*h)
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

// For implement Max heap, here we reverse the Less() logic
func (h IntHeap) Less(i, j int) bool {
	//min heap
	// return h[i] < h[j]
	//max heap
	return h[i] > h[j]
}

func (h *IntHeap) Push(i interface{}) {
	*h = append(*h, i.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func findKthLargestHeap(nums []int, k int) int {
	h := &IntHeap{}
	heap.Init(h)

	// push all numbers to the heap
	for _, n := range nums {
		heap.Push(h, n)
	}

	// pop k-1 largest numbers
	for i := 1; i < k; i++ {
		heap.Pop(h)
	}

	return heap.Pop(h).(int)
}

// cleaner solution
func findKthLargest(nums []int, k int) int {
	sort.Ints(nums)
	return nums[len(nums)-k]
}
