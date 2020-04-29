# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root) -> int:

        def DFS(node):
            """
            :param node:
            :return:
                node_max: max path sum
                node_max_from_node: max path sum containing current node
            """
            if not node.left and not node.right:
                return node.val, node.val

            elif node.left and not node.right:
                left_max, left_path = DFS(node.left)

                node_max_from_node = node.val + max(left_path, 0)
                node_max = max(node.val + max(left_path, 0),
                               left_max)

            elif node.right and not node.left:
                right_max, right_path = DFS(node.right)
                node_max_from_node = node.val + max(right_path, 0)
                node_max = max(node.val + max(right_path, 0),
                               right_max)

            else:
                left_max, left_path = DFS(node.left)
                right_max, right_path = DFS(node.right)

                node_max_from_node = max(node.val + max(left_path, 0),
                                         node.val + max(right_path, 0))
                node_max = max(node.val + max(left_path, 0) + max(right_path, 0),
                               left_max,
                               right_max)

            return node_max, node_max_from_node

        return DFS(root)[0]


tree_val = [1, 2, 3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().maxPathSum(root))

tree_val = [-10, 9, 20, None, None, 15, 7]
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().maxPathSum(root))

tree_val = [-3]
root = TreeNode(-3)
print(Solution().maxPathSum(root))

tree_val = [-1, -2, -3]
root = TreeNode(-1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
print(Solution().maxPathSum(root))

tree_val = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
print(Solution().maxPathSum(root))
