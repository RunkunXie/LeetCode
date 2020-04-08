# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """"""

    """my sol, time n, space 1"""
    # def middleNode(self, head: ListNode) -> ListNode:
    #
    #     count = 0
    #     next_node = head
    #     while next_node is not None:
    #         count += 1
    #         # print(count, next_node.val, head.val)
    #         next_node = next_node.next
    #
    #     i = 1
    #     ans = head
    #     while i < int(count / 2) + 1:
    #         ans = ans.next
    #         i += 1
    #         # print(i, ans.val)
    #
    #     return ans

    """online sol, time n, space 1"""
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
