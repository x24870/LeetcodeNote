package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	slow, fast := head, head
	for {
		if slow != nil {
			slow = slow.Next
		}
		if fast != nil {
			fast = fast.Next
		}
		if fast != nil {
			fast = fast.Next
		}

		if fast == slow {
			if fast != nil {
				return true
			}
			return false
		}
	}
}
