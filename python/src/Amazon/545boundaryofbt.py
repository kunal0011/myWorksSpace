# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode):
        if not root:
            return []

        def isLeaf(node):
            return not node.left and not node.right

        def addLeftBoundary(node):
            while node:
                if not isLeaf(node):
                    boundary.append(node.val)
                node = node.left if node.left else node.right

        def addLeaves(node):
            if isLeaf(node):
                boundary.append(node.val)
                return
            if node.left:
                addLeaves(node.left)
            if node.right:
                addLeaves(node.right)

        def addRightBoundary(node):
            stack = []
            while node:
                if not isLeaf(node):
                    stack.append(node.val)
                node = node.right if node.right else node.left
            while stack:
                boundary.append(stack.pop())

        # Start with root (only if it's not a leaf)
        boundary = [root.val] if not isLeaf(root) else []

        # Add left boundary (excluding root and leaves)
        if root.left:
            addLeftBoundary(root.left)

        # Add leaves
        addLeaves(root)

        # Add right boundary (excluding root and leaves)
        if root.right:
            addRightBoundary(root.right)

        return boundary

# Test cases


def test_boundary_of_binary_tree():
    solution = Solution()

    # Test case 1: Tree with all parts of the boundary
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   5   6
    #    / \
    #   7   8
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(6)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(8)
    expected_result_1 = [1, 2, 4, 7, 8, 6, 3]
    assert solution.boundaryOfBinaryTree(
        root1) == expected_result_1, "Test case 1 failed"

    # Test case 2: Tree with only root node
    root2 = TreeNode(1)
    expected_result_2 = [1]
    assert solution.boundaryOfBinaryTree(
        root2) == expected_result_2, "Test case 2 failed"

    print("All test cases passed!")


# Run the tests
test_boundary_of_binary_tree()
