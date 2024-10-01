# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []

        def dfs(node):
            if not node:
                return
            # Traverse left subtree
            dfs(node.left)
            # Visit node
            result.append(node.val)
            # Traverse right subtree
            dfs(node.right)

        dfs(root)
        return result

# Test cases


def test_inorderTraversal():
    sol = Solution()

    # Test Case 1: Standard binary tree
    root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert sol.inorderTraversal(root1) == [1, 3, 2], "Test Case 1 Failed"

    #
