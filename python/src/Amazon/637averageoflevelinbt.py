"""
LeetCode 637 - Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each level 
in the form of an array. Answers within 10^-5 of the actual answer will be accepted.

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(w) where w is the maximum width of the tree
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_nodes = list(queue)  # Current level nodes
            result.append(sum(node.val for node in level_nodes) / len(level_nodes))
            
            # Update queue with next level nodes using list comprehension
            queue = deque(
                child for node in queue 
                for child in (node.left, node.right) 
                if child
            )

        return result

def build_tree(values):
    """Helper function to build tree from list of values."""
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

# Test driver
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [3, 9, 20, None, None, 15, 7],  # Expected: [3.0, 14.5, 11.0]
        [3, 9, 20, 15, 7],  # Expected: [3.0, 14.5, 11.0]
        [1],  # Expected: [1.0]
        []  # Expected: []
    ]
    
    solution = Solution()
    for i, case in enumerate(test_cases):
        root = build_tree(case)
        result = solution.averageOfLevels(root)
        print(f"Test case {i + 1}:")
        print(f"Input: {case}")
        print(f"Output: {result}")
        print()
