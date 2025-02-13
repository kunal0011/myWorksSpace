"""
LeetCode 112. Path Sum

Problem Statement:
Given the root of a binary tree and an integer targetSum, return true if the tree has a 
root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:
Input: root = [], targetSum = 0
Output: false

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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Recursive DFS solution"""
        if not root:
            return False

        # If it's a leaf node, check if current path sum equals target
        if not root.left and not root.right:
            return root.val == targetSum

        # Recursively check left and right subtrees with remaining sum
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))

    def hasPathSumIterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Iterative DFS solution using stack"""
        if not root:
            return False

        # Stack stores (node, current_sum) pairs
        stack = [(root, root.val)]

        while stack:
            node, curr_sum = stack.pop()

            # Check leaf nodes
            if not node.left and not node.right and curr_sum == targetSum:
                return True

            # Add right child first (so left is processed first)
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))

        return False

    def hasPathSumBFS(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """BFS solution using queue"""
        if not root:
            return False

        # Queue stores (node, current_sum) pairs
        queue = deque([(root, root.val)])

        while queue:
            node, curr_sum = queue.popleft()

            # Check leaf nodes
            if not node.left and not node.right and curr_sum == targetSum:
                return True

            if node.left:
                queue.append((node.left, curr_sum + node.left.val))
            if node.right:
                queue.append((node.right, curr_sum + node.right.val))

        return False


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


def visualize_tree(root: TreeNode, level: int = 0, prefix: str = "Root: ", path_sum: int = 0) -> None:
    """Helper function to visualize binary tree with path sums"""
    if not root:
        print("  " * level + prefix + "None")
        return

    current_sum = path_sum + root.val
    print("  " * level + prefix + f"{root.val} (path sum: {current_sum})")

    if root.left or root.right:
        visualize_tree(root.left, level + 1, "L--- ", current_sum)
        visualize_tree(root.right, level + 1, "R--- ", current_sum)


def test_has_path_sum():
    solution = Solution()

    test_cases = [
        {
            "values": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
            "targetSum": 22,
            "expected": True,
            "description": "Standard case with valid path"
        },
        {
            "values": [1, 2, 3],
            "targetSum": 5,
            "expected": False,
            "description": "No valid path"
        },
        {
            "values": [],
            "targetSum": 0,
            "expected": False,
            "description": "Empty tree"
        },
        {
            "values": [1, 2],
            "targetSum": 1,
            "expected": False,
            "description": "Path must end at leaf"
        },
        {
            "values": [-2, None, -3],
            "targetSum": -5,
            "expected": True,
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
        print("Tree structure with path sums:")
        visualize_tree(root)

        # Test all three approaches
        result_recursive = solution.hasPathSum(root, target_sum)
        result_iterative = solution.hasPathSumIterative(root, target_sum)
        result_bfs = solution.hasPathSumBFS(root, target_sum)

        print(f"\nRecursive DFS result: {result_recursive}")
        print(f"Iterative DFS result: {result_iterative}")
        print(f"BFS result: {result_bfs}")

        assert result_recursive == expected and \
            result_iterative == expected and \
            result_bfs == expected, \
            f"Expected {expected}, but got {result_recursive} (recursive), " \
            f"{result_iterative} (iterative), {result_bfs} (BFS)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_has_path_sum()
    print("\nAll test cases passed! 🎉")
