# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0

        def post_order(node):
            if not node:
                return 0

            # Post-order traversal: process left and right children first
            left_balance = post_order(node.left)
            right_balance = post_order(node.right)

            # Calculate the balance of the current node
            balance = node.val - 1 + left_balance + right_balance

            # The number of moves is increased by the absolute value of the balance at this node
            self.moves += abs(balance)

            return balance

        post_order(root)
        return self.moves


# Testing
root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(0)
solution = Solution()
print("Python Test Result:", solution.distributeCoins(root))  # Output: 2
