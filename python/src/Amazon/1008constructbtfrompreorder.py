# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode:
        # Helper function to recursively insert a new node into the BST
        def helper(lower=float('-inf'), upper=float('inf')):
            nonlocal idx
            if idx == len(preorder):
                return None

            val = preorder[idx]
            # If the current value doesn't fit in the current bounds, return None
            if val < lower or val > upper:
                return None

            # Move to the next element in the preorder traversal
            idx += 1
            root = TreeNode(val)
            # All elements in the left subtree must be smaller than `val`
            root.left = helper(lower, val)
            # All elements in the right subtree must be greater than `val`
            root.right = helper(val, upper)
            return root

        idx = 0  # Start from the first element of the preorder traversal
        return helper()

# Testing the implementation


def print_inorder(root: TreeNode):
    if root is not None:
        print_inorder(root.left)
        print(root.val, end=' ')
        print_inorder(root.right)


def test_bst_from_preorder():
    solution = Solution()

    # Test case 1
    preorder1 = [8, 5, 1, 7, 10, 12]
    # Expected output: Inorder traversal of the tree should be [1, 5, 7, 8, 10, 12]
    root1 = solution.bstFromPreorder(preorder1)
    print("Test 1 - Inorder Traversal: ", end='')
    print_inorder(root1)  # Output should be in ascending order
    print()

    # Test case 2
    preorder2 = [4, 2]
    # Expected output: Inorder traversal of the tree should be [2, 4]
    root2 = solution.bstFromPreorder(preorder2)
    print("Test 2 - Inorder Traversal: ", end='')
    print_inorder(root2)
    print()

    # Test case 3
    preorder3 = [10, 5, 15, 12, 20]
    # Expected output: Inorder traversal of the tree should be [5, 10, 12, 15, 20]
    root3 = solution.bstFromPreorder(preorder3)
    print("Test 3 - Inorder Traversal: ", end='')
    print_inorder(root3)
    print()


# Run the test
test_bst_from_preorder()
