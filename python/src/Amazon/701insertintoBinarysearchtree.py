# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # If the root is null, create a new TreeNode
        if not root:
            return TreeNode(val)

        # Traverse the tree to find the correct position for the new value
        if val < root.val:
            # Insert into the left subtree
            root.left = self.insertIntoBST(root.left, val)
        else:
            # Insert into the right subtree
            root.right = self.insertIntoBST(root.right, val)

        return root

# Helper function to print the tree in-order


def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


# Test the function
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    val1 = 5
    result1 = sol.insertIntoBST(root1, val1)
    print(inorder_traversal(result1))  # Output: [1, 2, 3, 4, 5, 7]

    # Test case 2
    root2 = TreeNode(40, TreeNode(20, TreeNode(10), TreeNode(30)),
                     TreeNode(60, TreeNode(50), TreeNode(70)))
    val2 = 25
    result2 = sol.insertIntoBST(root2, val2)
    # Output: [10, 20, 25, 30, 40, 50, 60, 70]
    print(inorder_traversal(result2))
