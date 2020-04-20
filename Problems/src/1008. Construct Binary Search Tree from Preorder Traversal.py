# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """"""

    """my sol, time n"""

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def build_tree(l):
            if len(l) == 1:
                return TreeNode(l[0])
            cur = TreeNode(l[0])

            left = False
            for i in range(1, len(l)):
                if l[i] < cur.val:
                    left = True
                    break

            right = False
            for j in range(1, len(l)):
                if l[j] > cur.val:
                    right = True
                    break

            print(cur, left, right)
            if left and right:
                cur.left = build_tree(l[i:j])
                cur.right = build_tree(l[j:])
            elif left:
                cur.left = build_tree(l[i:])
            elif right:
                cur.right = build_tree(l[j:])

            return cur

        return build_tree(preorder)
