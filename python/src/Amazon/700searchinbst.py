"""
LeetCode 700: Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
If such a node does not exist, return null.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Iterative solution - O(h) time, O(1) space
        # where h is the height of the tree
        current = root
        while current and current.val != val:
            if val < current.val:
                current = current.left
            else:
                current = current.right
        return current

    def searchBST_recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Recursive solution - O(h) time, O(h) space
        if not root or root.val == val:
            return root
        return self.searchBST_recursive(root.left if val < root.val else root.right, val)

def create_tree(values: list) -> Optional[TreeNode]:
    """Helper function to create a BST from list of values"""
    if not values:
        return None
    root = TreeNode(values[0])
    for val in values[1:]:
        current = root
        while True:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = TreeNode(val)
                    break
                current = current.right
    return root

def tree_to_list(root: Optional[TreeNode]) -> list:
    """Helper function to convert tree to list for testing"""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def test_search_bst():
    test_cases = [
        ([4,2,7,1,3], 2, [2,1,3]),  # Normal case
        ([4,2,7,1,3], 5, []),       # Value not found
        ([1], 1, [1]),              # Single node
        ([], 1, []),                # Empty tree
        ([4,2,7,1,3], 7, [7])       # Search for leaf node
    ]
    
    solution = Solution()
    for i, (tree_vals, search_val, expected) in enumerate(test_cases, 1):
        root = create_tree(tree_vals)
        result = tree_to_list(solution.searchBST(root, search_val))
        print(f"Test case {i}:")
        print(f"Tree: {tree_vals}")
        print(f"Search value: {search_val}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}\n")

if __name__ == "__main__":
    test_search_bst()
