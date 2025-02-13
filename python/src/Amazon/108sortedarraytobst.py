"""
LeetCode 108. Convert Sorted Array to Binary Search Tree

Problem Statement:
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two 
subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted
    0
   / \
 -3   9
 /   /
-10  5

Example 2:
Input: nums = [1,3]
Output: [3,1]
    3
   /
  1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in a strictly increasing order
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """Recursive solution"""
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # Choose middle element as root
            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            # Recursively build left and right subtrees
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)

            return root

        return build_bst(0, len(nums) - 1)

    def sortedArrayToBSTIterative(self, nums: List[int]) -> Optional[TreeNode]:
        """Iterative solution using stack"""
        if not nums:
            return None

        # Create root node
        root = TreeNode(nums[len(nums) // 2])
        # Stack elements: (node, left_index, right_index, is_left_child)
        stack = [(root, 0, len(nums) - 1, False)]

        while stack:
            node, left, right, is_left = stack.pop()

            if is_left:
                # Process left subtree
                if left <= right:
                    mid = (left + right) // 2
                    node.left = TreeNode(nums[mid])
                    # Add right child of left subtree
                    if mid + 1 <= right:
                        stack.append((node.left, mid + 1, right, False))
                    # Add left child of left subtree
                    if left <= mid - 1:
                        stack.append((node.left, left, mid - 1, True))
            else:
                # Process right subtree
                if left <= right:
                    mid = (left + right) // 2
                    node.right = TreeNode(nums[mid])
                    # Add right child of right subtree
                    if mid + 1 <= right:
                        stack.append((node.right, mid + 1, right, False))
                    # Add left child of right subtree
                    if left <= mid - 1:
                        stack.append((node.right, left, mid - 1, True))

        return root


def tree_to_list(root: TreeNode) -> List[Optional[int]]:
    """Convert binary tree to level-order list representation"""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


def visualize_tree(root: TreeNode, level: int = 0, prefix: str = "Root: ") -> None:
    """Helper function to visualize binary tree with balance indicators"""
    if not root:
        print("  " * level + prefix + "None")
        return

    def get_height(node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))

    left_height = get_height(root.left)
    right_height = get_height(root.right)
    balance = right_height - left_height

    print("  " * level + prefix + f"{root.val} (balance: {balance})")
    if root.left or root.right:
        visualize_tree(root.left, level + 1, "L--- ")
        visualize_tree(root.right, level + 1, "R--- ")


def is_balanced(root: TreeNode) -> bool:
    """Check if tree is height-balanced"""
    def check_height(node: TreeNode) -> int:
        if not node:
            return 0

        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return check_height(root) != -1


def test_sorted_array_to_bst():
    solution = Solution()

    test_cases = [
        {
            "nums": [-10, -3, 0, 5, 9],
            "description": "Standard case"
        },
        {
            "nums": [1, 3],
            "description": "Two elements"
        },
        {
            "nums": [1],
            "description": "Single element"
        },
        {
            "nums": [1, 2, 3, 4, 5, 6, 7],
            "description": "Odd number of elements"
        },
        {
            "nums": [-5, -4, -3, -2, -1, 0, 1, 2],
            "description": "Even number of elements"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Input array: {nums}")

        # Test both recursive and iterative solutions
        root_recursive = solution.sortedArrayToBST(nums)
        root_iterative = solution.sortedArrayToBSTIterative(nums)

        print("\nRecursive solution tree:")
        visualize_tree(root_recursive)
        print("\nIterative solution tree:")
        visualize_tree(root_iterative)

        # Verify both trees are height-balanced
        assert is_balanced(
            root_recursive), "Recursive solution is not balanced"
        assert is_balanced(
            root_iterative), "Iterative solution is not balanced"

        # Verify both trees contain all elements
        result_recursive = tree_to_list(root_recursive)
        result_iterative = tree_to_list(root_iterative)

        assert sorted(result_recursive) == sorted(nums), \
            f"Recursive solution missing elements: {set(nums) - set(result_recursive)}"
        assert sorted(result_iterative) == sorted(nums), \
            f"Iterative solution missing elements: {set(nums) - set(result_iterative)}"

        print("✓ Test case passed!")


if __name__ == "__main__":
    test_sorted_array_to_bst()
    print("\nAll test cases passed! 🎉")
