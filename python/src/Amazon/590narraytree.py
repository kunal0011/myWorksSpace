"""
LeetCode 590 - N-ary Tree Postorder Traversal

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal. 
Each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
        1
      / | \
     3  2  4
    / \
   5   6

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

Constraints:
- The number of nodes in the tree is in the range [0, 10^4]
- 0 <= Node.val <= 10^4
- The height of the n-ary tree is less than or equal to 1000
- The total number of nodes is at most 10^4
"""

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        Recursive solution for N-ary tree postorder traversal
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        """
        def dfs(node: 'Node', result: List[int]) -> None:
            if not node:
                return
            # First traverse all children
            for child in node.children:
                dfs(child, result)
            # Then add current node's value
            result.append(node.val)
            
        result = []
        dfs(root, result)
        return result
    
    def postorder_iterative(self, root: 'Node') -> List[int]:
        """
        Iterative solution using stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return []
            
        result = []
        stack = [(root, False)]  # (node, visited_children)
        
        while stack:
            node, visited = stack.pop()
            
            if visited:
                # If we've visited all children, add current node
                result.append(node.val)
            else:
                # Put current node back with visited flag
                stack.append((node, True))
                # Add children in reverse order (to process them in correct order)
                for child in reversed(node.children):
                    stack.append((child, False))
                    
        return result
    
    def postorder_reverse_preorder(self, root: 'Node') -> List[int]:
        """
        Alternative solution using modified preorder traversal
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return []
            
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            # Add current node at beginning (reverse of final order)
            result.insert(0, node.val)
            # Add children in normal order
            stack.extend(node.children)
            
        return result


def build_nary_tree(values: List[int]) -> 'Node':
    """Helper function to build N-ary tree from level order traversal with null markers"""
    if not values:
        return None
        
    root = Node(values[0])
    queue = [root]
    i = 2  # Skip first null marker
    
    while queue and i < len(values):
        node = queue.pop(0)
        children = []
        
        # Add all children until we hit null
        while i < len(values) and values[i] is not None:
            child = Node(values[i])
            children.append(child)
            queue.append(child)
            i += 1
        
        node.children = children
        i += 1  # Skip null marker
        
    return root


def test_nary_tree_postorder():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ([1,None,3,2,4,None,5,6], [5,6,3,2,4,1]),  # Example 1
        ([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14],
         [2,6,14,11,7,3,12,8,4,13,9,10,5,1]),  # Example 2
         
        # Edge cases
        ([1], [1]),  # Single node
        ([], []),    # Empty tree
        
        # Simple trees
        ([1,None,2,3,4], [2,3,4,1]),  # One level
        ([1,None,2,None,3], [3,2,1]),  # Linear tree
        
        # Complex cases
        ([1,None,2,3,None,4,5,6], [4,5,2,6,3,1]),
        ([1,None,2,3,4,None,5,6,None,7,8], [5,6,2,7,8,3,4,1])
    ]
    
    print("Running tests for N-ary Tree Postorder Traversal...\n")
    
    for i, (values, expected) in enumerate(test_cases, 1):
        root = build_nary_tree(values)
        
        # Test all three implementations
        result1 = solution.postorder(root)
        result2 = solution.postorder_iterative(root)
        result3 = solution.postorder_reverse_preorder(root)
        
        print(f"Test Case {i}:")
        print(f"Input tree (level order): {values}")
        print(f"Expected postorder: {expected}")
        print(f"Recursive Solution: {result1} {'✅' if result1 == expected else '❌'}")
        print(f"Iterative Solution: {result2} {'✅' if result2 == expected else '❌'}")
        print(f"Reverse Preorder: {result3} {'✅' if result3 == expected else '❌'}")
        
        if (result1 != expected or 
            result2 != expected or 
            result3 != expected):
            print("❌ Test case failed!")
            if result1 != expected:
                print(f"Recursive solution failed. Got: {result1}")
            if result2 != expected:
                print(f"Iterative solution failed. Got: {result2}")
            if result3 != expected:
                print(f"Reverse preorder failed. Got: {result3}")
        else:
            print("✅ Test case passed!")
        print()


if __name__ == "__main__":
    test_nary_tree_postorder()