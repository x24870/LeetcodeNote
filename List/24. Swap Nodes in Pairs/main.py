# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first try, ugly
# Idea:
# consider these three cases:
# a. 1 -> 2 -> 3 -> 4
# b. 1 -> 2 -> 3
# 
# edge case:
# null
# 1 -> null

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = head
        return_head = head.next if head else None
        current = return_head

        while prev and current:
            next_pair_prev = current.next
            next_pair_cur = next_pair_prev.next if next_pair_prev else None

            if current.next:
                if current.next.next: # two nodes left
                    prev.next = current.next.next
                else: # only one node left
                    prev.next = current.next
            else:
                prev.next = None
            current.next = prev

            prev = next_pair_prev
            current = next_pair_cur

        return return_head if return_head else head



# This solution is more clear
# Only have to consider edge case and normal case
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # for edge case
        if not head or not head.next: return head
        
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next and head.next.next:
            n1, n2 = head.next, head.next.next
            n1.next = n2.next
            n2.next = n1
            head.next = n2
            head = n1
        return dummy.next