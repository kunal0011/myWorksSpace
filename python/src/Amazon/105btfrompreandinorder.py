"""
LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal

Problem Statement:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
    3
   / \
  9  20
     /  \
   15    7

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values
- Each value of inorder also appears in preorder
- preorder is guaranteed to be the preorder traversal of the tree
- inorder is guaranteed to be the inorder traversal of the tree
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a hash map for quick index lookup in inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build(preorder_start: int, preorder_end: int,
                  inorder_start: int, inorder_end: int) -> Optional[TreeNode]:
            if preorder_start > preorder_end:
                return None

            # Root value is first element in preorder traversal
            root_val = preorder[preorder_start]
            root = TreeNode(root_val)

            # Find root position in inorder traversal
            inorder_root = inorder_map[root_val]

            # Calculate size of left subtree
            left_subtree_size = inorder_root - inorder_start

            # Recursively build left and right subtrees
            root.left = build(preorder_start + 1,
                              preorder_start + left_subtree_size,
                              inorder_start,
                              inorder_root - 1)

            root.right = build(preorder_start + left_subtree_size + 1,
                               preorder_end,
                               inorder_root + 1,
                               inorder_end)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

    def buildTreeIterative(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """Iterative solution using stack"""
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorder_idx = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            if stack and stack[-1].val == inorder[inorder_idx]:
                # Found a right child
                while stack and stack[-1].val == inorder[inorder_idx]:
                    current = stack.pop()
                    inorder_idx += 1
                current.right = node
            else:
                # Left child
                stack[-1].left = node
            stack.append(node)

        return root


def visualize_tree(root: TreeNode, level: int = 0, prefix: str = "Root: ") -> None:
    """Helper function to visualize binary tree"""
    if not root:
        print("  " * level + prefix + "None")
        return

    print("  " * level + prefix + str(root.val))
    if root.left or root.right:
        visualize_tree(root.left, level + 1, "L--- ")
        visualize_tree(root.right, level + 1, "R--- ")


def tree_to_list(root: TreeNode) -> List[Optional[int]]:
    """Convert binary tree to level-order list representation"""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


def test_build_tree():
    solution = Solution()

    test_cases = [
        {
            "preorder": [3, 9, 20, 15, 7],
            "inorder": [9, 3, 15, 20, 7],
            "expected": [3, 9, 20, None, None, 15, 7],
            "description": "Standard tree"
        },
        {
            "preorder": [-1],
            "inorder": [-1],
            "expected": [-1],
            "description": "Single node"
        },
        {
            "preorder": [1, 2, 3],
            "inorder": [2, 1, 3],
            "expected": [1, 2, 3],
            "description": "Small tree"
        },
        {
            "preorder": [1, 2, 4, 5, 3, 6, 7],
            "inorder": [4, 2, 5, 1, 6, 3, 7],
            "expected": [1, 2, 3, 4, 5, 6, 7],
            "description": "Complete binary tree"
        },
        {
            "preorder": [1, 2, 3, 4],
            "inorder": [1, 2, 3, 4],
            "expected": [1, None, 2, None, 3, None, 4],
            "description": "Right-skewed tree"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        preorder = test_case["preorder"]
        inorder = test_case["inorder"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Preorder: {preorder}")
        print(f"Inorder:  {inorder}")

        # Test both recursive and iterative solutions
        root_recursive = solution.buildTree(preorder, inorder)
        root_iterative = solution.buildTreeIterative(preorder, inorder)

        print("\nConstructed tree (recursive):")
        visualize_tree(root_recursive)
        print("\nConstructed tree (iterative):")
        visualize_tree(root_iterative)

        result_recursive = tree_to_list(root_recursive)
        result_iterative = tree_to_list(root_iterative)

        assert result_recursive == expected and result_iterative == expected, \
            f"Expected {expected}, but got {result_recursive} (recursive) and {result_iterative} (iterative)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_build_tree()
    print("\nAll test cases passed! 🎉")
