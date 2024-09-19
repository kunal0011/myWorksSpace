# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # Base case: if root is null or if we find the node with the value
        if not root or root.val == val:
            return root

        # If the value is less than the current node's value, search the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        # Otherwise, search the right subtree
        else:
            return self.searchBST(root.right, val)

# Helper function to print the subtree


def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


# Test the function
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    val1 = 2
    result1 = sol.searchBST(root1, val1)
    print(inorder_traversal(result1))  # Output: [1, 2, 3]

    # Test case 2
    root2 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    val2 = 5
    result2 = sol.searchBST(root2, val2)
    print(inorder_traversal(result2))  # Output: []
