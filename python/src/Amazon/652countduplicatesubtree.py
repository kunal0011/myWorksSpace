"""
LeetCode 652: Find Duplicate Subtrees

Problem Statement:
Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.
"""

from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Hash map to store frequency of serialized subtrees
        subtrees = defaultdict(int)
        # List to store roots of duplicate subtrees
        result = []
        
        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return "#"
            # Create unique serialization for each subtree
            serialized = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            subtrees[serialized] += 1
            # If we find a duplicate subtree, add it to result
            if subtrees[serialized] == 2:
                result.append(node)
            return serialized
        
        serialize(root)
        return result

def create_tree(values: List[int], index: int = 0) -> Optional[TreeNode]:
    """Helper function to create a binary tree from list of values"""
    if index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)
    root.right = create_tree(values, 2 * index + 2)
    return root

def test_solution():
    """Test driver with various test cases"""
    solution = Solution()
    
    # Test cases
    test_cases = [
        [1,2,3,4,None,2,4,None,None,4],  # Has duplicate subtrees
        [2,1,1],  # Has duplicate leaf nodes
        [2,2,2,3,None,3,None],  # Has duplicate subtrees with multiple nodes
        [1],  # Single node
        []  # Empty tree
    ]
    
    for i, values in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input tree values: {values}")
        
        root = create_tree(values)
        result = solution.findDuplicateSubtrees(root)
        
        print(f"Number of duplicate subtrees found: {len(result)}")
        print(f"Root values of duplicate subtrees: {[node.val for node in result]}")
        print("-" * 50)

if __name__ == "__main__":
    test_solution()
