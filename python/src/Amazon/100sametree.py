"""
LeetCode 100. Same Tree

Problem Statement:
Given the roots of two binary trees p and q, write a function to check if they are the same tree.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
- The number of nodes in both trees is in the range [0, 100]
- -10^4 <= Node.val <= 10^4
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # If both nodes are None, trees are same
        if not p and not q:
            return True

        # If one node is None and other isn't, trees are different
        if not p or not q:
            return False

        # Check current nodes and recursively check children
        return (p.val == q.val and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))

    def isSameTreeIterative(self, p: TreeNode, q: TreeNode) -> bool:
        """Iterative solution using queue"""
        from collections import deque
        queue = deque([(p, q)])

        while queue:
            node1, node2 = queue.popleft()

            # If both nodes are None, continue
            if not node1 and not node2:
                continue

            # If one node is None or values are different
            if not node1 or not node2 or node1.val != node2.val:
                return False

            # Add children to queue
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))

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
    """Helper function to visualize binary tree"""
    if not root:
        print("  " * level + prefix + "None")
        return

    print("  " * level + prefix + str(root.val))
    if root.left or root.right:
        visualize_tree(root.left, level + 1, "L--- ")
        visualize_tree(root.right, level + 1, "R--- ")


def test_is_same_tree():
    solution = Solution()

    test_cases = [
        {
            "p": [1, 2, 3],
            "q": [1, 2, 3],
            "expected": True,
            "description": "Identical trees"
        },
        {
            "p": [1, 2],
            "q": [1, None, 2],
            "expected": False,
            "description": "Different structure"
        },
        {
            "p": [1, 2, 1],
            "q": [1, 1, 2],
            "expected": False,
            "description": "Different values"
        },
        {
            "p": [],
            "q": [],
            "expected": True,
            "description": "Empty trees"
        },
        {
            "p": [1],
            "q": [1],
            "expected": True,
            "description": "Single node trees"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        p_values = test_case["p"]
        q_values = test_case["q"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        p = create_binary_tree(p_values)
        q = create_binary_tree(q_values)

        print("\nTree p:")
        visualize_tree(p)
        print("\nTree q:")
        visualize_tree(q)

        # Test both recursive and iterative solutions
        result_recursive = solution.isSameTree(p, q)
        result_iterative = solution.isSameTreeIterative(p, q)

        print(f"\nRecursive result: {result_recursive}")
        print(f"Iterative result: {result_iterative}")

        assert result_recursive == expected and result_iterative == expected, \
            f"Expected {expected}, but got {result_recursive} (recursive) and {result_iterative} (iterative)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_is_same_tree()
    print("\nAll test cases passed! 🎉")
