"""
LeetCode 538 - Convert BST to Greater Tree

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that 
every key of the original BST is changed to the original key plus the sum of all keys 
greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Explanation:
- All numbers above 8 are null, so sum = 8
- All numbers above 7 are 8, so sum = 15
- All numbers above 6 are 7,8, so sum = 21
And so on...

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]

Example 3:
Input: root = [1,0,2]
Output: [3,3,2]

Note: This is the same as problem 1038. Binary Search Tree to Greater Sum Tree.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursive solution using reverse inorder traversal.
        Time complexity: O(n)
        Space complexity: O(h) where h is the height of the tree
        """
        def reverse_inorder(node: Optional[TreeNode], running_sum: int) -> int:
            if not node:
                return running_sum
                
            # Process right subtree first
            running_sum = reverse_inorder(node.right, running_sum)
            
            # Update current node
            node.val += running_sum
            running_sum = node.val
            
            # Process left subtree
            return reverse_inorder(node.left, running_sum)
            
        reverse_inorder(root, 0)
        return root

    def convertBST_iterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Iterative solution using a stack.
        Time complexity: O(n)
        Space complexity: O(h) where h is the height of the tree
        """
        if not root:
            return None

        stack = []
        curr = root
        running_sum = 0

        # Perform reverse inorder traversal iteratively
        while stack or curr:
            # Push all right nodes onto stack
            while curr:
                stack.append(curr)
                curr = curr.right

            curr = stack.pop()
            curr.val += running_sum
            running_sum = curr.val

            # Move to left subtree
            curr = curr.left

        return root


def create_tree(values: list, index: int = 0) -> Optional[TreeNode]:
    """Helper function to create a binary tree from a list of values"""
    if not values or index >= len(values) or values[index] is None:
        return None
        
    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)
    root.right = create_tree(values, 2 * index + 2)
    return root

def tree_to_list(root: Optional[TreeNode]) -> list:
    """Helper function to convert a binary tree to a list for comparison"""
    if not root:
        return []
        
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
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

def test_convert_bst():
    """Test function to verify both solution approaches"""
    solution = Solution()
    
    test_cases = [
        # Test case 1: Example from problem statement
        ([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8],
         [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]),
         
        # Test case 2: Simple tree
        ([0,None,1],
         [1,None,1]),
         
        # Test case 3: Basic tree
        ([1,0,2],
         [3,3,2]),
         
        # Test case 4: Empty tree
        ([], []),
         
        # Test case 5: Single node
        ([5], [5]),
         
        # Test case 6: Complete binary tree
        ([2,1,3],
         [5,6,3]),
         
        # Test case 7: Unbalanced tree
        ([5,2,13,1,3,None,None],
         [18,20,13,21,18,None,None])
    ]
    
    for i, (input_values, expected_values) in enumerate(test_cases, 1):
        # Create input tree
        root = create_tree(input_values)
        root_copy = create_tree(input_values)
        
        # Test recursive solution
        result_recursive = solution.convertBST(root)
        result_recursive_list = tree_to_list(result_recursive)
        
        # Test iterative solution
        result_iterative = solution.convertBST_iterative(root_copy)
        result_iterative_list = tree_to_list(result_iterative)
        
        recursive_correct = result_recursive_list == expected_values
        iterative_correct = result_iterative_list == expected_values
        
        print(f"\nTest {i}:")
        print(f"Input tree: {input_values}")
        print(f"Expected: {expected_values}")
        print(f"Recursive Solution: {'✓' if recursive_correct else '✗'}")
        print(f"Got: {result_recursive_list}")
        print(f"Iterative Solution: {'✓' if iterative_correct else '✗'}")
        print(f"Got: {result_iterative_list}")


if __name__ == "__main__":
    test_convert_bst()