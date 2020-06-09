# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """my sol under hint"""
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """ 

        ans = []
        dq = deque([root])

        while dq:
            node = dq.popleft()
            if node:
                dq.append(node.left)
                dq.append(node.right)

            ans.append(node.val if node else None)

        return ' '.join([str(n) for n in ans])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = deque(data.split())

        init_val = data.popleft()
        root = TreeNode(int(init_val)) if init_val != 'None' else None
        dq = deque([root])

        while dq:
            node = dq.popleft()
            if node:
                l, r = data.popleft(), data.popleft()
                node.left = TreeNode(int(l)) if l != 'None' else None
                node.right = TreeNode(int(r)) if r != 'None' else None
                dq.append(node.left)
                dq.append(node.right)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))