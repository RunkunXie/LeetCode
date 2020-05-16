"""Biweekly Contest 26 - Q3"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """my dfs sol - 1 attempt"""
    # def goodNodes(self, root: TreeNode) -> int:
    #
    #     self.ans = 0
    #
    #     def dfs(node, max_top):
    #
    #         if not node:
    #             return
    #
    #         if node.val >= max_top:
    #             self.ans += 1
    #             max_top = node.val
    #
    #         dfs(node.left, max_top)
    #         dfs(node.right, max_top)
    #
    #     dfs(root, -float("inf"))
    #
    #     return self.ans

    """my modified sol - dfs"""
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_top):
            if not node:
                return 0

            return (node.val >= max_top) + dfs(
                node.left, max(max_top, node.val)) + dfs(
                node.right, max(max_top, node.val))

        return dfs(root, -float("inf"))
