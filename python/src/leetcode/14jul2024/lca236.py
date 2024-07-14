# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: if the tree is empty or we've found one of the nodes
        if root is None or root == p or root == q:
            return root

        # Search for LCA in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-None, p and q are found in different subtrees
        if left and right:
            return root

        # Otherwise, return the non-None value
        return left if left else right
