# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if the node is None, the depth is 0
        if not root:
            return 0

        # Recursive case: compute the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Return the maximum of the two depths plus one (for the current node)
        return max(left_depth, right_depth) + 1

# Test cases


def test_maxDepth():
    sol = Solution()

    # Test Case 1: Balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    # The depth of this tree is 3
    assert sol.maxDepth(root1) == 3, "Test Case 1 Failed"

    # Test Case 2: Tree with only left children
    root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))
    # The depth of this tree is 5
    assert sol.maxDepth(root2) == 5, "Test Case 2 Failed"

    # Test Case 3: Single node tree
    root3 = TreeNode(1)
    # The depth of this tree is 1
    assert sol.maxDepth(root3) == 1, "Test Case 3 Failed"

    # Test Case 4: Empty tree
    root4 = None
    # The depth of an empty tree is 0
    assert sol.maxDepth(root4) == 0, "Test Case 4 Failed"

    print("All test cases passed!")


# Run the tests
test_maxDepth()
