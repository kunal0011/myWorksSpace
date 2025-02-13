"""
LeetCode 107. Binary Tree Level Order Traversal II

Problem Statement:
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
(i.e., from left to right, level by level from leaf to root).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
    3
   / \
  9  20
     /  \
   15    7

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 2000]
- -1000 <= Node.val <= 1000
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add current level to beginning of result
            result.insert(0, current_level)

        return result

    def levelOrderBottomDFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Alternative solution using DFS"""
        def dfs(node: TreeNode, level: int, levels: List[List[int]]) -> None:
            if not node:
                return

            # Add new level if needed
            if level == len(levels):
                levels.append([])

            # Add current node to its level
            levels[level].append(node.val)

            # Process children
            dfs(node.left, level + 1, levels)
            dfs(node.right, level + 1, levels)

        levels = []
        dfs(root, 0, levels)
        return levels[::-1]  # Reverse the levels


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
    """Helper function to visualize binary tree with level indicators"""
    if not root:
        print("  " * level + prefix + "None")
        return

    print("  " * level + prefix + f"{root.val} (level: {level})")
    if root.left or root.right:
        visualize_tree(root.left, level + 1, "L--- ")
        visualize_tree(root.right, level + 1, "R--- ")


def test_level_order_bottom():
    solution = Solution()

    test_cases = [
        {
            "values": [3, 9, 20, None, None, 15, 7],
            "expected": [[15, 7], [9, 20], [3]],
            "description": "Standard tree"
        },
        {
            "values": [1],
            "expected": [[1]],
            "description": "Single node"
        },
        {
            "values": [],
            "expected": [],
            "description": "Empty tree"
        },
        {
            "values": [1, 2, 3, 4, 5],
            "expected": [[4, 5], [2, 3], [1]],
            "description": "Complete binary tree"
        },
        {
            "values": [1, None, 2, None, 3],
            "expected": [[3], [2], [1]],
            "description": "Right-skewed tree"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        values = test_case["values"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        root = create_binary_tree(values)

        print("\nTree structure with level indicators:")
        visualize_tree(root)

        # Test both BFS and DFS solutions
        result_bfs = solution.levelOrderBottom(root)
        result_dfs = solution.levelOrderBottomDFS(root)

        print(f"\nBFS bottom-up traversal: {result_bfs}")
        print(f"DFS bottom-up traversal: {result_dfs}")

        assert result_bfs == expected and result_dfs == expected, \
            f"Expected {expected}, but got {result_bfs} (BFS) and {result_dfs} (DFS)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_level_order_bottom()
    print("\nAll test cases passed! 🎉")
