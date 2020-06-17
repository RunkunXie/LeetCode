# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """my sol under hint, 2nd attempt, time 2n space 1"""
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        node1, node2 = headA, headB
        tail1, tail2 = None, None
        if not node1 or not node2:
            return None

        while node1 != node2:

            if node1.next:
                node1 = node1.next
            else:
                tail1 = node1
                node1 = headB

            if node2.next:
                node2 = node2.next
            else:
                tail2 = node2
                node2 = headA

            if tail1 and tail2 and tail1 != tail2:
                return None

        return node1

    """my sol, 2nd attempt, time n space n"""
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        setA = set()
        while headA:
            setA.add(headA)
            headA = headA.next

        while headB:
            if headB in setA:
                return headB
            headB = headB.next

        return None

