"""
LeetCode 114. Flatten Binary Tree to Linked List

Problem Statement:
Given the root of a binary tree, flatten it to a linked list in-place.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
    1          1
   / \          \
  2   5    =>    2
 / \   \          \
3   4   6          3
                    \
                     4
                      \
                       5
                        \
                         6

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
- The number of nodes in the tree is in the range [0, 2000]
- -100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Recursive solution with O(1) extra space using Morris Traversal
        Modifies the tree in-place
        """
        current = root
        while current:
            if current.left:
                # Find the rightmost node in the left subtree
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right

                # Make current's right subtree the right child of predecessor
                predecessor.right = current.right
                # Make current's left subtree the right child of current
                current.right = current.left
                # Set left child to None
                current.left = None

            # Move to next node
            current = current.right

    def flattenRecursive(self, root: Optional[TreeNode]) -> None:
        """
        Alternative recursive solution using preorder traversal
        Uses O(h) space for recursion stack
        """
        def preorder(node: TreeNode) -> TreeNode:
            if not node:
                return None

            # Save references to left and right subtrees
            left_subtree = node.left
            right_subtree = node.right

            # Set left to None and make right point to flattened left subtree
            node.left = None
            if left_subtree:
                node.right = left_subtree
                # Get the tail of the flattened left subtree
                tail = preorder(left_subtree)
                # Connect the flattened right subtree to the tail
                tail.right = right_subtree
            else:
                node.right = right_subtree

            # Return the tail of the entire flattened tree
            if right_subtree:
                return preorder(right_subtree)
            return node

        preorder(root)

    def flattenIterative(self, root: Optional[TreeNode]) -> None:
        """
        Alternative iterative solution using stack
        Uses O(h) extra space
        """
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            current = stack.pop()

            # Add right child first (so it's processed after left)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            # Connect previous node to current
            if prev:
                prev.right = current
                prev.left = None

            prev = current


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


def visualize_flattened_tree(root: TreeNode) -> None:
    """Helper function to visualize flattened tree as a linked list"""
    if not root:
        print("Empty tree")
        return

    current = root
    path = []
    while current:
        path.append(str(current.val))
        if current.left:
            path.append("(warning: left child exists)")
        current = current.right

    print(" -> ".join(path))


def is_valid_flattened_tree(root: TreeNode) -> bool:
    """Check if tree is properly flattened"""
    current = root
    while current:
        if current.left:
            return False
        current = current.right
    return True


def test_flatten_binary_tree():
    solution = Solution()

    test_cases = [
        {
            "values": [1, 2, 5, 3, 4, None, 6],
            "description": "Standard case"
        },
        {
            "values": [],
            "description": "Empty tree"
        },
        {
            "values": [0],
            "description": "Single node"
        },
        {
            "values": [1, 2, 3],
            "description": "Simple tree"
        },
        {
            "values": [1, 2, None, 3],
            "description": "Left-skewed tree"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        values = test_case["values"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Input values: {values}")

        # Test all three approaches
        for method in ["Morris", "Recursive", "Iterative"]:
            # Create a new tree for each method
            root = create_binary_tree(values)

            print(f"\n{method} approach:")
            print("Before flattening:")
            print("Level-order traversal:", tree_to_list(root))

            # Apply the appropriate flattening method
            if method == "Morris":
                solution.flatten(root)
            elif method == "Recursive":
                solution.flattenRecursive(root)
            else:  # Iterative
                solution.flattenIterative(root)

            print("After flattening:")
            print("Level-order traversal:", tree_to_list(root))
            print("Flattened structure:")
            visualize_flattened_tree(root)

            # Verify the tree is properly flattened
            assert is_valid_flattened_tree(root), \
                f"{method} approach: Tree is not properly flattened"

        print("✓ Test case passed!")


if __name__ == "__main__":
    test_flatten_binary_tree()
    print("\nAll test cases passed! 🎉")
