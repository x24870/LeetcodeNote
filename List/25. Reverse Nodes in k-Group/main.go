package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// n = len(listNode)
// time complexity: O(n*k)
// space complexity: O(1)
func reverseKGroup(head *ListNode, k int) *ListNode {
	dummyHead := &ListNode{Next: head}
	ret := dummyHead
	cur := dummyHead.Next
	for {
		nxtHead, found := searchNxtHead(cur, k)
		if !found {
			break
		}

		curEnd := reverse(dummyHead, nxtHead, k)
		dummyHead = curEnd
		cur = dummyHead.Next
	}

	return ret.Next

}

func reverse(prevGroupEnd *ListNode, nxtGroupHead *ListNode, k int) *ListNode {
	cur := prevGroupEnd.Next
	nxt := cur.Next
	prev := nxtGroupHead
	count := 0
	for count < k {
		cur.Next = prev
		prev = cur
		cur = nxt
		if nxt != nil {
			nxt = nxt.Next
		}
		count++
	}

	curGroupEnd := prevGroupEnd.Next
	prevGroupEnd.Next = prev
	return curGroupEnd
}

func searchNxtHead(head *ListNode, k int) (nxtHead *ListNode, found bool) {
	count := 0
	cur := head
	for count < k && cur != nil {
		cur = cur.Next
		count++
	}

	if count < k {
		return nil, false
	}

	return cur, true
}
