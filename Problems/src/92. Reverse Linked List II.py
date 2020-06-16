# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """my sol, 1st attempt"""
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        i = 1

        # after iteration: prev -> (m-1)-th node, curr -> m-th node
        prev, curr = None, head
        while curr and i < m:
            prev, curr = curr, curr.next
            i += 1

        # after iteration: re_prev -> n-th node, re_curr -> (n+1)-th node
        re_prev, re_curr = prev, curr
        while re_curr and i <= n:
            re_curr.next, re_prev, re_curr = re_prev, re_curr, re_curr.next
            i += 1

        # assign prev.next = re_prev, the start of reverse linked list
        if prev:
            prev.next = re_prev

        # assign curr.next = re_curr, the (n+1)-th node
        curr.next = re_curr

        # return, if prev is None, i.e., m = 1, return re_prev
        return head if prev else re_prev


