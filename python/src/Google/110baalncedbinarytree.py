# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # Helper function to determine the height of the tree
        def height(node):
            # Base case: empty node has height 0
            if not node:
                return 0

            # Recursively find the height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # If the subtree is unbalanced, return -1
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1

            # Return the height of the current subtree
            return max(left_height, right_height) + 1

        # Use the helper function to check if the tree is balanced
        return height(root) != -1
