package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
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

		// found meet point
		if fast == slow {
			if fast == nil {
				return nil
			} else {
				break
			}
		}
	}

	slow = head
	for slow != fast {
		slow = slow.Next
		fast = fast.Next
	}

	return slow
}
