# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# peek, it's shame
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = current = ListNode(0)
        while l1 or l2 or carry:
            num = carry
            num += l1.val if l1 else 0
            num += l2.val if l2 else 0
            carry = num // 10
            current.next = ListNode(num % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next