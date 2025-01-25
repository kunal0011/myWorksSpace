"""
LeetCode 98. Validate Binary Search Tree

Problem Statement:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true
    2
   / \
  1   3

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
    5
   / \
  1   4
     / \
    3   6
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4]
- -2^31 <= Node.val <= 2^31 - 1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node: TreeNode, min_val: float, max_val: float) -> bool:
            if not node:
                return True

            # Check if current node's value is within valid range
            if node.val <= min_val or node.val >= max_val:
                return False

            # Recursively validate left and right subtrees
            return validate(node.left, min_val, node.val) and \
                validate(node.right, node.val, max_val)

        return validate(root, float('-inf'), float('inf'))

    def isValidBST_inorder(self, root: TreeNode) -> bool:
        """Alternative solution using inorder traversal"""
        def inorder(node: TreeNode) -> bool:
            if not node:
                return True

            if not inorder(node.left):
                return False

            if node.val <= self.prev:
                return False
            self.prev = node.val

            return inorder(node.right)

        self.prev = float('-inf')
        return inorder(root)


def create_binary_tree(values: list) -> TreeNode:
    """Helper function to create binary tree from list of values"""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

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
    """Helper function to visualize binary tree"""
    if not root:
        return

    print("  " * level + prefix + str(root.val))
    if root.left or root.right:
        if root.left:
            visualize_tree(root.left, level + 1, "L--- ")
        if root.right:
            visualize_tree(root.right, level + 1, "R--- ")


def test_is_valid_bst():
    solution = Solution()

    test_cases = [
        {
            "values": [2, 1, 3],
            "expected": True,
            "description": "Valid BST"
        },
        {
            "values": [5, 1, 4, None, None, 3, 6],
            "expected": False,
            "description": "Invalid BST - right subtree"
        },
        {
            "values": [1],
            "expected": True,
            "description": "Single node"
        },
        {
            "values": [5, 4, 6, None, None, 3, 7],
            "expected": False,
            "description": "Invalid BST - violates BST property"
        },
        {
            "values": [3, 1, 5, 0, 2, 4, 6],
            "expected": True,
            "description": "Complete valid BST"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        values = test_case["values"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        root = create_binary_tree(values)

        print("\nTree structure:")
        visualize_tree(root)

        # Test both methods
        result1 = solution.isValidBST(root)
        result2 = solution.isValidBST_inorder(root)

        print(f"\nRange-based validation result: {result1}")
        print(f"Inorder traversal validation result: {result2}")

        assert result1 == expected and result2 == expected, \
            f"Expected {expected}, but got {result1} (range-based) and {result2} (inorder)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_is_valid_bst()
    print("\nAll test cases passed! 🎉")
