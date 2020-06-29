# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first try
# idea: insertion sort, but it's a array version
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return
        prev = head
        cur = pos = head.next
        while cur:
            if cur.val < prev.val:
                pos = head
                while pos != cur:
                    if cur.val < pos.val:
                        pos.val, cur.val = cur.val, pos.val
                    pos = pos.next
            prev = cur
            cur = cur.next
        return head
                    
# time complexity: O(n^2)
# space complexity: O(n)
# insertion sort
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                insert = head.next
                cur = dummy
                while cur.next.val < insert.val:
                    cur = cur.next
                head.next = insert.next
                cur.next, insert.next = insert, cur.next

        return dummy.next