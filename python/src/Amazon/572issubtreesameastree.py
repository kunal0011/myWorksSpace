# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # Helper function to check if two trees are identical
        def isSameTree(s: TreeNode, t: TreeNode) -> bool:
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            # Check if both left and right subtrees are the same
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        # Main function to check if subRoot is a subtree of root
        if not root:
            return False
        # If the current trees are identical, return True
        if isSameTree(root, subRoot):
            return True
        # Recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# Test cases


def test_is_subtree():
    sol = Solution()

    # Test case 1: subRoot is a subtree of root
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    assert sol.isSubtree(root, subRoot) == True  # subRoot is a subtree

    # Test case 2: subRoot is not a subtree of root
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(3)  # Different structure

    assert sol.isSubtree(root, subRoot) == False  # subRoot is not a subtree

    # Test case 3: Single node match
    root = TreeNode(1)
    subRoot = TreeNode(1)
    assert sol.isSubtree(root, subRoot) == True  # Single node matches

    # Test case 4: subRoot is a subtree at a deeper level
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)

    subRoot = TreeNode(2)
    subRoot.left = TreeNode(0)

    # subRoot is a subtree deeper in the tree
    assert sol.isSubtree(root, subRoot) == True

    print("All test cases passed!")


# Run the tests
test_is_subtree()
