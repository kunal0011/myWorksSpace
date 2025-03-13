"""
LeetCode 617 - Merge Two Binary Trees

You are given two binary trees root1 and root2. Imagine that when you put one of them to cover the other, 
some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into 
a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value 
of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Example 1:
Input: 
root1 = [1,3,2,5]
root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:
Input: 
root1 = [1]
root2 = [1,2]
Output: [2,2]

Constraints:
- The number of nodes in both trees is in the range [0, 2000]
- -10^4 <= Node.val <= 10^4
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Optimized recursive solution for merging two binary trees.
        
        Logic:
        1. If one of the nodes is None, return the other node
        2. Create a new node with sum of values
        3. Recursively merge left and right subtrees
        
        Time Complexity: O(min(n1, n2)) where n1, n2 are number of nodes in trees
        Space Complexity: O(min(h1, h2)) where h1, h2 are heights of trees (recursive stack)
        """
        # Base cases: if either tree is empty, return the other tree
        if not root1:
            return root2
        if not root2:
            return root1
            
        # Create new node with sum of values
        merged = TreeNode(root1.val + root2.val)
        
        # Recursively merge left and right subtrees
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        
        return merged
    
    def mergeTrees_iterative(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Alternative iterative solution using a queue.
        Useful for cases where recursion stack might be an issue.
        
        Time Complexity: O(min(n1, n2))
        Space Complexity: O(min(w1, w2)) where w1, w2 are max widths of trees
        """
        if not root1:
            return root2
        if not root2:
            return root1
            
        queue = deque([(root1, root2)])
        
        while queue:
            node1, node2 = queue.popleft()
            
            # Already merged the values during queue addition
            
            # Process left children
            if node1.left and node2.left:
                queue.append((node1.left, node2.left))
            elif node2.left:
                node1.left = node2.left
                
            # Process right children
            if node1.right and node2.right:
                queue.append((node1.right, node2.right))
            elif node2.right:
                node1.right = node2.right
                
        return root1


def create_tree(values: list) -> Optional[TreeNode]:
    """Helper function to create a binary tree from a list of values"""
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Add left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Add right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
        
    return root


def tree_to_list(root: Optional[TreeNode]) -> list:
    """Helper function to convert a binary tree to a list for testing"""
    if not root:
        return []
        
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
            
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
        
    return result


def test_merge_trees():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Example test cases
        ([1,3,2,5], [2,1,3,None,4,None,7], [3,4,5,5,4,None,7]),
        ([1], [1,2], [2,2]),
        
        # Edge cases
        ([], [1], [1]),
        ([1], [], [1]),
        ([], [], []),
        
        # Balanced trees
        ([1,2,3], [4,5,6], [5,7,9]),
        
        # Unbalanced trees
        ([1,2], [3,None,4], [4,2,4]),
        ([1,None,2], [3,4], [4,4,2]),
        
        # Trees with negative values
        ([-1,2], [3,-4], [2,-2]),
        
        # Complex cases
        ([1,2,3,4,5], [1,2,3,4,5], [2,4,6,8,10]),
        ([5,3,7,2,4,6,8], [1,2,3], [6,5,10,2,4,6,8])
    ]
    
    print("Running tests for Merge Two Binary Trees...\n")
    
    for i, (vals1, vals2, expected) in enumerate(test_cases, 1):
        # Create input trees
        root1 = create_tree(vals1)
        root2 = create_tree(vals2)
        
        # Test recursive solution
        merged_recursive = solution.mergeTrees(root1, root2)
        result_recursive = tree_to_list(merged_recursive)
        
        # Create trees again for iterative solution (since previous trees were modified)
        root1 = create_tree(vals1)
        root2 = create_tree(vals2)
        
        # Test iterative solution
        merged_iterative = solution.mergeTrees_iterative(root1, root2)
        result_iterative = tree_to_list(merged_iterative)
        
        print(f"Test Case {i}:")
        print(f"Tree 1: {vals1}")
        print(f"Tree 2: {vals2}")
        print(f"Expected: {expected}")
        print(f"Recursive Solution: {result_recursive}")
        print(f"Iterative Solution: {result_iterative}")
        
        if result_recursive == expected and result_iterative == expected:
            print("✅ Test case passed!")
        else:
            print("❌ Test case failed!")
            if result_recursive != expected:
                print(f"Recursive solution failed. Got: {result_recursive}")
            if result_iterative != expected:
                print(f"Iterative solution failed. Got: {result_iterative}")
        print()


if __name__ == "__main__":
    test_merge_trees()