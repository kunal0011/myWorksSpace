from typing import List, Optional
from collections import deque


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    LeetCode 199 - Binary Tree Right Side View

    Problem Statement:
    Given the root of a binary tree, imagine yourself standing on the right side of it,
    return the values of the nodes you can see ordered from top to bottom.

    Example:
    Input: [1,2,3,null,5,null,4]
    Output: [1,3,4]
    Explanation: Right side view contains nodes that are rightmost at each level
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Solution using BFS (Level Order Traversal)

        Logic:
        - Use level order traversal (BFS)
        - For each level, add the rightmost node value to result

        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(d) where d is the tree diameter
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            # Process all nodes at current level
            for i in range(level_size):
                node = queue.popleft()

                # If this is the rightmost node of the level
                if i == level_size - 1:
                    result.append(node.val)

                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    def rightSideView_dfs(self, root: Optional[TreeNode]) -> List[int]:
        """
        Alternative solution using DFS (Preorder Traversal)

        Logic:
        - Use preorder traversal but visit right child first
        - Keep track of levels and only add first node seen at each level

        Time Complexity: O(n)
        Space Complexity: O(h) where h is height of tree
        """
        def dfs(node: TreeNode, level: int, result: List[int]) -> None:
            if not node:
                return

            # Add value if this is the first node we've seen at this level
            if level == len(result):
                result.append(node.val)

            # Visit right child first
            dfs(node.right, level + 1, result)
            dfs(node.left, level + 1, result)

        result = []
        dfs(root, 0, result)
        return result


def create_tree(values: List[int], index: int = 0) -> Optional[TreeNode]:
    """Helper function to create a binary tree from a list of values"""
    if index >= len(values) or values[index] is None:
        return None

    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)
    root.right = create_tree(values, 2 * index + 2)
    return root


def run_tests():
    """Test driver for Binary Tree Right Side View solutions"""
    solution = Solution()

    test_cases = [
        {
            'input': [1, 2, 3, None, 5, None, 4],
            'expected': [1, 3, 4],
            'explanation': "Right side view shows 1, 3, and 4"
        },
        {
            'input': [1, None, 3],
            'expected': [1, 3],
            'explanation': "Tree with only right child"
        },
        {
            'input': [],
            'expected': [],
            'explanation': "Empty tree"
        },
        {
            'input': [1, 2, 3, 4],
            'expected': [1, 3, 4],
            'explanation': "Complete binary tree of height 2"
        }
    ]

    methods = [
        ('BFS Solution', solution.rightSideView),
        ('DFS Solution', solution.rightSideView_dfs)
    ]

    for method_name, method in methods:
        print(f"\nTesting {method_name}:")
        print("-" * 50)

        for i, test in enumerate(test_cases, 1):
            root = create_tree(test['input'])
            result = method(root)
            passed = result == test['expected']

            print(f"Test {i}:")
            print(f"Input: {test['input']}")
            print(f"Expected: {test['expected']}")
            print(f"Got: {result}")
            print(f"Explanation: {test['explanation']}")
            print(f"Result: {'✓ PASS' if passed else '✗ FAIL'}\n")


if __name__ == "__main__":
    run_tests()
