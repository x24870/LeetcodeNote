# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# First try
# Use hash table
# Time complexity: O(n)
# Space complexity: O(n)
from collections import defaultdict
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        history = defaultdict(bool)
        while head:
            if history.get(head): return head
            history[head] = True
            head = head.next
        return None

# Without using extra space
# Reference: https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while True:
            fast = fast.next if fast else None
            fast = fast.next if fast else None
            slow = slow.next if slow else None
            if fast == slow:
                break

        if fast == None: return None

        # cycle exist
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast