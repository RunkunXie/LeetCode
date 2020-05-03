# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        def dfs(leftTree, rightTree):

            if not leftTree and not rightTree:
                return True
            elif not leftTree or not rightTree:
                return False

            return (leftTree.val == rightTree.val) and dfs(
                leftTree.left, rightTree.right) and dfs(
                leftTree.right, rightTree.left)

        return dfs(root.left, root.right)
