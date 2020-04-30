# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:

        def dfs(node, i, n):

            ans = False
            if node and node.val == arr[i]:
                if i < n - 1:
                    ans = dfs(node.left, i + 1, n) or dfs(node.right, i + 1, n)
                elif i == n - 1:
                    if not node.left and not node.right:
                        ans = True

            return ans

        return dfs(root, 0, len(arr))
