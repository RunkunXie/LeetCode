# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    """my sol, 2nd attempt"""
    def hasCycle(self, head: ListNode) -> bool:

        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return False

        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
