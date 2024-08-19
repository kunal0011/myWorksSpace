# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob_helper(node):
            # Base case: if the node is None, return (0, 0)
            if not node:
                return (0, 0)

            # Recursively solve for left and right children
            left = rob_helper(node.left)
            right = rob_helper(node.right)

            # Option 1: Rob the current node, so you cannot rob its children
            rob_current = node.val + left[1] + right[1]

            # Option 2: Do not rob the current node, take the max of robbing or not robbing children
            not_rob_current = max(left) + max(right)

            # Return two values: (max money if robbing this node, max money if not robbing this node)
            return (rob_current, not_rob_current)

        # Call the helper function on the root node
        return max(rob_helper(root))
