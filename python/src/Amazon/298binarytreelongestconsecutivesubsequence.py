"""
LeetCode 298 - Binary Tree Longest Consecutive Sequence

Problem Statement:
Given the root of a binary tree, find the length of the longest consecutive sequence path.
A consecutive sequence path is a path where the values increase by one along the path.
Note that the path can start at any node in the binary tree.

Logic:
1. Use DFS with additional parameters:
   - parent: to check if current node continues sequence
   - length: current length of consecutive sequence
2. For each node:
   - If node continues sequence from parent, increment length
   - Otherwise reset length to 1
3. Return maximum of:
   - Current length
   - Result from left subtree
   - Result from right subtree
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        
        def dfs(node: Optional[TreeNode], prev_val: int, current_length: int) -> None:
            if not node:
                return
            
            # If consecutive sequence continues
            if prev_val is not None and node.val == prev_val + 1:
                current_length += 1
            else:
                current_length = 1
                
            # Update max_length if current_length is larger
            self.max_length = max(self.max_length, current_length)
            
            # Continue DFS on both children
            dfs(node.left, node.val, current_length)
            dfs(node.right, node.val, current_length)
        
        dfs(root, None, 0)
        return self.max_length

def test_longest_consecutive():
    def create_tree(values):
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

    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1,None,3,2,4,None,None,None,5], 3),  # Example with path 3-4-5
        ([2,1], 1),                            # No consecutive sequence
        ([1], 1),                              # Single node
        ([1,2,3], 2),                          # Path from root to child
        ([], 0),                               # Empty tree
        ([1,2,None,3,None,4], 4)              # Long consecutive path
    ]
    
    for i, (values, expected) in enumerate(test_cases):
        root = create_tree(values)
        result = solution.longestConsecutive(root)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: values={values}, longest consecutive sequence={result}")

if __name__ == "__main__":
    test_longest_consecutive()
    print("All test cases passed!")
