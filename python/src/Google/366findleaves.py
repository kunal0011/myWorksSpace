"""
LeetCode 366 - Find Leaves of Binary Tree

Given the root of a binary tree, collect a tree's nodes as if you were doing this:
- Collect all the leaf nodes.
- Remove all the leaf nodes.
- Repeat until the tree is empty.

Return all leaf nodes in the order they were collected.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.collectLeaves(root, result)
        return result

    def collectLeaves(self, node: Optional[TreeNode], result: List[List[int]]) -> int:
        if not node:
            return -1  # Base case: null nodes are at height -1

        # Get the height of left and right subtrees
        leftHeight = self.collectLeaves(node.left, result)
        rightHeight = self.collectLeaves(node.right, result)

        # Current node's height is max of left and right heights + 1
        currentHeight = max(leftHeight, rightHeight) + 1

        # Add new list for nodes at current height if needed
        if len(result) == currentHeight:
            result.append([])

        # Add current node to its corresponding height group
        result[currentHeight].append(node.val)
        return currentHeight


def test_find_leaves():
    def create_tree(values, index=0):
        if index >= len(values) or values[index] is None:
            return None
        root = TreeNode(values[index])
        root.left = create_tree(values, 2 * index + 1)
        root.right = create_tree(values, 2 * index + 2)
        return root

    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5],  # Test case 1
        [1],              # Test case 2: Single node
        [1, 2, 3],       # Test case 3: Simple tree
    ]

    solution = Solution()
    print("Testing Find Leaves of Binary Tree:")

    for i, values in enumerate(test_cases, 1):
        root = create_tree(values)
        result = solution.findLeaves(root)
        print(f"\nTest case {i}:")
        print(f"Input tree: {values}")
        print(f"Output: {result}")


# Example usage:
if __name__ == "__main__":
    # Creating the binary tree:
    #          1
    #         / \
    #        2   3
    #       / \
    #      4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Solution instance
    solution = Solution()
    result = solution.findLeaves(root)
    print(result)  # Output: [[4, 5, 3], [2], [1]]

    test_find_leaves()
