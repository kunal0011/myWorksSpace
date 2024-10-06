# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def height(node: TreeNode) -> int:
            if not node:
                return 0
            # Recursively get the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # Update the diameter if the path through this node is larger
            self.diameter = max(self.diameter, left_height + right_height)

            # Return the height of this node
            return 1 + max(left_height, right_height)

        height(root)
        return self.diameter

# Test cases


def test_diameter_of_binary_tree():
    solution = Solution()

    # Test case 1: Full binary tree
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    expected_result_1 = 3  # Path: 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3
    assert solution.diameterOfBinaryTree(
        root1) == expected_result_1, "Test case 1 failed"

    # Test case 2: Only left subtree
    #
