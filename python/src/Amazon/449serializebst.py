"""
LeetCode 449 - Serialize and Deserialize BST

Problem Statement:
-----------------
Serialization is converting a data structure or object into a sequence of bits so that 
it can be stored in a file or memory buffer, or transmitted across a network connection 
link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree (BST). There is no 
restriction on how your serialization/deserialization algorithm should work. You need to 
ensure that a binary search tree can be serialized to a string, and this string can be 
deserialized to the original tree structure.

The encoded string should be as compact as possible.

Key Points:
----------
1. Must handle both serialization and deserialization
2. The tree is a Binary Search Tree (BST)
3. Can use BST properties for optimization
4. Should generate compact representation
5. Must handle empty trees and single nodes

Examples:
--------
Input: root = [2,1,3]
Output: [2,1,3]
Explanation: Original BST:
    2
   / \\
  1   3
After serialize and deserialize, we get the same BST

Input: root = []
Output: []
Explanation: Empty tree serializes to empty string

Constraints:
-----------
* The number of nodes in the tree is in the range [0, 10^4]
* 0 <= Node.val <= 10^4
* The input tree is guaranteed to be a binary search tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """Initialize binary tree node"""
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """
        Serialize BST to string using preorder traversal.
        Since it's a BST, we only need preorder traversal to reconstruct it.
        
        Algorithm:
        1. Use preorder traversal (root -> left -> right)
        2. Join values with comma separator
        3. Empty nodes are skipped (BST property helps in reconstruction)
        
        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(n) for the string representation
        """
        def preorder(node):
            if not node:
                return []
            return [str(node.val)] + preorder(node.left) + preorder(node.right)

        return ','.join(preorder(root))

    def deserialize(self, data: str) -> TreeNode:
        """
        Deserialize string back to BST.
        Uses BST property that left subtree values < root < right subtree values
        
        Algorithm:
        1. Convert string to list of integers
        2. Use BST property to determine left and right subtrees
        3. Recursively build tree using value range constraints
        
        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(h) where h is height of tree (recursion stack)
        """
        if not data:
            return None

        # Convert string to list of integers
        preorder_vals = list(map(int, data.split(',')))

        def build_bst(min_val, max_val):
            if not preorder_vals or preorder_vals[0] < min_val or preorder_vals[0] > max_val:
                return None
                
            val = preorder_vals.pop(0)
            node = TreeNode(val)
            node.left = build_bst(min_val, val)
            node.right = build_bst(val, max_val)
            return node

        return build_bst(float('-inf'), float('inf'))


def build_tree(values):
    """Helper function to build BST from list of values"""
    if not values:
        return None
    root = TreeNode(values[0])
    for val in values[1:]:
        current = root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                current = current.right
    return root

def tree_to_list(root):
    """Helper function to convert BST to sorted list (inorder traversal)"""
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    return inorder(root)

def test_codec():
    """
    Test driver for BST serialization/deserialization
    """
    test_cases = [
        [2, 1, 3],  # Basic BST
        [],  # Empty tree
        [5],  # Single node
        [5, 3, 7, 1, 4, 6, 8],  # Complete BST
        [10, 5, 15, 3, 7, 12, 17],  # Balanced BST
        [1, 2, 3, 4, 5],  # Right-skewed BST
        [5, 4, 3, 2, 1],  # Left-skewed BST
        [8, 3, 10, 1, 6, 14, 4, 7, 13]  # Complex BST
    ]
    
    codec = Codec()
    
    for i, values in enumerate(test_cases, 1):
        # Create original BST
        original = build_tree(values)
        
        # Serialize and then deserialize
        serialized = codec.serialize(original)
        deserialized = codec.deserialize(serialized)
        
        # Convert both trees to sorted lists for comparison
        original_list = tree_to_list(original)
        deserialized_list = tree_to_list(deserialized)
        
        # Check if the trees match
        status = "PASSED" if original_list == deserialized_list else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input values: {values}")
        print(f"Original (inorder): {original_list}")
        print(f"Serialized: {serialized}")
        print(f"Deserialized (inorder): {deserialized_list}")
        print("-" * 40)

if __name__ == "__main__":
    test_codec()
