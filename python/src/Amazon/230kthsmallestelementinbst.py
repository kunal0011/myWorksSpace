# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.result = None
        self.inorder(root)
        return self.result

    def inorder(self, node):
        if not node or self.result is not None:
            return

        # Visit left subtree
        self.inorder(node.left)

        # Visit current node
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return

        # Visit right subtree
        self.inorder(node.right)
