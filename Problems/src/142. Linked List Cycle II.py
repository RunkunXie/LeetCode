# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """my 2-pointers sol, 2nd attempt"""
    def detectCycle(self, head: ListNode) -> ListNode:

        #         1 2 3 4 5 6 7 8 9
        #         1 2 3 4 2 3 4 2 3

        #         1 3 5 7 9 11131517
        #         1 3 2 4 3 2 4 3 2

        # find circle
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                p1, p2 = head, slow
                break
        else:
            return None

        # find cycle start
        while p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1
