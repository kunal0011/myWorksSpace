"""
LeetCode 987: Vertical Order Traversal of a Binary Tree

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position (row, col), its left and right children will be at positions 
(row + 1, col - 1) and (row + 1, col + 1) respectively.

Return the vertical order traversal of the binary tree as an array of arrays of node values.
Nodes in the same row and column should be sorted in ascending order.

Constraints:
- The number of nodes in the tree is in the range [1, 1000]
- 0 <= Node.val <= 1000
- The tree will be complete and balanced
"""

from typing import List, Optional
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Map to store nodes by column and row
        nodes = defaultdict(lambda: defaultdict(list))
        
        def dfs(node: TreeNode, row: int, col: int) -> None:
            if not node:
                return
                
            # Add current node to its column and row
            nodes[col][row].append(node.val)
            
            # Process children
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        # Traverse tree and collect nodes
        dfs(root, 0, 0)
        
        # Build result with proper sorting
        result = []
        for col in sorted(nodes.keys()):
            col_nodes = []
            for row in sorted(nodes[col].keys()):
                col_nodes.extend(sorted(nodes[col][row]))
            result.append(col_nodes)
            
        return result

def build_tree(values: List[int]) -> Optional[TreeNode]:
    """Build binary tree from level-order traversal"""
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

def visualize_vertical_order(root: TreeNode, result: List[List[int]]) -> None:
    """Create visual representation of vertical traversal"""
    if not root:
        return
        
    # Find dimensions for visualization
    min_col = -(len(result) // 2)
    max_col = min_col + len(result) - 1
    
    print("\nVertical traversal visualization:")
    print(f"Columns from {min_col} to {max_col}")
    
    for i, column in enumerate(result):
        col_num = min_col + i
        print(f"\nColumn {col_num}:")
        print(" ".join(map(str, column)))

def test_vertical_traversal():
    """Test function for Vertical Order Traversal"""
    test_cases = [
        ([3,9,20,None,None,15,7], [[9],[3,15],[20],[7]]),
        ([1], [[1]]),
        ([1,2,3,4,5,6,7], [[4],[2],[1,5,6],[3],[7]]),
        ([1,2,3,4,6,5,7], [[4],[2],[1,6,5],[3],[7]]),
        ([3,1,4,0,2,2], [[0],[1],[3,2],[4],[2]])
    ]
    
    solution = Solution()
    
    for i, (values, expected) in enumerate(test_cases, 1):
        root = build_tree(values)
        result = solution.verticalTraversal(root)
        
        print(f"\nTest case {i}:")
        print(f"Input values: {values}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        visualize_vertical_order(root, result)
        
        # Additional statistics
        total_nodes = sum(len(col) for col in result)
        print(f"\nStatistics:")
        print(f"Number of columns: {len(result)}")
        print(f"Total nodes: {total_nodes}")
        print(f"Nodes per column: {[len(col) for col in result]}")

if __name__ == "__main__":
    test_vertical_traversal()
