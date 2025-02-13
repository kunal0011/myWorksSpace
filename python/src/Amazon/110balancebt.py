"""
LeetCode 110. Balanced Binary Tree

Problem Statement:
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the left and right subtrees 
of every node differ in height by no more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
    3
   / \
  9  20
     /  \
   15    7

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
    1
   / \
  2   2
 / \
3   3
/\
4 4

Example 3:
Input: root = []
Output: true

Constraints:
- The number of nodes in the tree is in the range [0, 5000]
- -10^4 <= Node.val <= 10^4
"""

from collections import deque
from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Bottom-up approach with early termination"""
        def check_height(node: TreeNode) -> int:
            if not node:
                return 0

            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1

            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1

            # Check balance condition
            if abs(left_height - right_height) > 1:
                return -1

            # Return height of current subtree
            return 1 + max(left_height, right_height)

        return check_height(root) != -1

    def isBalancedTopDown(self, root: Optional[TreeNode]) -> bool:
        """Top-down approach (less efficient but more intuitive)"""
        if not root:
            return True

        def get_height(node: TreeNode) -> int:
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        # Check balance at current node
        if abs(get_height(root.left) - get_height(root.right)) > 1:
            return False

        # Recursively check left and right subtrees
        return self.isBalancedTopDown(root.left) and self.isBalancedTopDown(root.right)

    def isBalancedIterative(self, root: Optional[TreeNode]) -> bool:
        """Iterative approach using stack"""
        if not root:
            return True

        # Stack stores (node, processed) pairs
        stack = [(root, False)]
        heights = {}  # Store heights of processed nodes

        while stack:
            node, processed = stack.pop()

            if not processed:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
            else:
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)

                if abs(left_height - right_height) > 1:
                    return False

                heights[node] = 1 + max(left_height, right_height)

        return True


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


def visualize_tree(root: TreeNode, level: int = 0, prefix: str = "Root: ") -> None:
    """Helper function to visualize binary tree with height and balance information"""
    if not root:
        print("  " * level + prefix + "None")
        return

    def get_height_and_balance(node: TreeNode) -> Tuple[int, int]:
        if not node:
            return (0, 0)

        left_height, _ = get_height_and_balance(node.left)
        right_height, _ = get_height_and_balance(node.right)
        balance = right_height - left_height

        return (1 + max(left_height, right_height), balance)

    height, balance = get_height_and_balance(root)
    print("  " * level + prefix +
          f"{root.val} (height: {height}, balance: {balance})")

    if root.left or root.right:
        visualize_tree(root.left, level + 1, "L--- ")
        visualize_tree(root.right, level + 1, "R--- ")


def test_is_balanced():
    solution = Solution()

    test_cases = [
        {
            "values": [3, 9, 20, None, None, 15, 7],
            "expected": True,
            "description": "Balanced tree"
        },
        {
            "values": [1, 2, 2, 3, 3, None, None, 4, 4],
            "expected": False,
            "description": "Unbalanced tree"
        },
        {
            "values": [],
            "expected": True,
            "description": "Empty tree"
        },
        {
            "values": [1],
            "expected": True,
            "description": "Single node"
        },
        {
            "values": [1, 2, 3, 4, 5, 6, 7],
            "expected": True,
            "description": "Perfect binary tree"
        },
        {
            "values": [1, 2, None, 3],
            "expected": False,
            "description": "Left-heavy unbalanced tree"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        values = test_case["values"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        root = create_binary_tree(values)

        print("\nTree structure with height and balance information:")
        visualize_tree(root)

        # Test all three approaches
        result_bottom_up = solution.isBalanced(root)
        result_top_down = solution.isBalancedTopDown(root)
        result_iterative = solution.isBalancedIterative(root)

        print(f"\nBottom-up result: {result_bottom_up}")
        print(f"Top-down result: {result_top_down}")
        print(f"Iterative result: {result_iterative}")

        assert result_bottom_up == expected and \
            result_top_down == expected and \
            result_iterative == expected, \
            f"Expected {expected}, but got {result_bottom_up} (bottom-up), " \
            f"{result_top_down} (top-down), {result_iterative} (iterative)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_is_balanced()
    print("\nAll test cases passed! 🎉")
