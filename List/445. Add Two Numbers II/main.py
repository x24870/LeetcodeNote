# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first try
# reverse the input
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r_l1 = self.reverse(l1)
        r_l2 = self.reverse(l2)
        dummy = tail = ListNode(0)
        carry = 0

        while r_l1 or r_l2 or carry:
            s = carry
            s += r_l1.val if r_l1 else 0
            s += r_l2.val if r_l2 else 0

            carry = s // 10
            tail.next = ListNode(s % 10)
            tail = tail.next
        
            r_l1 = r_l1.next if r_l1 else None
            r_l2 = r_l2.next if r_l2 else None
        return self.reverse(dummy.next)

    def reverse(self, lst):
        current = prev = None
        while lst:
            if not prev:
                prev = ListNode(lst.val)
            else:
                current = ListNode(lst.val)
                current.next = prev
                prev = current
            lst = lst.next
        return prev

# use stack
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        prev = None
        carry = 0
        while stack1 or stack2 or carry:
            a = stack1[-1] if stack1 else None
            b = stack2[-1] if stack2 else None
            print(a, b, carry)
            s = carry
            s += stack1.pop() if stack1 else 0
            s += stack2.pop() if stack2 else 0
            

            if not prev:
                prev = ListNode(s % 10)
            else:
                current = ListNode(s % 10)
                current.next = prev
                prev = current

            carry = s // 10

        return prev