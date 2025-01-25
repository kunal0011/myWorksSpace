"""
LeetCode 99. Recover Binary Search Tree

Problem Statement:
You are given the root of a binary search tree (BST), where the values of exactly two nodes
of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 will restore the BST property.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 will restore the BST property.

Constraints:
- The number of nodes in the tree is in the range [2, 1000]
- -2^31 <= Node.val <= 2^31 - 1

Follow up: Can you devise a constant space solution?
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Modifies the tree in-place to recover the BST property
        Uses Morris Traversal for O(1) space complexity
        """
        # Initialize pointers for the two swapped nodes and previous node
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        def morris_traversal(root: TreeNode) -> None:
            current = root

            while current:
                if not current.left:
                    # Process current node
                    self.check_nodes(current)
                    current = current.right
                else:
                    # Find the inorder predecessor
                    predecessor = current.left
                    while predecessor.right and predecessor.right != current:
                        predecessor = predecessor.right

                    if not predecessor.right:
                        # Create thread
                        predecessor.right = current
                        current = current.left
                    else:
                        # Remove thread and process current node
                        predecessor.right = None
                        self.check_nodes(current)
                        current = current.right

        def check_nodes(node: TreeNode) -> None:
            """Helper function to identify swapped nodes"""
            if self.prev.val >= node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node

        self.check_nodes = check_nodes
        morris_traversal(root)

        # Swap the values of the two nodes
        self.first.val, self.second.val = self.second.val, self.first.val


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


def tree_to_list(root: TreeNode) -> list:
    """Helper function to convert binary tree to list"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
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


def is_valid_bst(root: TreeNode) -> bool:
    """Helper function to check if tree is a valid BST"""
    def validate(node: TreeNode, min_val: float, max_val: float) -> bool:
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return validate(node.left, min_val, node.val) and \
            validate(node.right, node.val, max_val)

    return validate(root, float('-inf'), float('inf'))


def test_recover_tree():
    solution = Solution()

    test_cases = [
        {
            "values": [1, 3, None, None, 2],
            "description": "Simple case with left subtree violation"
        },
        {
            "values": [3, 1, 4, None, None, 2],
            "description": "Case with right subtree violation"
        },
        {
            "values": [2, 3, 1],
            "description": "Complete tree with swapped nodes"
        },
        {
            "values": [4, 2, 6, 1, 3, 5, 7],
            "description": "Balanced tree with swapped nodes"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        values = test_case["values"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        root = create_binary_tree(values)

        print("\nBefore recovery:")
        visualize_tree(root)
        print("Is valid BST:", is_valid_bst(root))

        solution.recoverTree(root)

        print("\nAfter recovery:")
        visualize_tree(root)

        # Verify the tree is now a valid BST
        assert is_valid_bst(root), "Tree is not a valid BST after recovery"
        print("✓ Test case passed! Tree is now a valid BST")


if __name__ == "__main__":
    test_recover_tree()
    print("\nAll test cases passed! 🎉")
