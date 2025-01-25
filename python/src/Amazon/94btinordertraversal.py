"""
LeetCode 94. Binary Tree Inorder Traversal

Problem Statement:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

Note: Inorder traversal visits nodes in the order: left subtree, root, right subtree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        def recursive_inorder(node: TreeNode, result: list[int]):
            if not node:
                return
            recursive_inorder(node.left, result)
            result.append(node.val)
            recursive_inorder(node.right, result)

        result = []
        recursive_inorder(root, result)
        return result

    def inorderTraversalIterative(self, root: TreeNode) -> list[int]:
        """Iterative solution using stack"""
        result = []
        stack = []
        current = root

        while current or stack:
            # Reach the leftmost node of current node
            while current:
                stack.append(current)
                current = current.left

            # Process current node and move to right subtree
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result


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


def test_inorder_traversal():
    solution = Solution()

    test_cases = [
        {
            "values": [1, None, 2, 3],
            "expected": [1, 3, 2],
            "description": "Standard case"
        },
        {
            "values": [],
            "expected": [],
            "description": "Empty tree"
        },
        {
            "values": [1],
            "expected": [1],
            "description": "Single node"
        },
        {
            "values": [1, 2, 3, 4, 5],
            "expected": [4, 2, 5, 1, 3],
            "description": "Complete binary tree"
        },
        {
            "values": [1, 2, None, 3],
            "expected": [3, 2, 1],
            "description": "Left-skewed tree"
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

        # Test recursive solution
        result_recursive = solution.inorderTraversal(root)
        print(f"\nRecursive inorder traversal: {result_recursive}")
        assert result_recursive == expected, \
            f"Recursive: Expected {expected}, but got {result_recursive}"

        # Test iterative solution
        result_iterative = solution.inorderTraversalIterative(root)
        print(f"Iterative inorder traversal: {result_iterative}")
        assert result_iterative == expected, \
            f"Iterative: Expected {expected}, but got {result_iterative}"

        print("✓ Test case passed!")


if __name__ == "__main__":
    test_inorder_traversal()
    print("\nAll test cases passed! 🎉")

# Test cases


def test_inorderTraversal():
    sol = Solution()

    # Test Case 1: Standard binary tree
    root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert sol.inorderTraversal(root1) == [1, 3, 2], "Test Case 1 Failed"

    #
