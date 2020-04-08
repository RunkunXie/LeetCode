# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """"""

    """my sol, time nlogn, space n"""
    # def sortList(self, head: ListNode) -> ListNode:
    #
    #     if not head:
    #         return None
    #
    #     val = []
    #     next = head
    #     while next:
    #         val.append(next.val)
    #         next = next.next
    #
    #     val = sorted(val)
    #     root = ans = ListNode(val[0])
    #     for v in val[1:]:
    #         ans.next = ListNode(v)
    #         ans = ans.next
    #
    #     return root

    """online sol, need to be space 1, use merge sort"""
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        pre = slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        firstHalf = self.sortList(head)
        secondHalf = self.sortList(slow)
        return self.sort(firstHalf, secondHalf)

    def sort(self, left, right):
        dummy = ListNode(0)
        cur = dummy
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            elif left.val > right.val:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left or right
        return dummy.next
