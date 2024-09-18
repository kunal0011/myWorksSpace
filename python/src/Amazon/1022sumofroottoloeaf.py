# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        MOD = 10**9 + 7

        # Helper function for DFS traversal
        def dfs(node, current_value):
            if not node:
                return 0

            # Update the current value (shift left and add current node's value)
            current_value = (current_value << 1) | node.val

            # If it's a leaf node, return the current binary number
            if not node.left and not node.right:
                return current_value

            # Recur for left and right children
            left_sum = dfs(node.left, current_value)
            right_sum = dfs(node.right, current_value)

            return (left_sum + right_sum) % MOD

        # Call the DFS function starting from the root with the initial binary value of 0
        return dfs(root, 0)


# Testing
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

solution = Solution()
print("Python Test Result:", solution.sumRootToLeaf(root))  # Output: 22
