class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Base case: both nodes are None, trees are the same
        if not p and not q:
            return True

        # If one node is None and the other is not, trees are not the same
        if not p or not q:
            return False

        # Check if the current nodes are the same and recursively check their children
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
