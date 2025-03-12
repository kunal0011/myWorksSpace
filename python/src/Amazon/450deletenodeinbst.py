"""
LeetCode 450 - Delete Node in a BST

Problem Statement:
-----------------
Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.

Key Points:
----------
1. Must maintain BST properties after deletion
2. Three cases to handle:
   - Node to delete is a leaf
   - Node has one child
   - Node has two children
3. When node has two children, replace with inorder successor
4. Must handle root node deletion
5. Return modified BST root

Examples:
--------
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7]

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Constraints:
-----------
* The number of nodes in the tree is in the range [0, 10^4]
* -10^5 <= Node.val <= 10^5
* Each node has a unique value
* root is a valid binary search tree
* -10^5 <= key <= 10^5
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """Initialize binary tree node"""
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        Delete a node with given key from BST and return new root.
        
        Algorithm:
        1. Search for node to delete using BST property
        2. If node found, handle three cases:
           - Leaf node: Simply remove it
           - One child: Replace with child
           - Two children: Replace with inorder successor
        3. Return modified root
        
        Time Complexity: O(h) where h is height of tree
        Space Complexity: O(h) for recursion stack
        """
        if not root:
            return None

        # Search phase
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found, handle deletion cases
            
            # Case 1 & 2: No child or one child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case 3: Two children
            # Find inorder successor (smallest in right subtree)
            successor = self.findMin(root.right)
            root.val = successor.val
            # Delete the successor
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        """Find node with minimum value in BST (leftmost node)"""
        while node.left:
            node = node.left
        return node


def build_bst(values):
    """Helper function to build BST from level-order traversal"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def bst_to_list(root):
    """Convert BST to level-order list representation"""
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

def test_delete_node():
    """
    Test driver for BST node deletion
    """
    test_cases = [
        (
            [5,3,6,2,4,None,7], 3,
            [5,4,6,2,None,None,7]  # Delete node with two children
        ),
        (
            [5,3,6,2,4,None,7], 0,
            [5,3,6,2,4,None,7]  # Delete non-existent node
        ),
        (
            [5], 5,
            []  # Delete root node with no children
        ),
        (
            [5,3], 5,
            [3]  # Delete root with one child
        ),
        (
            [5,3,6], 5,
            [6,3]  # Delete root with two children
        ),
        (
            [5,3,6,2,4,None,7], 6,
            [5,3,7,2,4]  # Delete node with one child
        ),
        (
            [5,3,6,2,4,None,7], 2,
            [5,3,6,None,4,None,7]  # Delete leaf node
        ),
        (
            [10,5,15,3,7,12,17], 15,
            [10,5,17,3,7,12]  # Complex case
        )
    ]
    
    solution = Solution()
    
    for i, (tree_values, key, expected) in enumerate(test_cases, 1):
        # Build input BST
        root = build_bst(tree_values)
        
        # Delete node
        result_root = solution.deleteNode(root, key)
        
        # Convert result to list for comparison
        result = bst_to_list(result_root)
        
        # Check if result matches expected
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input BST: {tree_values}")
        print(f"Key to delete: {key}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_delete_node()
