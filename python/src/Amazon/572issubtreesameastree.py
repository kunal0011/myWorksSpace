"""
LeetCode 572 - Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with 
the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree 'tree' is a tree that consists of a node in tree and all of this node's descendants. 
The tree 'tree' could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Explanation: The tree with root node value 4 from the main tree is identical to the subRoot.

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
Explanation: Although the subRoot appears in the main tree, the structure is different at node 2.

Constraints:
- The number of nodes in the root tree is in the range [1, 2000]
- The number of nodes in the subRoot tree is in the range [1, 1000]
- -10^4 <= root.val <= 10^4
- -10^4 <= subRoot.val <= 10^4
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Optimized solution using recursive traversal
        Time Complexity: O(m*n) where m and n are the number of nodes in root and subRoot
        Space Complexity: O(h) where h is the height of the root tree (recursion stack)
        """
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Helper function to check if two trees are identical"""
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
    
    def isSubtree_serialization(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Alternative solution using tree serialization
        Time Complexity: O(m + n) where m and n are the number of nodes in root and subRoot
        Space Complexity: O(m + n) for storing the serialized strings
        """
        def serialize(node: Optional[TreeNode]) -> str:
            """Convert tree to string representation with special markers for null nodes"""
            if not node:
                return "#"
            return f"^{node.val}{serialize(node.left)}{serialize(node.right)}"
        
        return serialize(subRoot) in serialize(root)


def build_tree(values: list, index: int = 0) -> Optional[TreeNode]:
    """Helper function to build a binary tree from list representation"""
    if not values or index >= len(values) or values[index] is None:
        return None
        
    root = TreeNode(values[index])
    root.left = build_tree(values, 2 * index + 1)
    root.right = build_tree(values, 2 * index + 2)
    return root


def test_is_subtree():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ([3,4,5,1,2], [4,1,2], True),
        ([3,4,5,1,2,None,None,None,None,0], [4,1,2], False),
        
        # Edge cases
        ([1], [1], True),
        ([1,1], [1], True),
        ([1], [2], False),
        
        # More complex test cases
        ([3,4,5,1,2,None,None,0], [4,1,2], False),
        ([3,4,5,1,None,2], [3,1,2], False),
        ([1,2,3], [2], True),
        ([1,2,3,4], [2,4], True),
        
        # Identical structure but different values
        ([1,2,3], [1,2,3], True),
        ([1,2,3], [1,2,4], False),
        
        # Larger trees
        ([10,5,15,3,7,None,18], [5,3,7], True),
        ([10,5,15,3,7,None,18], [5,3,8], False)
    ]
    
    print("Running tests for Subtree of Another Tree...\n")
    
    for i, (root_vals, subroot_vals, expected) in enumerate(test_cases, 1):
        root = build_tree(root_vals)
        subRoot = build_tree(subroot_vals)
        
        # Test both implementations
        result1 = solution.isSubtree(root, subRoot)
        result2 = solution.isSubtree_serialization(root, subRoot)
        
        print(f"Test Case {i}:")
        print(f"Root: {root_vals}")
        print(f"SubRoot: {subroot_vals}")
        print(f"Expected: {expected}")
        print(f"Recursive Solution: {result1} {'✅' if result1 == expected else '❌'}")
        print(f"Serialization Solution: {result2} {'✅' if result2 == expected else '❌'}")
        
        if result1 != expected or result2 != expected:
            print("❌ Test case failed!")
            if result1 != expected:
                print(f"Recursive solution failed")
            if result2 != expected:
                print(f"Serialization solution failed")
        else:
            print("✅ Test case passed!")
        print()


if __name__ == "__main__":
    test_is_subtree()