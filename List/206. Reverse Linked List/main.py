# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# first try
# recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # for edge case: [1] or []
        if not head or not head.next: return head
        self.prev = None
        self.next = head.next
        
        def reverse(node):
            if not node: return
            self.next = node.next
            node.next = self.prev
            self.prev = node
            reverse(self.next)
        
        reverse(head)
        return self.prev

# first try
# iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        prev =  None
        next = head.next

        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev


# this solution is more clear and handle all cases
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur, nxt = None, head, None
        while cur:
            nxt, cur.next = cur.next, prev
            prev, cur = cur, nxt
        return prev