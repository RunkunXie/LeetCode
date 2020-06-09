"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    """my dfs sol"""
    def flatten(self, root):
        # write your code here

        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left:
            left = root.left
            while left.right:
                left = left.right

            if root.right:
                left.right = root.right
            root.left, root.right = None, root.left


