# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """my sol, time n space 1"""
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head:
            return None

        # o, e: end of odd and even list
        o = head
        e = head.next

        while e and e.next:
            # cur: next odd element
            cur = e.next

            # append next even element
            e.next = cur.next
            e = e.next

            # append next odd element
            o.next = ListNode(cur.val, o.next)
            o = o.next

        return head


