# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#peek
# merge sort (up down)
# This solution does not meet the request of constant space complexity, but still pass the test
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None #break to two lists
        return self.merge(self.sortList(head), self.sortList(mid))

    def merge(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        cur.next = l1 if l1 else l2
        return dummy.next


# merge sort (bottom up)
class Solution2:
    def print_lst(self, head):
        while head:
            print(head.val, end=' ')
            head = head.next
        print()

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        # get list length
        length = 1
        h = head
        while h:
            length += 1
            h = h.next

        n = 1
        dummy = ListNode(0)
        dummy.next = head
        while n < length:
            cur = dummy.next
            tail = dummy
            while cur: # merge sort these sub lists
                l = cur
                r = self.split(l, n-1)
                cur = self.split(r, n-1)
                # print('------------------')
                # self.print_lst(l)
                # self.print_lst(r)
                # self.print_lst(cur)
                tail.next, tail = self.merge(l, r)
            n *= 2
            # self.print_lst(dummy.next)

        return dummy.next

    def split(self, head, n):
        # Splits the list into two parts, first n element and the rest.
        # Returns the head of the rest.
        while head and n:
            head = head.next
            n -= 1
        rest = head.next if head else None
        if head: head.next = None # break to two lists
        return rest

    def merge(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        cur.next = l1 if l1 else l2
        while cur.next: cur = cur.next # return the tail of list
        return dummy.next, cur


n1 = ListNode(4)
n2 = ListNode(2)
n3 = ListNode(1)
n4 = ListNode(3)
n1.next = n2
n2.next = n3
n3.next = n4
s = Solution2()
ans = s.sortList(n1)
while ans:
    print(ans.val)
    ans = ans.next