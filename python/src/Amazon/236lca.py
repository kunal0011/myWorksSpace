"""
LeetCode 236 - Lowest Common Ancestor of a Binary Tree

Problem Statement:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
The lowest common ancestor is defined between two nodes p and q as the lowest node in T that
has both p and q as descendants (where we allow a node to be a descendant of itself).

Solution Logic:
1. Use recursive DFS approach
2. Base cases:
   - Root is None or root is p or q
3. Recursive step:
   - Search left and right subtrees
   - If both subtrees return non-None, current node is LCA
   - Otherwise, return the non-None value
4. Time: O(n), Space: O(h) where h is height
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: if the tree is empty or we've found one of the nodes
        if root is None or root == p or root == q:
            return root

        # Search for LCA in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-None, p and q are found in different subtrees
        if left and right:
            return root

        # Otherwise, return the non-None value
        return left if left else right

def create_tree(values, index=0):
    """Helper function to create binary tree."""
    if not values or index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)
    root.right = create_tree(values, 2 * index + 2)
    return root

def test_lca():
    solution = Solution()
    
    # Test Case 1: Regular case
    tree1 = create_tree([3,5,1,6,2,0,8,None,None,7,4])
    p1, q1 = TreeNode(5), TreeNode(1)
    result1 = solution.lowestCommonAncestor(tree1, p1, q1)
    print("Test 1: Regular case")
    print(f"LCA of {p1.val} and {q1.val}: {result1.val}")  # Expected: 3
    
    # Test Case 2: One node is ancestor
    tree2 = create_tree([3,5,1,6,2])
    p2, q2 = TreeNode(3), TreeNode(5)
    result2 = solution.lowestCommonAncestor(tree2, p2, q2)
    print("\nTest 2: One node is ancestor")
    print(f"LCA of {p2.val} and {q2.val}: {result2.val}")  # Expected: 3
    
    # Test Case 3: Nodes in same subtree
    tree3 = create_tree([3,5,1,6,2,0,8])
    p3, q3 = TreeNode(6), TreeNode(2)
    result3 = solution.lowestCommonAncestor(tree3, p3, q3)
    print("\nTest 3: Nodes in same subtree")
    print(f"LCA of {p3.val} and {q3.val}: {result3.val}")  # Expected: 5

if __name__ == "__main__":
    test_lca()
