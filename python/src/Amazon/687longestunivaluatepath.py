"""
LeetCode 687: Longest Univalue Path

Problem Statement:
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value.
This path may or may not pass through the root.
The length of the path between two nodes is represented by the number of edges between them.

Example:
Input: root = [5,4,5,1,1,5]
Output: 2
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Get lengths from left and right subtrees
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            
            # Initialize current left and right paths
            left_path = right_path = 0
            
            # If left child exists and has same value
            if node.left and node.left.val == node.val:
                left_path = left_length + 1
                
            # If right child exists and has same value
            if node.right and node.right.val == node.val:
                right_path = right_length + 1
            
            # Update maximum length considering both paths
            self.max_length = max(self.max_length, left_path + right_path)
            
            # Return maximum path that can be extended
            return max(left_path, right_path)
        
        dfs(root)
        return self.max_length
        
def create_tree(values: list, index: int = 0) -> Optional[TreeNode]:
    """Helper function to create a tree from list of values."""
    if not values or index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)
    root.right = create_tree(values, 2 * index + 2)
    return root

def test_longest_univalue_path():
    solution = Solution()
    
    test_cases = [
        (
            [5,4,5,1,1,5],
            2,
            "Basic case with path through siblings"
        ),
        (
            [1,4,5,4,4,5],
            2,
            "Path in left subtree"
        ),
        (
            [1],
            0,
            "Single node"
        ),
        (
            [1,1,1,1,1,1,1],
            4,
            "All nodes same value"
        ),
        (
            None,
            0,
            "Empty tree"
        ),
        (
            [5,5,5,1,5,5,5],
            4,
            "Complex path with multiple possibilities"
        )
    ]
    
    for i, (tree_values, expected, description) in enumerate(test_cases, 1):
        root = create_tree(tree_values) if tree_values is not None else None
        result = solution.longestUnivaluePath(root)
        assert result == expected, \
            f"Test {i} failed: Expected {expected}, got {result}"
        print(f"\nTest {i}: {description}")
        print(f"Tree values: {tree_values}")
        print(f"Expected length: {expected}")
        print(f"Result: {result}")
        print("-" * 50)

if __name__ == "__main__":
    test_longest_univalue_path()
