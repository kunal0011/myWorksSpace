# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # This variable will store the cumulative sum
        self.total = 0

        def reverse_inorder(node: TreeNode):
            if not node:
                return
            # Traverse the right subtree first
            reverse_inorder(node.right)
            # Modify the current node's value
            self.total += node.val
            node.val = self.total
            # Traverse the left subtree
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root
