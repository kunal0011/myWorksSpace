"""
LeetCode 103. Binary Tree Zigzag Level Order Traversal

Problem Statement:
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
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
- -100 <= Node.val <= 100
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

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

            # Reverse current level if needed
            if not left_to_right:
                current_level.reverse()

            result.append(current_level)
            left_to_right = not left_to_right

        return result

    def zigzagLevelOrderDFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Alternative solution using DFS"""
        def dfs(node: TreeNode, level: int, result: List[List[int]]) -> None:
            if not node:
                return

            # Add new level if needed
            if level == len(result):
                result.append([])

            # Add value to current level based on direction
            if level % 2 == 0:
                result[level].append(node.val)  # left to right
            else:
                result[level].insert(0, node.val)  # right to left

            # Process children
            dfs(node.left, level + 1, result)
            dfs(node.right, level + 1, result)

        result = []
        dfs(root, 0, result)
        return result


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
    """Helper function to visualize binary tree with zigzag indicators"""
    if not root:
        print("  " * level + prefix + "None")
        return

    direction = "→" if level % 2 == 0 else "←"
    print("  " * level + prefix + f"{root.val} {direction}")
    if root.left or root.right:
        visualize_tree(root.left, level + 1, "L--- ")
        visualize_tree(root.right, level + 1, "R--- ")


def test_zigzag_level_order():
    solution = Solution()

    test_cases = [
        {
            "values": [3, 9, 20, None, None, 15, 7],
            "expected": [[3], [20, 9], [15, 7]],
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
            "values": [1, 2, 3, 4, 5, 6, 7],
            "expected": [[1], [3, 2], [4, 5, 6, 7]],
            "description": "Complete binary tree"
        },
        {
            "values": [1, 2, 3, 4],
            "expected": [[1], [3, 2], [4]],
            "description": "Partial tree"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        values = test_case["values"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        root = create_binary_tree(values)

        print("\nTree structure (→ indicates left-to-right, ← indicates right-to-left):")
        visualize_tree(root)

        # Test both BFS and DFS solutions
        result_bfs = solution.zigzagLevelOrder(root)
        result_dfs = solution.zigzagLevelOrderDFS(root)

        print(f"\nBFS zigzag traversal: {result_bfs}")
        print(f"DFS zigzag traversal: {result_dfs}")

        assert result_bfs == expected and result_dfs == expected, \
            f"Expected {expected}, but got {result_bfs} (BFS) and {result_dfs} (DFS)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_zigzag_level_order()
    print("\nAll test cases passed! 🎉")
