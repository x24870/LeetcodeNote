# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# First try, use built-in function
# Very slow and cost momory
# Time complexity: O(n^2)
# Space complexity: O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        history = []
        while head:
            if head in history: return True
            history.append(head)
            head = head.next
        return False

# Use hash table
# Time complexity: O(n)
# Space complexity: O(n)
from collections import defaultdict
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        history = defaultdict(bool)
        while head:
            if head in history: return True
            history[head] = True
            head = head.next
        return False

# Better solution
# Use two pointers, one fast(two step) and another one slow(one step)
# If there is cycle exist, the fast pointer will catch up the slow pointer
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while True:
            fast = fast.next if fast else None
            fast = fast.next if fast else None
            slow = slow.next if slow else None
            if fast == slow:
                return True if fast else False