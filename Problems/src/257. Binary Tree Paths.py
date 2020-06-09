# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """my dfs sol"""
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        # root is None
        if not root:
            return []

        # root is leaf
        if not root.right and not root.left:
            return [str(root.val)]

        # root is not leaf
        left_path = self.binaryTreePaths(root.left)
        right_path = self.binaryTreePaths(root.right)
        return ["".join([str(root.val), "->", path])
                for path in left_path + right_path]

