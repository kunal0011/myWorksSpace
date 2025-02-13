"""
LeetCode 104. Maximum Depth of Binary Tree

Problem Statement:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
    3
   / \
  9  20
     /  \
   15    7

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Constraints:
- The number of nodes in the tree is in the range [0, 10^4]
- -100 <= Node.val <= 100
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Recursive DFS solution"""
        if not root:
            return 0

        # Maximum depth is 1 (current node) plus the maximum of left and right subtrees
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        """Iterative BFS solution"""
        if not root:
            return 0

        queue = deque([(root, 1)])  # (node, depth) pairs
        max_depth = 0

        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return max_depth

    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        """Iterative DFS solution using stack"""
        if not root:
            return 0

        stack = [(root, 1)]  # (node, depth) pairs
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.right:  # Push right first for left-to-right traversal
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

        return max_depth


def create_binary_tree(values: list) -> TreeNode:
    """Helper function to create binary tree from list of values"""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def visualize_tree(root: TreeNode, level: int = 0, prefix: str = "Root: ") -> None:
    """Helper function to visualize binary tree with depth indicators"""
    if not root:
        print("  " * level + prefix + "None")
        return

    print("  " * level + prefix + f"{root.val} (depth: {level + 1})")
    if root.left or root.right:
        visualize_tree(root.left, level + 1, "L--- ")
        visualize_tree(root.right, level + 1, "R--- ")


def test_max_depth():
    solution = Solution()

    test_cases = [
        {
            "values": [3, 9, 20, None, None, 15, 7],
            "expected": 3,
            "description": "Standard tree"
        },
        {
            "values": [1, None, 2],
            "expected": 2,
            "description": "Right-skewed tree"
        },
        {
            "values": [],
            "expected": 0,
            "description": "Empty tree"
        },
        {
            "values": [1],
            "expected": 1,
            "description": "Single node"
        },
        {
            "values": [1, 2, 3, 4, 5, 6, 7, 8],
            "expected": 4,
            "description": "Complete binary tree"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        values = test_case["values"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        root = create_binary_tree(values)

        print("\nTree structure with depth indicators:")
        visualize_tree(root)

        # Test all three solutions
        result_recursive = solution.maxDepth(root)
        result_bfs = solution.maxDepthBFS(root)
        result_dfs = solution.maxDepthDFS(root)

        print(f"\nRecursive DFS result: {result_recursive}")
        print(f"Iterative BFS result: {result_bfs}")
        print(f"Iterative DFS result: {result_dfs}")

        assert result_recursive == expected and result_bfs == expected and result_dfs == expected, \
            f"Expected {expected}, but got {result_recursive} (recursive), {result_bfs} (BFS), {result_dfs} (DFS)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_max_depth()
    print("\nAll test cases passed! 🎉")
