"""
LeetCode 543 - Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: The longest path is [4,2,5] or [4,2,1,3] with length 3.

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
- The number of nodes in the tree is in the range [1, 10^4]
- -100 <= Node.val <= 100
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Optimized solution using a single DFS traversal
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        """
        self.diameter = 0
        
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
                
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update diameter if path through current node is longer
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return height of current subtree
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter


def build_tree(values: list, index: int = 0) -> Optional[TreeNode]:
    """Helper function to build binary tree from list representation"""
    if not values or index >= len(values) or values[index] is None:
        return None
        
    root = TreeNode(values[index])
    root.left = build_tree(values, 2 * index + 1)
    root.right = build_tree(values, 2 * index + 2)
    return root


def test_diameter_of_binary_tree():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ([1,2,3,4,5], 3),  # Example 1
        ([1,2], 1),        # Example 2
        ([1], 0),          # Single node
        
        # Complex test cases
        ([1,2,3,4,5,None,None,8,9], 4),  # Longer path on left side
        ([1,2,3,None,4,5,6], 3),         # Balanced tree
        ([1,2,None,3,None,4,None], 3),   # Linear tree (like linked list)
        
        # Edge cases
        ([1,2,3,4,None,None,5], 3),      # Unbalanced tree
        ([1,None,2,None,3,None,4], 3),   # Right-skewed tree
        ([1,2,None,3,None,4,None], 3),   # Left-skewed tree
    ]
    
    for i, (values, expected) in enumerate(test_cases, 1):
        root = build_tree(values)
        result = solution.diameterOfBinaryTree(root)
        status = "✓" if result == expected else "✗"
        
        print(f"\nTest Case {i}: {status}")
        print(f"Input tree: {values}")
        print(f"Expected diameter: {expected}")
        print(f"Got diameter: {result}")
        
        if result != expected:
            print("❌ Test case failed!")
        else:
            print("✅ Test case passed!")
    

if __name__ == "__main__":
    test_diameter_of_binary_tree()