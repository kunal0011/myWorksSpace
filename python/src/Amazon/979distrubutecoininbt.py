"""
LeetCode 979: Distribute Coins in Binary Tree

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins.
There are n coins in total distributed across the nodes.

In one move, we may choose two adjacent nodes and move one coin from one node to another.
Return the minimum number of moves required to make every node have exactly one coin.

Constraints:
- The number of nodes in the tree is n
- 1 <= n <= 100
- 0 <= Node.val <= n
- The sum of all Node.val is n
"""

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        
        def balance(node: TreeNode) -> int:
            if not node:
                return 0
                
            left = balance(node.left)   # Get balance from left subtree
            right = balance(node.right)  # Get balance from right subtree
            
            self.moves += abs(left) + abs(right)  # Add moves needed for both subtrees
            
            return node.val + left + right - 1  # Return excess/deficit coins
            
        balance(root)
        return self.moves

def validate_tree(root: TreeNode) -> bool:
    """Validate tree according to constraints"""
    if not root:
        return False
        
    nodes = []
    total_coins = 0
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        nodes.append(node)
        total_coins += node.val
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    n = len(nodes)
    return (1 <= n <= 100 and 
            all(0 <= node.val <= n for node in nodes) and
            total_coins == n)

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

def visualize_tree(root: TreeNode) -> None:
    """Print visual representation of the tree with coin distribution"""
    if not root:
        return
        
    levels = []
    queue = deque([(root, 0)])
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node, pos = queue.popleft()
            level.append((pos, str(node.val)))
            
            if node.left:
                queue.append((node.left, pos*2))
            if node.right:
                queue.append((node.right, pos*2 + 1))
                
        levels.append(level)
    
    # Print tree
    for level in levels:
        spacing = " " * 4
        print(spacing.join(" " * pos + val for pos, val in level))

def test_distribute_coins():
    """Test function for Distribute Coins in Binary Tree"""
    test_cases = [
        ([3,0,0], 2),
        ([0,3,0], 3),
        ([1,0,2], 2),
        ([1,0,0,None,3], 4),
        ([5,0,0,None,None], 4)
    ]
    
    solution = Solution()
    
    for i, (values, expected) in enumerate(test_cases, 1):
        root = build_tree([x if x != 'null' else None for x in values])
        is_valid = validate_tree(root)
        
        print(f"\nTest case {i}:")
        print("Initial tree state:")
        visualize_tree(root)
        
        result = solution.distributeCoins(root)
        
        print(f"\nMoves required: {result}")
        print(f"Expected moves: {expected}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional statistics
        total_nodes = sum(1 for x in values if x != 'null' and x is not None)
        total_coins = sum(x for x in values if x != 'null' and x is not None)
        print(f"\nTree statistics:")
        print(f"Total nodes: {total_nodes}")
        print(f"Total coins: {total_coins}")
        print(f"Average moves per node: {result/total_nodes:.2f}")

if __name__ == "__main__":
    test_distribute_coins()
