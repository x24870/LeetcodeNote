package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	if left == right {
		return head
	}

	// find left node
	var preLeft *ListNode
	leftNode := head
	for left > 1 {
		preLeft = leftNode
		leftNode = leftNode.Next
		left--
		right--
	}

	// reverse
	rightNode := reverse(leftNode, preLeft, leftNode, right)
	if preLeft != nil {
		preLeft.Next = rightNode
		return head
	}

	return rightNode
}

func reverse(leftNode, pre, cur *ListNode, rightDist int) *ListNode {
	// found the right node
	if rightDist <= 1 {
		leftNode.Next = cur.Next
		cur.Next = pre
		return cur
	}

	rightNode := reverse(leftNode, cur, cur.Next, rightDist-1)
	if cur != leftNode {
		cur.Next.Next = cur
		cur.Next = pre
	}
	return rightNode
}

func main() {
	head := &ListNode{Val: 1}
	head.Next = &ListNode{Val: 2}
	head.Next.Next = &ListNode{Val: 3}
	head.Next.Next.Next = &ListNode{Val: 4}
	head.Next.Next.Next.Next = &ListNode{Val: 5}

	head = reverseBetween(head, 2, 4)
	for head != nil {
		fmt.Println(head.Val)
		head = head.Next
	}

	head = &ListNode{Val: 3}
	head.Next = &ListNode{Val: 5}

	head = reverseBetween(head, 1, 2)
	for head != nil {
		fmt.Println(head.Val)
		head = head.Next
	}

}
