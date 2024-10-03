# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_zigzag = 0

        # Helper function to perform DFS
        def dfs(node, direction, length):
            if not node:
                return
            # Update the maximum ZigZag length found so far
            self.max_zigzag = max(self.max_zigzag, length)

            if direction == 'left':
                # Move to the left (continue zigzagging)
                dfs(node.left, 'right', length + 1)
                # Reset the path when moving right
                dfs(node.right, 'left', 1)
            elif direction == 'right':
                # Move to the right (continue zigzagging)
                dfs(node.right, 'left', length + 1)
                # Reset the path when moving left
                dfs(node.left, 'right', 1)

        # Start the DFS from the root in both directions
        dfs(root, 'left', 0)
        dfs(root, 'right', 0)

        return self.max_zigzag

# Test the Solution class


def test_solution():
    sol = Solution()

    # Test case 1
    root = TreeNode(1, None, TreeNode(1, TreeNode(
        1, None, TreeNode(1)), TreeNode(1, None, TreeNode(1))))
    assert sol.longestZigZag(root) == 3

    # Test case 2
    root = TreeNode(1)
    assert sol.longestZigZag(root) == 0

    # Test case 3
    root = TreeNode(1, TreeNode(1), TreeNode(1))
    assert sol.longestZigZag(root) == 1

    print("All test cases passed!")


# Run the tests
test_solution()
