# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # Helper function for DFS traversal
        def dfs(node, min_val, max_val):
            if not node:
                return max_val - min_val

            # Update min and max values for the current path
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            # Recursively call dfs for left and right children
            left_diff = dfs(node.left, min_val, max_val)
            right_diff = dfs(node.right, min_val, max_val)

            # Return the maximum difference found in either subtree
            return max(left_diff, right_diff)

        # Call dfs starting from the root with the root value as the initial min and max
        return dfs(root, root.val, root.val)

# Testing the implementation


def test_max_ancestor_diff():
    solution = Solution()

    # Test case 1
    # Tree structure:
    #         1
    #          \
    #           2
    #            \
    #             0
    #            /
    #           3
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.right = TreeNode(0)
    root1.right.right.left = TreeNode(3)
    # Expected output: 3 (The maximum difference is between the node 3 and its ancestor 0 or 1)
    result1 = solution.maxAncestorDiff(root1)
    print(f"Test 1 - Result: {result1}, Expected: 3")

    # Test case 2
    # Tree structure:
    #         8
    #        / \
    #       3   10
    #      / \    \
    #     1   6    14
    #        / \   /
    #       4   7 13
    root2 = TreeNode(8)
    root2.left = TreeNode(3)
    root2.right = TreeNode(10)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(6)
    root2.left.right.left = TreeNode(4)
    root2.left.right.right = TreeNode(7)
    root2.right.right = TreeNode(14)
    root2.right.right.left = TreeNode(13)
    # Expected output: 7 (Max diff is between node 1 and ancestor 8, or between node 14 and ancestor 8)
    result2 = solution.maxAncestorDiff(root2)
    print(f"Test 2 - Result: {result2}, Expected: 7")


# Run the test
test_max_ancestor_diff()
