"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """

    def findSubtree2(self, root):
        # write your code here

        def dfs(node):
            """
            @param: node
            @return: cur_avg, cur_node_num, max_avg, max_node
            """
            if not node:
                return 0, 0, -float("inf"), None

            left_avg, left_node_num, left_max_avg, left_max_node = dfs(node.left)
            right_avg, right_node_num, right_max_avg, right_max_node = dfs(node.right)

            cur_node_num = left_node_num + right_node_num + 1
            cur_avg = (left_node_num * left_avg + right_node_num * right_avg + node.val) / cur_node_num

            if cur_avg > max(left_max_avg, right_max_avg):
                return cur_avg, cur_node_num, cur_avg, node
            elif left_max_avg > right_max_avg:
                return cur_avg, cur_node_num, left_max_avg, left_max_node
            else:
                return cur_avg, cur_node_num, right_max_avg, right_max_node

        return dfs(root)[3]