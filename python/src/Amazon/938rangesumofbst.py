"""
LeetCode 938: Range Sum of BST

Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].

Constraints:
- The number of nodes in the tree is in the range [1, 2 * 10^4]
- 1 <= Node.val <= 10^5
- 1 <= low <= high <= 10^5
- All Node.val are unique
"""

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
            
        # If current node is less than low, only explore right subtree
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
            
        # If current node is greater than high, only explore left subtree
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
            
        # Current node is in range, include it and explore both subtrees
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

def validate_input(root: Optional[TreeNode], low: int, high: int) -> bool:
    """Validate input according to constraints"""
    if not root:
        return False
        
    def count_nodes(node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)
    
    node_count = count_nodes(root)
    if not 1 <= node_count <= 2 * 10**4:
        return False
        
    values = set()
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if not 1 <= node.val <= 10**5:
            return False
        if node.val in values:
            return False
        values.add(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return 1 <= low <= high <= 10**5

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build binary tree from level-order traversal list"""
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def test_range_sum_bst():
    """Test function for Range Sum of BST"""
    test_cases = [
        ([10,5,15,3,7,None,18], 7, 15, 32),
        ([10,5,15,3,7,13,18,1,None,6], 6, 10, 23),
        ([18], 6, 10, 0),
        ([10,5,15], 7, 15, 25),
        ([10,5,15,3,7,13,18,1,None,6,None,None,20], 1, 20, 98)
    ]
    
    solution = Solution()
    
    for i, (values, low, high, expected) in enumerate(test_cases, 1):
        root = build_tree(values)
        is_valid = validate_input(root, low, high)
        result = solution.rangeSumBST(root, low, high)
        
        print(f"\nTest case {i}:")
        print(f"Tree values: {values}")
        print(f"Range: [{low}, {high}]")
        print(f"Expected sum: {expected}")
        print(f"Actual sum: {result}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Count nodes in range
        def count_in_range(node: TreeNode) -> int:
            if not node:
                return 0
            count = 1 if low <= node.val <= high else 0
            return count + count_in_range(node.left) + count_in_range(node.right)
            
        nodes_in_range = count_in_range(root)
        print(f"\nStatistics:")
        print(f"Nodes in range: {nodes_in_range}")
        if nodes_in_range > 0:
            print(f"Average value in range: {result/nodes_in_range:.2f}")

if __name__ == "__main__":
    test_range_sum_bst()
