# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, parent: TreeNode, grandparent: TreeNode) -> int:
            if not node:
                return 0

            # If grandparent is even-valued, include this node's value
            sum_val = 0
            if grandparent and grandparent.val % 2 == 0:
                sum_val += node.val

            # Traverse left and right subtrees
            sum_val += dfs(node.left, node, parent)
            sum_val += dfs(node.right, node, parent)

            return sum_val

        # Start the DFS with the root node, no parent, and no grandparent
        return dfs(root, None, None)


# Testing
root = TreeNode(6,
                TreeNode(7,
                         TreeNode(2, TreeNode(9)),
                         TreeNode(7, TreeNode(1), TreeNode(4))),
                TreeNode(8,
                         TreeNode(1),
                         TreeNode(3)))

solution = Solution()
print("Python Test Result:", solution.sumEvenGrandparent(root))  # Output: 18
