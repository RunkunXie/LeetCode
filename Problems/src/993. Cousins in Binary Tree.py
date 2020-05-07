# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """my dfs sol, add Branch Pruning under hint"""
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        self.x_d = self.y_d = None
        self.x_p = self.y_p = None
        self.max_dep = float('inf')

        def dfs(node, x, y, depth, parent_val):

            if not node or depth > self.max_dep:
                return

            if node.val == x:
                self.x_d = depth
                self.x_p = parent_val
                self.max_dep = min(self.max_dep, depth)
            elif node.val == y:
                self.y_d = depth
                self.y_p = parent_val
                self.max_dep = min(self.max_dep, depth)

            if node.left:
                dfs(node.left, x, y, depth + 1, node.val)
            if node.right:
                dfs(node.right, x, y, depth + 1, node.val)

        dfs(root, x, y, 0, None)

        return self.x_d == self.y_d if self.x_d and self.y_d and (self.x_p != self.y_p) else False


