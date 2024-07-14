# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Start from the root node of the tree
        current = root

        while current:
            # If both p and q are greater than current node, then LCA lies in right
            if p.val > current.val and q.val > current.val:
                current = current.right
            # If both p and q are smaller than current node, then LCA lies in left
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                # We have found the split point, i.e. the LCA node.
                return current
