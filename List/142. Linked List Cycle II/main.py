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
# Floyd's algorithm