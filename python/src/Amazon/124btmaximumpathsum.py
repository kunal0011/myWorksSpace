class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0

            # Recursive call on the left and right children.
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # The price of the current node is its value plus the maximum gain from its left and right subtrees.
            price_newpath = node.val + left_gain + right_gain

            # Update the maximum sum if the new path is better.
            self.max_sum = max(self.max_sum, price_newpath)

            # Return the maximum gain if we continue the same path.
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum
