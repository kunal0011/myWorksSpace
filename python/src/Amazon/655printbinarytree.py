"""
LeetCode 655: Print Binary Tree

Problem Statement:
Given the root of a binary tree, construct a 0-indexed m x n string matrix res that 
represents this tree using the following rules:
- The row number m should be equal to the height of the tree
- The column number n should be equal to 2^height - 1
- The root node is at position (0, (n-1)/2) in matrix
- For each node at (r, c), its left child is at (r+1, c-2^(height-r-2)) and 
  its right child is at (r+1, c+2^(height-r-2))
- Empty spots should be filled with empty string ""
Return the constructed matrix res.
"""

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        if not root:
            return []

        # Helper function to compute height of tree
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        # Get height & calculate grid width
        height = get_height(root)
        width = (1 << height) - 1  # 2^height - 1
        res = [[""] * width for _ in range(height)]  # Res grid init

        # Fill the matrix
        def fill_matrix(node: Optional[TreeNode], row: int, col: int):
            if not node:
                return
            res[row][col] = str(node.val)
            offset = 1 << (height - row - 2)  # Calculates 2^(height-row-2)
            fill_matrix(node.left, row + 1, col - offset)  # Left child fill
            fill_matrix(node.right, row + 1, col + offset)  # Right child fill

        # Start filling matrix
        fill_matrix(root, 0, (width - 1) // 2)
        return res


# Helper function to create a binary tree
def create_tree(values: list, index: int = 0) -> Optional[TreeNode]:
    """Creates a binary tree from the list values"""
    if index >= len(values) or values[index] is None:
        return None

    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)  # Left child
    root.right = create_tree(values, 2 * index + 2)  # Right child
    return root


# Helper function to print matrix
def print_matrix(matrix: List[List[str]]) -> None:
    """Print the matrix in a readable format"""
    for row in matrix:
        print("[" + ", ".join(f"'{cell}'" if cell else '""' for cell in row) + "]")


# Test driver for solution's cases
def test_solution():
    """Run solution for several test cases"""
    solution = Solution()
    test_cases = [
        ([1,2,3,None,4], "Basic tree"),
        ([1], "Single node"),
        ([1,2,3,4,5], "Complete binary tree"),
        ([1,2], "Tree with left child only"),
        ([], "Empty tree")
    ]

    for values, description in test_cases:
        print(f"\nTest Case: {description}")
        print(f"Input values: {values}")
        root = create_tree(values)
        result = solution.printTree(root)
        print("Output matrix:")
        print_matrix(result)
        print("-" * 50)


if __name__ == "__main__":
    test_solution()
