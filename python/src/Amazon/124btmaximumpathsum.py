"""
LeetCode 124. Binary Tree Maximum Path Sum

Problem Statement:
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the
sequence has an edge connecting them. A node can only appear in the sequence at most once.
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

     -10
     /  \
    9    20
        /  \
       15   7

Constraints:
- The number of nodes in the tree is in the range [1, 3 * 10^4]
- -1000 <= Node.val <= 1000
"""

from typing import List, Optional, Tuple
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        DFS approach with path tracking.
        Time complexity: O(n)
        Space complexity: O(h) where h is the height of the tree
        """
        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum

            if not node:
                return 0

            # Get the maximum gain from left and right subtrees
            # If the gain is negative, we don't include that path
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Current path sum including the node and both subtrees
            current_path_sum = node.val + left_gain + right_gain

            # Update maximum path sum if current path is larger
            max_sum = max(max_sum, current_path_sum)

            # Return maximum sum of path ending at current node
            # We can only include one subtree in the path that continues up
            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        max_gain(root)
        return max_sum

    def maxPathSumWithPath(self, root: Optional[TreeNode]) -> Tuple[int, List[int]]:
        """
        DFS approach that also returns the path with maximum sum.
        Time complexity: O(n)
        Space complexity: O(h) where h is the height of the tree
        """
        def max_gain_with_path(node: Optional[TreeNode]) -> Tuple[int, List[int]]:
            nonlocal max_sum, max_path

            if not node:
                return 0, []

            # Get maximum gains and paths from subtrees
            left_gain, left_path = max_gain_with_path(node.left)
            right_gain, right_path = max_gain_with_path(node.right)

            # Only include positive gains
            left_gain = max(left_gain, 0)
            right_gain = max(right_gain, 0)

            # Current path sum including the node and both subtrees
            current_path_sum = node.val + left_gain + right_gain

            # Update maximum path if current path is larger
            if current_path_sum > max_sum:
                max_sum = current_path_sum
                # Construct the path
                max_path = (left_path + [node.val] + right_path[::-1]
                            if right_gain > 0 else left_path + [node.val])
                if left_gain <= 0:
                    max_path = ([node.val] + right_path
                                if right_gain > 0 else [node.val])

            # For the path continuing up, choose the better subtree
            if left_gain > right_gain:
                return node.val + left_gain, left_path + [node.val]
            else:
                return node.val + right_gain, [node.val] + right_path

        max_sum = float('-inf')
        max_path = []
        max_gain_with_path(root)
        return max_sum, max_path


def create_binary_tree(values: List[Optional[int]], index: int = 0) -> Optional[TreeNode]:
    """Helper function to create a binary tree from a list of values."""
    if not values or index >= len(values) or values[index] is None:
        return None

    root = TreeNode(values[index])
    root.left = create_binary_tree(values, 2 * index + 1)
    root.right = create_binary_tree(values, 2 * index + 2)
    return root


def visualize_binary_tree(root: Optional[TreeNode], path: List[int] = None) -> None:
    """Helper function to visualize binary tree with highlighted path."""
    if not root:
        print("Empty tree")
        return

    def get_tree_height(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(get_tree_height(node.left), get_tree_height(node.right))

    def get_tree_string(node: Optional[TreeNode],
                        curr_height: int,
                        path: List[int] = None) -> List[str]:
        if not node:
            return [" " * (2 ** curr_height - 1)] * curr_height

        # Highlight node if it's in the path
        node_str = f"[{node.val}]" if path and node.val in path else f"{node.val}"
        node_str = node_str.center(3)

        if curr_height == 1:
            return [node_str]

        left_subtree = get_tree_string(node.left, curr_height - 1, path)
        right_subtree = get_tree_string(node.right, curr_height - 1, path)

        # Combine subtrees
        current_row = [node_str.center(2 ** curr_height - 1)]

        # Add branches
        below_row = [" " * (2 ** (curr_height - 1) - 1)]
        if node.left:
            below_row.append("/")
        else:
            below_row.append(" ")
        if node.right:
            below_row.append("\\")
        else:
            below_row.append(" ")
        below_row.append(" " * (2 ** (curr_height - 1) - 2))
        current_row.append("".join(below_row))

        # Combine rows
        for left_row, right_row in zip(left_subtree, right_subtree):
            spacing = " " * 1
            combined_row = f"{left_row}{spacing}{right_row}"
            current_row.append(combined_row)

        return current_row

    height = get_tree_height(root)
    tree_string = get_tree_string(root, height, path)
    print("\n".join(tree_string))


def test_max_path_sum():
    solution = Solution()

    test_cases = [
        {
            "values": [1, 2, 3],
            "expected": 6,
            "description": "Simple tree with positive values"
        },
        {
            "values": [-10, 9, 20, None, None, 15, 7],
            "expected": 42,
            "description": "Tree with negative root"
        },
        {
            "values": [-3],
            "expected": -3,
            "description": "Single negative node"
        },
        {
            "values": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
            "expected": 48,
            "description": "Complex tree"
        },
        {
            "values": [-1, -2, -3],
            "expected": -1,
            "description": "All negative values"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        values = test_case["values"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        root = create_binary_tree(values)

        # Test both implementations
        result1 = solution.maxPathSum(root)
        max_sum, max_path = solution.maxPathSumWithPath(root)

        print("\nBinary Tree Visualization:")
        print("(Path with maximum sum is highlighted)")
        visualize_binary_tree(root, max_path)

        print(f"\nMaximum path sum: {max_sum}")
        print(f"Path with maximum sum: {' -> '.join(map(str, max_path))}")

        assert result1 == expected and max_sum == expected, \
            f"Expected {expected}, but got {result1} (basic), {max_sum} (with path)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_max_path_sum()
    print("\nAll test cases passed! 🎉")
