# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#peek
# Idea:
# Use merge sort, because all lists are sorted
# So we can just merge these lists
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(l1, l2):
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

        ans = None
        for lst in lists:
            ans = merge(ans, lst)
        return ans

# priority queue
# But PriorityQueue seems not work well on Leetcode Python3 compiler
# You will get TypeError if you run this solution on their Python3 compiler
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = PriorityQueue()
        dummy = cur = ListNode(0)
        for lst in lists:
            if lst:
                pq.put((lst.val, lst))

        while not pq.empty():
            val, node = pq.get()
            cur.next = node
            cur = cur.next
            node = node.next
            if node: pq.put(node.val, node)

        return dummy.next