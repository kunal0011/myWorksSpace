"""
LeetCode 993: Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth but have different parents.
Return true if and only if the two nodes x and y are cousins.

Constraints:
- The number of nodes in the tree will be between [2, 100]
- Each node has a unique value in range [1, 100]
- x != y
- x and y exist in the tree
"""

from typing import Optional, List, Tuple
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # Edge case: if the root is None or root itself is x or y
        if not root or root.val == x or root.val == y:
            return False

        # Initialize a queue for BFS
        queue = [(root, None, 0)]  # (node, parent, depth)

        x_info = y_info = None  # To store the parent and depth of x and y

        # BFS traversal
        while queue:
            node, parent, depth = queue.pop(0)

            if node.val == x:
                x_info = (parent, depth)
            elif node.val == y:
                y_info = (parent, depth)

            # If both x and y are found, break early
            if x_info and y_info:
                break

            # Add left and right children to the queue
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))

        # Both nodes should have same depth but different parents
        if x_info and y_info:
            return x_info[1] == y_info[1] and x_info[0] != y_info[0]

        return False

def validate_tree(root: TreeNode, x: int, y: int) -> bool:
    """Validate tree according to constraints"""
    if not root:
        return False
        
    values = set()
    nodes = 0
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        nodes += 1
        values.add(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return (2 <= nodes <= 100 and
            1 <= x <= 100 and
            1 <= y <= 100 and
            x != y and
            x in values and
            y in values)

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

def print_tree(root: TreeNode) -> None:
    """Print visual representation of the tree"""
    if not root:
        return
        
    levels = []
    queue = deque([(root, 0, 0)])
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node, pos, depth = queue.popleft()
            level.append((pos, str(node.val)))
            
            if node.left:
                queue.append((node.left, pos*2, depth+1))
            if node.right:
                queue.append((node.right, pos*2+1, depth+1))
                
        levels.append(level)
        
    # Print tree
    for level in levels:
        spacing = " " * 4
        print(spacing.join(" " * pos + val for pos, val in level))

def test_cousins():
    """Test function for Cousins in Binary Tree"""
    test_cases = [
        ([1,2,3,4], 4, 3, False),
        ([1,2,3,None,4,None,5], 5, 4, True),
        ([1,2,3,None,4], 2, 3, False),
        ([1,2,3,4,5,6,7], 4, 6, True),
        ([1,2,3,None,None,4,5], 4, 5, True)
    ]
    
    solution = Solution()
    
    for i, (values, x, y, expected) in enumerate(test_cases, 1):
        root = build_tree(values)
        is_valid = validate_tree(root, x, y)
        result = solution.isCousins(root, x, y)
        
        print(f"\nTest case {i}:")
        print(f"Tree structure:")
        print_tree(root)
        print(f"Checking if {x} and {y} are cousins")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Find nodes info
        queue = deque([(root, None, 0)])
        x_info = y_info = None
        
        while queue:
            node, parent, depth = queue.popleft()
            if node.val == x:
                x_info = (parent.val if parent else None, depth)
            elif node.val == y:
                y_info = (parent.val if parent else None, depth)
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))
                
        if x_info and y_info:
            print(f"\nNode {x}: parent={x_info[0]}, depth={x_info[1]}")
            print(f"Node {y}: parent={y_info[0]}, depth={y_info[1]}")

if __name__ == "__main__":
    test_cousins()
