package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// recursive
func reverseList(head *ListNode) *ListNode {
	return reverse(nil, head)
}

func reverse(pre, cur *ListNode) *ListNode {
	if cur == nil || cur.Next == nil {
		return cur
	}

	reversedHead := reverse(cur, cur.Next)
	cur.Next.Next = cur
	cur.Next = pre
	return reversedHead
}

// iterations
func reverseListIter(head *ListNode) *ListNode {
	var pre *ListNode
	cur, nxt := head, head
	for cur != nil {
		nxt = cur.Next
		cur.Next = pre
		pre = cur
		cur = nxt
	}

	return pre
}
