"""
LeetCode 545 - Boundary of Binary Tree

The boundary of a binary tree is the concatenation of the root, the left boundary, 
the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:
- The root node's left child is in the left boundary
- If M is in the left boundary, then M's left child is in the left boundary
- If M is in the left boundary and M has no left child but has a right child, 
  then M's right child is in the left boundary
- The leftmost leaf is not in the left boundary

The right boundary is similar (just replace "left" with "right").
The leaves are nodes that do not have any children.

Example 1:
Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
Output: [1,2,4,7,8,9,10,6,3]

Example 2:
Input: root = [1]
Output: [1]

Constraints:
- The number of nodes in the tree is in the range [1, 10^4]
- -1000 <= Node.val <= 1000
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        # Handle single node case
        if not root.left and not root.right:
            return [root.val]
            
        def is_leaf(node: TreeNode) -> bool:
            return node and not node.left and not node.right
            
        def left_boundary(node: TreeNode) -> List[int]:
            result = []
            curr = node.left
            
            while curr:
                if not is_leaf(curr):
                    result.append(curr.val)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
                    
            return result
            
        def leaves(node: TreeNode) -> List[int]:
            result = []
            
            def dfs(node: TreeNode):
                if not node:
                    return
                if is_leaf(node):
                    result.append(node.val)
                    return
                dfs(node.left)
                dfs(node.right)
                
            dfs(node)
            return result
            
        def right_boundary(node: TreeNode) -> List[int]:
            result = []
            curr = node.right
            
            while curr:
                if not is_leaf(curr):
                    result.append(curr.val)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
                    
            return result[::-1]  # Reverse the right boundary
        
        # Combine all parts
        boundary = [root.val]
        boundary.extend(left_boundary(root))
        boundary.extend(leaves(root))
        boundary.extend(right_boundary(root))
        
        return boundary


def build_tree(values: list, index: int = 0) -> Optional[TreeNode]:
    """Helper function to build binary tree from list representation"""
    if not values or index >= len(values) or values[index] is None:
        return None
        
    root = TreeNode(values[index])
    root.left = build_tree(values, 2 * index + 1)
    root.right = build_tree(values, 2 * index + 2)
    return root


def test_boundary_of_binary_tree():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ([1,2,3,4,5,6,None,None,None,7,8,9,10],
         [1,2,4,7,8,9,10,6,3]),  # Example 1
         
        ([1], [1]),  # Single node
        
        # Complex test cases
        ([1,2,3,4,5,6,7], 
         [1,2,4,5,6,7,3]),  # Perfect binary tree
         
        ([1,None,2,None,3,None,4],
         [1,2,3,4]),  # Right-skewed tree
         
        ([1,2,None,3,None,4,None],
         [1,2,3,4]),  # Left-skewed tree
         
        ([1,2,3,4,None,None,5],
         [1,2,4,5,3]),  # Tree with specific boundary pattern
         
        # Edge cases
        ([1,2,3],
         [1,2,3]),  # Simple three-node tree
         
        ([1,None,2],
         [1,2]),  # Two nodes
    ]
    
    for i, (values, expected) in enumerate(test_cases, 1):
        root = build_tree(values)
        result = solution.boundaryOfBinaryTree(root)
        status = "✓" if result == expected else "✗"
        
        print(f"\nTest Case {i}: {status}")
        print(f"Input tree: {values}")
        print(f"Expected boundary: {expected}")
        print(f"Got boundary: {result}")
        
        if result != expected:
            print("❌ Test case failed!")
        else:
            print("✅ Test case passed!")


if __name__ == "__main__":
    test_boundary_of_binary_tree()