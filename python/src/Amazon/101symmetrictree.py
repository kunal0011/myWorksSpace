"""
LeetCode 101. Symmetric Tree

Problem Statement:
Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true
    1
   / \
  2   2
 / \ / \
3  4 4  3

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
    1
   / \
  2   2
   \   \
   3    3

Constraints:
- The number of nodes in the tree is in the range [1, 1000]
- -100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            # If both nodes are None, they're symmetric
            if not left and not right:
                return True

            # If one node is None and the other isn't, not symmetric
            if not left or not right:
                return False

            # Check values and recursive check outer and inner pairs
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))

        return isMirror(root.left, root.right)

    def isSymmetricIterative(self, root: TreeNode) -> bool:
        """Iterative solution using queue"""
        if not root:
            return True

        from collections import deque
        queue = deque([(root.left, root.right)])

        while queue:
            left, right = queue.popleft()

            # If both nodes are None, continue
            if not left and not right:
                continue

            # If one node is None or values don't match
            if not left or not right or left.val != right.val:
                return False

            # Add outer and inner pairs
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True


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
    """Helper function to visualize binary tree with symmetry indicators"""
    if not root:
        print("  " * level + prefix + "None")
        return

    print("  " * level + prefix + str(root.val))
    if root.left or root.right:
        visualize_tree(root.left, level + 1, "L--- ")
        visualize_tree(root.right, level + 1, "R--- ")


def test_is_symmetric():
    solution = Solution()

    test_cases = [
        {
            "values": [1, 2, 2, 3, 4, 4, 3],
            "expected": True,
            "description": "Symmetric tree"
        },
        {
            "values": [1, 2, 2, None, 3, None, 3],
            "expected": False,
            "description": "Non-symmetric tree"
        },
        {
            "values": [1],
            "expected": True,
            "description": "Single node"
        },
        {
            "values": [1, 2, 2, 2, None, 2],
            "expected": False,
            "description": "Structurally asymmetric"
        },
        {
            "values": [1, 2, 2, None, 3, 3, None],
            "expected": True,
            "description": "Symmetric with missing nodes"
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

        # Test both recursive and iterative solutions
        result_recursive = solution.isSymmetric(root)
        result_iterative = solution.isSymmetricIterative(root)

        print(f"\nRecursive result: {result_recursive}")
        print(f"Iterative result: {result_iterative}")

        assert result_recursive == expected and result_iterative == expected, \
            f"Expected {expected}, but got {result_recursive} (recursive) and {result_iterative} (iterative)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_is_symmetric()
    print("\nAll test cases passed! 🎉")
