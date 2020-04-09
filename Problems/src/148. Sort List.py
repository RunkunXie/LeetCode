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
    def sortList(self, head):
        if not head or not head.next:
            return head
        length = self.getLen(head)
        dummy = ListNode(-1)
        dummy.next = head
        step = 1
        while step <= length:
            preTail = dummy
            # shouldn't be head here, because head might be modified to other places by below steps.
            curHead = dummy.next
            while curHead:
                leftHead = curHead
                rightHead = self.splitAndReturnNextHead(leftHead, step)
                nextHead = self.splitAndReturnNextHead(rightHead, step)
                curTail = self.mergeAndReturnTail(leftHead, rightHead, preTail)
                preTail, curHead = curTail, nextHead
            step *= 2
        return dummy.next

    def mergeAndReturnTail(self, l1, l2, prevTail):
        cur = prevTail
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        while l1:
            cur.next = l1
            l1, cur = l1.next, cur.next
        while l2:
            cur.next = l2
            l2, cur = l2.next, cur.next
        return cur  # the tail of this merged segment

    def splitAndReturnNextHead(self, head, length):
        if not head:
            return head
        count = 1
        while (count < length and head.next):
            head = head.next
            count += 1
        nextHead = head.next
        head.next = None  # cut this segment for valid merging step.
        return nextHead  # the head of next segment

    def getLen(self, head):
        if not head:
            return 0
        count = 1
        while head.next:
            count += 1
            head = head.next
        return count

    """online sol, time nlogn, space n"""
    # def sortList(self, head: ListNode) -> ListNode:
    #     if not head or not head.next: return head
    #     pre = slow = fast = head
    #     while fast and fast.next:
    #         pre = slow
    #         slow = slow.next
    #         fast = fast.next.next
    #     pre.next = None
    #     firstHalf = self.sortList(head)
    #     secondHalf = self.sortList(slow)
    #     return self.sort(firstHalf, secondHalf)
    #
    # def sort(self, left, right):
    #     dummy = ListNode(0)
    #     cur = dummy
    #     while left and right:
    #         if left.val <= right.val:
    #             cur.next = left
    #             left = left.next
    #         elif left.val > right.val:
    #             cur.next = right
    #             right = right.next
    #         cur = cur.next
    #     cur.next = left or right
    #     return dummy.next
