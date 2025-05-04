"""
LeetCode 872: Leaf-Similar Trees

Problem Statement:
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Logic:
1. Use DFS to collect leaf values in left-to-right order for each tree
2. Compare the two leaf sequences
   - If sequences are equal, trees are leaf-similar
   - If sequences differ, trees are not leaf-similar
3. A leaf node is one with no left and right children

Time Complexity: O(n1 + n2) where n1, n2 are number of nodes in each tree
Space Complexity: O(h1 + h2) where h1, h2 are heights of trees for recursion stack
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leaf_sequence(node: TreeNode):
            leaves = []

            def dfs(node):
                if not node:
                    return
                if not node.left and not node.right:
                    leaves.append(node.val)
                dfs(node.left)
                dfs(node.right)
            dfs(node)
            return leaves

        leaves1 = get_leaf_sequence(root1)
        leaves2 = get_leaf_sequence(root2)

        return leaves1 == leaves2


def test_leaf_similar():
    solution = Solution()

    # Test case 1: Basic case - Leaf similar trees
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)

    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(8)

    result1 = solution.leafSimilar(root1, root2)
    print(f"Test case 1: Leaf-Similar Trees")
    print(f"Result: {result1}")
    assert result1 == True, "Test case 1 failed"

    # Test case 2: Different leaf sequences
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)

    root4 = TreeNode(1)
    root4.left = TreeNode(3)
    root4.right = TreeNode(2)

    result2 = solution.leafSimilar(root3, root4)
    print(f"\nTest case 2: Different Leaf Sequences")
    print(f"Result: {result2}")
    assert result2 == False, "Test case 2 failed"

    # Test case 3: Single node trees
    root5 = TreeNode(1)
    root6 = TreeNode(1)

    result3 = solution.leafSimilar(root5, root6)
    print(f"\nTest case 3: Single Node Trees")
    print(f"Result: {result3}")
    assert result3 == True, "Test case 3 failed"

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_leaf_similar()
