class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None

        # If the current node's value is less than low, trim the left subtree and continue with the right subtree
        if root.val < low:
            return self.trimBST(root.right, low, high)

        # If the current node's value is greater than high, trim the right subtree and continue with the left subtree
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # Otherwise, the current node's value is within the range [low, high]
        # Recursively trim the left and right subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root
