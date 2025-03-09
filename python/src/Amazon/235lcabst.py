"""
LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree

Problem Statement:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes
p and q in the BST. The LCA is defined between two nodes p and q as the lowest node in T that
has both p and q as descendants.

Solution Logic:
1. Use BST properties for efficient search
2. Start from root and traverse down
3. If both values < current, go left
4. If both values > current, go right
5. If split occurs (one <= node <= other), current is LCA
6. Time: O(H), Space: O(1) where H is height of tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Start from the root node of the tree
        current = root

        while current:
            # If both p and q are greater than current node, then LCA lies in right
            if p.val > current.val and q.val > current.val:
                current = current.right
            # If both p and q are smaller than current node, then LCA lies in left
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                # We have found the split point, i.e. the LCA node.
                return current

def create_bst(values):
    """Helper function to create BST from sorted list."""
    if not values:
        return None
    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = create_bst(values[:mid])
    root.right = create_bst(values[mid+1:])
    return root

def test_lca():
    solution = Solution()
    
    # Test Case 1: Regular case
    root1 = create_bst([2,4,5,6,7,8,9])
    p1, q1 = TreeNode(4), TreeNode(8)
    result1 = solution.lowestCommonAncestor(root1, p1, q1)
    print("Test 1: Regular BST")
    print(f"LCA of {p1.val} and {q1.val}: {result1.val}")  # Expected: 6
    
    # Test Case 2: One node is ancestor
    root2 = create_bst([2,3,4,5])
    p2, q2 = TreeNode(2), TreeNode(4)
    result2 = solution.lowestCommonAncestor(root2, p2, q2)
    print("\nTest 2: One node is ancestor")
    print(f"LCA of {p2.val} and {q2.val}: {result2.val}")  # Expected: 2
    
    # Test Case 3: Same subtree
    root3 = create_bst([1,2,3,4,5,6,7])
    p3, q3 = TreeNode(2), TreeNode(3)
    result3 = solution.lowestCommonAncestor(root3, p3, q3)
    print("\nTest 3: Nodes in same subtree")
    print(f"LCA of {p3.val} and {q3.val}: {result3.val}")  # Expected: 3

if __name__ == "__main__":
    test_lca()
