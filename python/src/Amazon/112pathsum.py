# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Base case: if the root is None, there can't be a path
        if not root:
            return False

        # Check if we have reached a leaf node and the target sum matches the node value
        if not root.left and not root.right and root.val == targetSum:
            return True

        # Recursively check left and right subtrees with updated target sum
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
