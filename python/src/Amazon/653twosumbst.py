"""
LeetCode 653: Two Sum IV - Input is a BST

Problem Statement:
Given the root of a Binary Search Tree and a target number k, 
return true if there exist two elements in the BST such that their sum is equal to the given target.
"""

from typing import Optional, Set
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Using set to store visited values
        seen = set()
        
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
                
            # Check if we can find k - node.val in seen values
            complement = k - node.val
            if complement in seen:
                return True
                
            # Add current value to seen set
            seen.add(node.val)
            
            # Check left and right subtrees
            return dfs(node.left) or dfs(node.right)
            
        return dfs(root)
    
    def findTarget_iterative(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
            
        seen = set()
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            complement = k - node.val
            
            if complement in seen:
                return True
                
            seen.add(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return False

def create_bst(values: list, index: int = 0) -> Optional[TreeNode]:
    """Helper function to create BST from list"""
    if index >= len(values) or values[index] is None:
        return None
        
    root = TreeNode(values[index])
    root.left = create_bst(values, 2 * index + 1)
    root.right = create_bst(values, 2 * index + 2)
    return root

def test_solution():
    """Test driver with various test cases"""
    solution = Solution()
    
    # Test cases: [tree_values, target, expected_result]
    test_cases = [
        [[5,3,6,2,4,None,7], 9, True],  # Has pair (2,7)
        [[5,3,6,2,4,None,7], 28, False], # No pair exists
        [[2,1,3], 4, True],              # Has pair (1,3)
        [[1], 2, False],                 # Single node
        [], 1, False]                     # Empty tree
    
    for i, (values, target, expected) in enumerate(test_cases, 1):
        root = create_bst(values)
        
        # Test recursive solution
        result_recursive = solution.findTarget(root, target)
        # Test iterative solution
        result_iterative = solution.findTarget_iterative(root, target)
        
        print(f"\nTest Case {i}:")
        print(f"Tree values: {values}")
        print(f"Target sum: {target}")
        print(f"Expected: {expected}")
        print(f"Recursive solution: {result_recursive}")
        print(f"Iterative solution: {result_iterative}")
        print(f"{'✓' if result_recursive == result_iterative == expected else '✗'}")
        print("-" * 50)

if __name__ == "__main__":
    test_solution()
