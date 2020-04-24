# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """my sol"""
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        curr = ListNode(-1)
        root = curr
        while l1 and l2:

            curr.next = ListNode()
            if l1.val < l2.val:
                curr.next.val = l1.val
                l1 = l1.next
            else:
                curr.next.val = l2.val
                l2 = l2.next

            curr = curr.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return root.next

    """my modified sol"""
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        curr = ListNode(-1)
        root = curr
        while l1 and l2:

            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return root.next