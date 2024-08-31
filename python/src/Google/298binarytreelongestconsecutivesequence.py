class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, parent_val, length):
            if not node:
                return length

            # Check if the current node is consecutive
            if node.val == parent_val + 1:
                length += 1
            else:
                length = 1

            # Recursively find the longest sequence in the left and right subtrees
            left_length = dfs(node.left, node.val, length)
            right_length = dfs(node.right, node.val, length)

            # Return the maximum length found
            return max(length, left_length, right_length)

        return dfs(root, root.val - 1, 0)
