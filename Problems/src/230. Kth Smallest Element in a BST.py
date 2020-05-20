# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """my sol, recursive"""
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l = []

        def dfs(node):
            if node:
                dfs(node.left)
                l.append(node.val)
                dfs(node.right)

        dfs(root)

        return l[k - 1]

    """ans, iterative"""
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
