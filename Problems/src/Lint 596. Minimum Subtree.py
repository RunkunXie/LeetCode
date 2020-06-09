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
    @return: the root of the minimum subtree
    """

    """my dfs sol under hint, 2nd attempt"""
    def findSubtree(self, root):
        # write your code here
        def dfs(root):
            """
            @return: cur_sum, min_sum, min_root
            """
            if not root:
                return 0, float("inf"), None

            left_sum, left_min_sum, left_min_root = dfs(root.left)
            right_sum, right_min_sum, right_min_root = dfs(root.right)

            cur_sum = root.val + left_sum + right_sum

            if cur_sum < min(left_min_sum, right_min_sum):
                return cur_sum, cur_sum, root
            elif left_min_sum < right_min_sum:
                return cur_sum, left_min_sum, left_min_root
            return cur_sum, right_min_sum, right_min_root

        return dfs(root)[2]

    """my dfs sol, 1st attempt"""
    def findSubtree(self, root):
        # write your code here

        if not root:
            return root

        def dfs(root):

            cur_sum, min_sum, min_root = root.val, root.val, root

            if root.left and root.right:
                left_sum, left_min_sum, left_min_root = dfs(root.left)
                right_sum, right_min_sum, right_min_root = dfs(root.right)
                cur_sum += (left_sum + right_sum)
                if cur_sum < min(left_sum, right_sum):
                    min_sum, min_root = cur_sum, root
                elif left_min_sum < right_min_sum:
                    min_sum, min_root = left_min_sum, left_min_root
                else:
                    min_sum, min_root = right_min_sum, right_min_root

            elif root.left:
                left_sum, left_min_sum, left_min_root = dfs(root.left)
                cur_sum += left_sum
                if cur_sum < left_min_sum:
                    min_sum, min_root = cur_sum, root
                else:
                    min_sum, min_root = left_min_sum, left_min_root

            elif root.right:
                right_sum, right_min_sum, right_min_root = dfs(root.right)
                cur_sum += right_sum
                if cur_sum < right_min_sum:
                    min_sum, min_root = cur_sum, root
                else:
                    min_sum, min_root = right_min_sum, right_min_root

            return cur_sum, min_sum, min_root

        cur_sum, min_sum, min_root = dfs(root)
        return min_root
