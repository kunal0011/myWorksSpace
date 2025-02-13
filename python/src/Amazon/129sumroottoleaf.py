"""
LeetCode 129. Sum Root to Leaf Numbers

Problem Statement:
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
- For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers.
A leaf node is a node with no children.

Example 1:
    1
   / \
  2   3
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12
The root-to-leaf path 1->3 represents the number 13
Therefore, sum = 12 + 13 = 25

Example 2:
    4
   / \
  9   0
 / \
5   1
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495
The root-to-leaf path 4->9->1 represents the number 491
The root-to-leaf path 4->0 represents the number 40
Therefore, sum = 495 + 491 + 40 = 1026

Constraints:
- The number of nodes in the tree is in the range [1, 1000]
- 0 <= Node.val <= 9
- The depth of the tree will not exceed 10
"""

from typing import Optional, List, Tuple
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        DFS approach.
        Time complexity: O(N) where N is number of nodes
        Space complexity: O(H) where H is height of tree
        """
        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0

            # Calculate current number
            current_sum = current_sum * 10 + node.val

            # If leaf node, return the current number
            if not node.left and not node.right:
                return current_sum

            # Recursively calculate sum for left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)

    def sumNumbersIterative(self, root: Optional[TreeNode]) -> int:
        """
        Iterative BFS approach.
        Time complexity: O(N)
        Space complexity: O(W) where W is max width of tree
        """
        if not root:
            return 0

        total_sum = 0
        queue = deque([(root, root.val)])

        while queue:
            node, current_sum = queue.popleft()

            # If leaf node, add to total
            if not node.left and not node.right:
                total_sum += current_sum

            # Add left child to queue
            if node.left:
                queue.append((node.left, current_sum * 10 + node.left.val))

            # Add right child to queue
            if node.right:
                queue.append((node.right, current_sum * 10 + node.right.val))

        return total_sum

    def sumNumbersWithPaths(self, root: Optional[TreeNode]) -> Tuple[int, List[List[int]]]:
        """
        Returns both sum and all paths.
        Time complexity: O(N)
        Space complexity: O(N)
        """
        def dfs(node: Optional[TreeNode], current_path: List[int],
                all_paths: List[List[int]]) -> int:
            if not node:
                return 0

            current_path.append(node.val)

            if not node.left and not node.right:
                all_paths.append(current_path[:])
                path_sum = int(''.join(map(str, current_path)))
                current_path.pop()
                return path_sum

            total = dfs(node.left, current_path, all_paths) + \
                dfs(node.right, current_path, all_paths)
            current_path.pop()
            return total

        all_paths = []
        total_sum = dfs(root, [], all_paths)
        return total_sum, all_paths


def create_binary_tree(values: List[int]) -> Optional[TreeNode]:
    """Helper function to create a binary tree from a list of values."""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def visualize_paths(paths: List[List[int]]) -> None:
    """Helper function to visualize all root-to-leaf paths and their numbers."""
    print("\nRoot-to-leaf paths:")
    for path in paths:
        number = int(''.join(map(str, path)))
        print(f"Path {' -> '.join(map(str, path))} = {number}")


def test_sum_numbers():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "values": [1, 2, 3],
            "expected": 25,
            "description": "Basic tree with two leaves"
        },
        {
            "values": [4, 9, 0, 5, 1],
            "expected": 1026,
            "description": "Tree with three leaves"
        },
        {
            "values": [1],
            "expected": 1,
            "description": "Single node tree"
        },
        {
            "values": [1, 2, None, 3],
            "expected": 123,
            "description": "Left-skewed tree"
        },
        {
            "values": [0, 1, 2, None, 3, 4],
            "expected": 37,
            "description": "Complex tree structure"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Tree values: {test_case['values']}")

        root = create_binary_tree(test_case['values'])

        # Test all implementations
        result1 = solution.sumNumbers(root)
        result2 = solution.sumNumbersIterative(root)
        result3, paths = solution.sumNumbersWithPaths(root)

        print(f"\nResults:")
        print(f"DFS approach sum: {result1}")
        print(f"BFS approach sum: {result2}")
        print(f"Path tracking sum: {result3}")

        # Visualize paths
        visualize_paths(paths)

        assert result1 == test_case['expected'], \
            f"DFS approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"BFS approach failed. Expected {test_case['expected']}, got {result2}"
        assert result3 == test_case['expected'], \
            f"Path tracking failed. Expected {test_case['expected']}, got {result3}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_sum_numbers()
