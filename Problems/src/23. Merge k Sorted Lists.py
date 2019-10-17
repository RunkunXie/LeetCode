from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def gen_lists_node(lists_list):
    lists_node = []
    for v in lists_list:
        root = tmp_node = ListNode(0)
        for n in v:
            tmp_node.next = ListNode(n)
            tmp_node = tmp_node.next
        lists_node.append(root.next)
    return lists_node


def gen_lists(lists_node: ListNode):
    lists_list = []
    while lists_node:
        lists_list.append(lists_node.val)
        lists_node = lists_node.next
    return lists_list


class Solution:
    # def mergeKLists(self, lists: [ListNode]) -> ListNode:
    #     """
    #     Ccompare one by one, O(kN)
    #     :param lists:
    #     :return:
    #     """
    #     head = point = ListNode(0)
    #
    #     while lists:
    #
    #         tmp_i = 0
    #         tmp_min = float("inf")
    #         for i, v in enumerate(lists):
    #             if v and v.val < tmp_min:
    #                 tmp_i = i
    #                 tmp_min = v.val
    #
    #         if lists[tmp_i] is None:
    #             break
    #
    #         if lists[tmp_i].next:
    #             lists[tmp_i] = lists[tmp_i].next
    #         else:
    #             lists.pop(tmp_i)
    #
    #         point.next = ListNode(tmp_min)
    #         point = point.next
    #
    #     return head.next

    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        """
        Brute Force, O(NlogN)
        :param lists:
        :return:
        """

        convert_to_list = []
        for v in lists:
            while v:
                convert_to_list.append(v.val)
                v = v.next

        convert_to_list.sort()

        root = merge_list = ListNode(0)
        for l in convert_to_list:
            merge_list.next = ListNode(l)
            merge_list = merge_list.next

        return root.next

    # def mergeKLists(self, lists: [ListNode]) -> ListNode:
    #     """
    #     Ccompare one by one, optimize using queue - O(N*logk)
    #     :param lists:
    #     :return:
    #     """
    #     head = point = ListNode(0)
    #     q = PriorityQueue()
    #
    #     for i, l in enumerate(lists):
    #         if l:
    #             q.put((l.val, i, l))
    #
    #     while not q.empty():
    #         val, i, node = q.get()
    #
    #         point.next = ListNode(val)
    #         point = point.next
    #
    #         node = node.next
    #         if node:
    #             q.put((node.val, i, node))
    #
    #     return head.next


lists = gen_lists_node([[1, 4, 5], [1, 3, 4], [2, 6]])
merge_nodes = Solution().mergeKLists(lists)
print("result:", gen_lists(merge_nodes))
print("answer:", [1, 1, 2, 3, 4, 4, 5, 6])

lists = gen_lists_node([[], [2, 6]])
merge_nodes = Solution().mergeKLists(lists)
print("result:", gen_lists(merge_nodes))
print("answer:", [2, 6])

lists = gen_lists_node([[], []])
merge_nodes = Solution().mergeKLists(lists)
print("result:", gen_lists(merge_nodes))
print("answer:", [])

lists = gen_lists_node(
    [[0, 1, 2], [-10, -8, -5, -4], [], [], [-3], [-10, -9, -6, -4, -3, -2, -2, -1, 2], [-9, -9, -2, -1, 0, 1],
     [-9, -4, -3, -2, 2, 2, 3, 3, 4]])
merge_nodes = Solution().mergeKLists(lists)
print("result:", gen_lists(merge_nodes))
print("answer:",
      [-10, -10, -9, -9, -9, -9, -8, -6, -5, -4, -4, -4, -3, -3, -3, -2, -2, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 2, 2, 3,
       3, 4])
