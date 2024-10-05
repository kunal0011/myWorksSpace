# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # Helper function to perform flattening
        def flatten_tree(node):
            if not node:
                return None

            # Flatten left and right subtrees
            left_tail = flatten_tree(node.left)
            right_tail = flatten_tree(node.right)

            # If there is a left subtree, we need to move it to the right
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            # We need to return the "tail" of the flattened tree
            return right_tail if right_tail else left_tail if left_tail else node

        flatten_tree(root)
