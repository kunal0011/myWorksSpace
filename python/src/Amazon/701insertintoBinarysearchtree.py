"""
LeetCode 701: Insert into a Binary Search Tree

Given the root node of a binary search tree (BST) and a value to be inserted
into the BST, insert the value into the BST. Return the root node of the BST
after the insertion. The BST is guaranteed to be unique.

Constraints:
- The number of nodes in the tree will be in the range [0, 10^4].
- -10^8 <= Node.val <= 10^8
- All the values Node.val are unique.
- -10^8 <= val <= 10^8
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # If tree is empty, create new root
        if not root:
            return TreeNode(val)
        
        # Iterative solution - more space efficient
        current = root
        while current:
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

# Helper function to print the tree in-order
def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

def test_insert_bst():
    """
    Test driver for BST insertion with various cases
    """
    sol = Solution()
    
    test_cases = [
        {
            'tree': [4,2,7,1,3],
            'val': 5,
            'expected': [1,2,3,4,5,7]
        },
        {
            'tree': [40,20,60,10,30,50,70],
            'val': 25,
            'expected': [10,20,25,30,40,50,60,70]
        },
        {
            'tree': [],
            'val': 5,
            'expected': [5]
        },
        {
            'tree': [1],
            'val': 2,
            'expected': [1,2]
        }
    ]
    
    def create_tree(values):
        if not values:
            return None
        root = TreeNode(values[0])
        for val in values[1:]:
            sol.insertIntoBST(root, val)
        return root
    
    for i, case in enumerate(test_cases, 1):
        root = create_tree(case['tree'])
        result = sol.insertIntoBST(root, case['val'])
        actual = inorder_traversal(result)
        passed = actual == case['expected']
        
        print(f"\nTest case {i}:")
        print(f"Input tree: {case['tree']}")
        print(f"Value to insert: {case['val']}")
        print(f"Expected: {case['expected']}")
        print(f"Got: {actual}")
        print(f"{'✓ Passed' if passed else '✗ Failed'}")

if __name__ == "__main__":
    test_insert_bst()
