# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# First try
# Use stack to store nodes
# Time complexity: O(max(l1, l2))
# Space complexity: O(max(l1, l2))
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        queue = []
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    queue.append(l1)
                    l1 = l1.next
                else:
                    queue.append(l2)
                    l2 = l2.next
            elif l1:
                queue.append(l1)
                l1 = l1.next
            else:
                queue.append(l2)
                l2 = l2.next

        while queue:
            cur.next = queue.pop(0)
            cur = cur.next
        cur.next = None
        return dummy.next

# Recursive solution
# Time complexity: O(max(l1, l2))
# Space complexity: O(max(l1, l2))
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: return l1 if l1 else l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# Iterative solution
# Time complexity: O(max(l1, l2))
# Space complexity: O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1: cur.next = l1
        if l2: cur.next = l2
        return dummy.next