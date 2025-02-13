"""
LeetCode 113. Path Sum II

Problem Statement:
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths
where the sum of the node values in the path equals targetSum. Each path should be
returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 5000]
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """Recursive DFS solution with backtracking"""
        def dfs(node: TreeNode, remaining: int, path: List[int], paths: List[List[int]]) -> None:
            if not node:
                return

            # Add current node to path
            path.append(node.val)

            # Check if we've reached a leaf node and found target sum
            if not node.left and not node.right and remaining == node.val:
                paths.append(path[:])  # Make a copy of the current path

            # Recursively explore left and right subtrees
            dfs(node.left, remaining - node.val, path, paths)
            dfs(node.right, remaining - node.val, path, paths)

            # Backtrack by removing current node from path
            path.pop()

        paths = []
        dfs(root, targetSum, [], paths)
        return paths

    def pathSumIterative(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """Iterative DFS solution using stack"""
        if not root:
            return []

        # Stack stores (node, current_sum, path) tuples
        stack = [(root, root.val, [root.val])]
        paths = []

        while stack:
            node, curr_sum, path = stack.pop()

            # Check leaf nodes
            if not node.left and not node.right and curr_sum == targetSum:
                paths.append(path)

            # Add right child first (so left is processed first)
            if node.right:
                stack.append((node.right,
                              curr_sum + node.right.val,
                              path + [node.right.val]))
            if node.left:
                stack.append((node.left,
                              curr_sum + node.left.val,
                              path + [node.left.val]))

        return paths

    def pathSumBFS(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """BFS solution using queue"""
        if not root:
            return []

        # Queue stores (node, current_sum, path) tuples
        queue = deque([(root, root.val, [root.val])])
        paths = []

        while queue:
            node, curr_sum, path = queue.popleft()

            # Check leaf nodes
            if not node.left and not node.right and curr_sum == targetSum:
                paths.append(path)

            if node.left:
                queue.append((node.left,
                              curr_sum + node.left.val,
                              path + [node.left.val]))
            if node.right:
                queue.append((node.right,
                              curr_sum + node.right.val,
                              path + [node.right.val]))

        return paths


def create_binary_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
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


def visualize_tree(root: TreeNode, level: int = 0, prefix: str = "Root: ", path: List[int] = None) -> None:
    """Helper function to visualize binary tree with path sums and current path"""
    if not root:
        print("  " * level + prefix + "None")
        return

    if path is None:
        path = []

    path.append(root.val)
    path_sum = sum(path)

    print("  " * level + prefix +
          f"{root.val} (path: {path}, sum: {path_sum})")

    if root.left or root.right:
        visualize_tree(root.left, level + 1, "L--- ", path.copy())
        visualize_tree(root.right, level + 1, "R--- ", path.copy())


def test_path_sum():
    solution = Solution()

    test_cases = [
        {
            "values": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
            "targetSum": 22,
            "expected": [[5, 4, 11, 2], [5, 8, 4, 5]],
            "description": "Multiple valid paths"
        },
        {
            "values": [1, 2, 3],
            "targetSum": 5,
            "expected": [],
            "description": "No valid paths"
        },
        {
            "values": [1, 2],
            "targetSum": 0,
            "expected": [],
            "description": "Target sum not possible"
        },
        {
            "values": [],
            "targetSum": 0,
            "expected": [],
            "description": "Empty tree"
        },
        {
            "values": [-2, None, -3],
            "targetSum": -5,
            "expected": [[-2, -3]],
            "description": "Negative values"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        values = test_case["values"]
        target_sum = test_case["targetSum"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        root = create_binary_tree(values)

        print(f"\nTarget sum: {target_sum}")
        print("Tree structure with paths and sums:")
        visualize_tree(root)

        # Test all three approaches
        result_recursive = solution.pathSum(root, target_sum)
        result_iterative = solution.pathSumIterative(root, target_sum)
        result_bfs = solution.pathSumBFS(root, target_sum)

        print(f"\nRecursive DFS paths: {result_recursive}")
        print(f"Iterative DFS paths: {result_iterative}")
        print(f"BFS paths: {result_bfs}")

        # Sort paths for comparison since order doesn't matter
        result_recursive.sort()
        result_iterative.sort()
        result_bfs.sort()
        expected.sort()

        assert result_recursive == expected and \
            result_iterative == expected and \
            result_bfs == expected, \
            f"Expected {expected}, but got {result_recursive} (recursive), " \
            f"{result_iterative} (iterative), {result_bfs} (BFS)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_path_sum()
    print("\nAll test cases passed! 🎉")
