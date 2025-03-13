"""
LeetCode 654: Maximum Binary Tree

Problem Statement:
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:
1. Create a root node whose value is the maximum value in nums.
2. Recursively build the left subtree on the subarray prefix to the left of the maximum value.
3. Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Optimized solution using monotonic stack
        Time complexity: O(n)
        Space complexity: O(n)
        """
        stack = []

        for num in nums:
            node = TreeNode(num)

            while stack and stack[-1].val < num:
                node.left = stack.pop()

            if stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0] if stack else None

    def constructMaximumBinaryTree_recursive(self, nums: List[int]) -> Optional[TreeNode]:
        """Original recursive solution - kept for comparison
        Time complexity: O(n^2) worst case
        Space complexity: O(n) for recursion stack
        """
        # Base case: if nums is empty, return None
        if not nums:
            return None

        # Find the index of the maximum element in nums
        max_index = nums.index(max(nums))

        # Create the root node with the maximum value
        root = TreeNode(nums[max_index])

        # Recursively construct the left subtree
        root.left = self.constructMaximumBinaryTree_recursive(nums[:max_index])

        # Recursively construct the right subtree
        root.right = self.constructMaximumBinaryTree_recursive(nums[max_index + 1:])

        return root


def print_tree(root: TreeNode, level: int = 0, prefix: str = "Root: ") -> None:
    """Helper function to visualize the tree structure"""
    if not root:
        return

    print("  " * level + prefix + str(root.val))
    if root.left:
        print_tree(root.left, level + 1, "L--- ")
    if root.right:
        print_tree(root.right, level + 1, "R--- ")


def test_solution():
    """Comprehensive test driver"""
    solution = Solution()

    test_cases = [
        ([3, 2, 1, 6, 0, 5], "Basic test case"),
        ([1, 2, 3, 4, 5], "Increasing sequence"),
        ([5, 4, 3, 2, 1], "Decreasing sequence"),
        ([1], "Single element"),
        ([], "Empty array")
    ]

    for nums, description in test_cases:
        print(f"\nTest Case: {description}")
        print(f"Input array: {nums}")

        # Test both implementations
        root1 = solution.constructMaximumBinaryTree(nums)
        root2 = solution.constructMaximumBinaryTree_recursive(nums)

        print("\nOptimized Solution (Stack-based):")
        print_tree(root1)
        print("\nRecursive Solution:")
        print_tree(root2)
        print("-" * 50)


if __name__ == "__main__":
    test_solution()
