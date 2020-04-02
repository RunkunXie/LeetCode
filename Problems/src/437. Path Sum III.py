# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        if root is None:
            return 0

        cur = 0
        count = 0

        count_cur = self.pathSumSource(root, sum, cur, count)
        count_left = self.pathSum(root.left, sum)
        count_right = self.pathSum(root.right, sum)

        return count_cur + count_left + count_right

    def pathSumSource(self, root, sum, cur, count) -> int:

        if root is None:
            return 0

        cur += root.val

        if cur == sum:
            count += 1

        left_count = self.pathSumSource(root.left, sum, cur, 0)
        right_count = self.pathSumSource(root.right, sum, cur, 0)

        return count + left_count + right_count
