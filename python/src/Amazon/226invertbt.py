"""
LeetCode 226 - Invert Binary Tree

Problem Statement:
Given the root of a binary tree, invert the tree, and return its root.
Inverting means swapping every left node with its right node at every level.

Solution Logic:
1. Use recursive approach to invert the tree
2. Base case: return None if root is None
3. Recursively invert left and right subtrees
4. Swap left and right children
5. Time: O(n) where n is number of nodes
6. Space: O(h) where h is height of tree (recursion stack)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        # Recursively invert the left and right subtrees
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)

        # Swap the left and right children
        root.left, root.right = right_inverted, left_inverted

        return root

def create_tree(values):
    """Helper function to create a binary tree from list of values."""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def tree_to_list(root):
    """Helper function to convert tree to list for printing."""
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
    while result[-1] is None:
        result.pop()
    return result

def test_invert_tree():
    solution = Solution()
    
    # Test Case 1: Perfect binary tree
    root1 = create_tree([4,2,7,1,3,6,9])
    print("Test 1: Perfect binary tree")
    print(f"Original: {tree_to_list(root1)}")
    inverted1 = solution.invertTree(root1)
    print(f"Inverted: {tree_to_list(inverted1)}")  # Expected: [4,7,2,9,6,3,1]
    
    # Test Case 2: Empty tree
    print("\nTest 2: Empty tree")
    root2 = None
    inverted2 = solution.invertTree(root2)
    print(f"Inverted: {tree_to_list(inverted2)}")  # Expected: []
    
    # Test Case 3: Single node
    print("\nTest 3: Single node")
    root3 = create_tree([1])
    inverted3 = solution.invertTree(root3)
    print(f"Inverted: {tree_to_list(inverted3)}")  # Expected: [1]

if __name__ == "__main__":
    test_invert_tree()
