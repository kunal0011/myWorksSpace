"""
LeetCode 230 - Kth Smallest Element in a BST

Problem Statement:
Given the root of a binary search tree, and an integer k, return the kth smallest value
(1-indexed) of all the values of the nodes in the tree.

Solution Logic:
1. Use inorder traversal (gives nodes in ascending order in BST)
2. Keep track of nodes visited using k as counter
3. When k reaches 0, we found our target node
4. Time: O(H + k) where H is tree height
5. Space: O(H) due to recursion stack
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.result = None
        self.inorder(root)
        return self.result

    def inorder(self, node):
        if not node or self.result is not None:
            return

        # Visit left subtree
        self.inorder(node.left)

        # Visit current node
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return

        # Visit right subtree
        self.inorder(node.right)

def create_bst(values):
    """Helper function to create BST from sorted list."""
    if not values:
        return None
    
    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = create_bst(values[:mid])
    root.right = create_bst(values[mid + 1:])
    return root

def test_kth_smallest():
    solution = Solution()
    
    # Test Case 1: Regular BST
    root1 = create_bst([1,2,3,4,5,6,7])
    k1 = 3
    print("Test 1: Regular BST")
    print(f"k = {k1}")
    print(f"Kth smallest: {solution.kthSmallest(root1, k1)}")  # Expected: 3
    
    # Test Case 2: Small tree
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    k2 = 2
    print("\nTest 2: Small tree")
    print(f"k = {k2}")
    print(f"Kth smallest: {solution.kthSmallest(root2, k2)}")  # Expected: 2
    
    # Test Case 3: Unbalanced tree
    root3 = create_bst([1,2,3,4,5])
    k3 = 1
    print("\nTest 3: First smallest")
    print(f"k = {k3}")
    print(f"Kth smallest: {solution.kthSmallest(root3, k3)}")  # Expected: 1

if __name__ == "__main__":
    test_kth_smallest()
