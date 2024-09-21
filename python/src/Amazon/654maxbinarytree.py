# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # Base case: if nums is empty, return None
        if not nums:
            return None

        # Find the index of the maximum element in nums
        max_index = nums.index(max(nums))

        # Create the root node with the maximum value
        root = TreeNode(nums[max_index])

        # Recursively construct the left subtree
        root.left = self.constructMaximumBinaryTree(nums[:max_index])

        # Recursively construct the right subtree
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])

        return root

# Helper function to print the tree in preorder for testing


def preorder_traversal(root):
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


# Test the function
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [3, 2, 1, 6, 0, 5]
    root1 = sol.constructMaximumBinaryTree(nums1)
    print(preorder_traversal(root1))  # Output: [6, 3, 2, 1, 5, 0]

    # Test case 2
    nums2 = [1, 2, 3, 4, 5]
    root2 = sol.constructMaximumBinaryTree(nums2)
    print(preorder_traversal(root2))  # Output: [5, 4, 3, 2, 1]
