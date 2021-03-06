# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    """my sol, 2nd attempt"""
    def reverseList(self, head: ListNode) -> ListNode:

        prev, curr, next = None, None, head

        while next:
            prev, curr, next = curr, next, next.next
            curr.next = prev

        return curr

    """online iterative, nice solution!"""
    def reverseList(self, head: ListNode) -> ListNode:

        cur, prev = head, None

        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    """my iter sol"""
    def reverseList(self, head: ListNode) -> ListNode:
        new_node = None

        while head:
            prev_node = new_node

            new_node = ListNode()
            new_node.val = head.val
            new_node.next = prev_node

            head = head.next

        return new_node