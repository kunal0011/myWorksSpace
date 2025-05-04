"""
LeetCode 652 - Find Duplicate Subtrees

Problem Statement:
Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.

Logic:
1. Use serialization to convert each subtree into a unique string representation
2. Keep track of count of each serialized subtree using a hash map
3. When we encounter a serialized subtree for the second time, add it to result
4. Serialize each subtree in format: val(left_subtree)(right_subtree)
5. Use "#" to represent null nodes

Time Complexity: O(n), where n is the number of nodes
Space Complexity: O(n) for storing serialized strings

Key Optimizations:
1. Only add to result when count becomes exactly 2 to avoid duplicates
2. Use defaultdict to simplify counting logic
"""

from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def serialize(node):
            if not node:
                return "#"
            serial = f"{node.val}({serialize(node.left)})({serialize(node.right)})"
            count[serial] += 1
            if count[serial] == 2:
                result.append(node)
            return serial

        count = defaultdict(int)
        result = []
        serialize(root)
        return result


def build_tree(values, index=0):
    """Helper function to build tree from list"""
    if index >= len(values) or values[index] is None:
        return None

    root = TreeNode(values[index])
    root.left = build_tree(values, 2 * index + 1)
    root.right = build_tree(values, 2 * index + 2)
    return root


def get_tree_values(root):
    """Helper function to get values from tree nodes"""
    if not root:
        return None
    return root.val


def test_find_duplicate_subtrees():
    solution = Solution()

    # Test Case 1: Tree with duplicate subtrees
    values1 = [1, 2, 3, 4, None, 2, 4, None, None, 4]
    root1 = build_tree(values1)
    result1 = solution.findDuplicateSubtrees(root1)
    print("\nTest Case 1:")
    print(f"Input tree: {values1}")
    print(
        f"Duplicate subtree roots: {[get_tree_values(node) for node in result1]}")
    print(f"Expected: [4, 2]")

    # Test Case 2: Tree with no duplicates
    values2 = [1, 2, 3]
    root2 = build_tree(values2)
    result2 = solution.findDuplicateSubtrees(root2)
    print("\nTest Case 2:")
    print(f"Input tree: {values2}")
    print(
        f"Duplicate subtree roots: {[get_tree_values(node) for node in result2]}")
    print(f"Expected: []")

    # Test Case 3: Tree with multiple duplicates
    values3 = [2, 1, 1, None, None, None, None]
    root3 = build_tree(values3)
    result3 = solution.findDuplicateSubtrees(root3)
    print("\nTest Case 3:")
    print(f"Input tree: {values3}")
    print(
        f"Duplicate subtree roots: {[get_tree_values(node) for node in result3]}")
    print(f"Expected: [1]")


if __name__ == "__main__":
    test_find_duplicate_subtrees()
