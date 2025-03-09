"""
LeetCode 314 - Binary Tree Vertical Order Traversal

Problem Statement:
Given the root of a binary tree, return the vertical order traversal of its nodes' values.
For each node at position (row, col), its left child is at (row + 1, col - 1) and its 
right child is at (row + 1, col + 1). The root is at (0, 0).
Return the nodes organized by their columns from leftmost to rightmost.

Logic:
1. Use BFS with column tracking:
   - Each node stores (node, column) in queue
   - Left child: column-1, Right child: column+1
2. Use defaultdict to store nodes by column
3. Track min and max columns for final ordering
4. Time: O(n), Space: O(n)
"""

from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        # Dictionary to hold the column values
        column_table = defaultdict(list)
        # Queue for BFS with (node, column index)
        queue = deque([(root, 0)])  # Start with the root at column index 0
        min_col, max_col = 0, 0  # To track the range of column indices

        while queue:
            node, col = queue.popleft()
            if node is not None:
                # Add the node value to the corresponding column index
                column_table[col].append(node.val)
                # Update the min and max column indices
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                # Push left and right children to the queue with updated column index
                queue.append((node.left, col - 1))  # Left child is in col - 1
                # Right child is in col + 1
                queue.append((node.right, col + 1))

        # Extract the columns in order from min_col to max_col
        return [column_table[col] for col in range(min_col, max_col + 1)]


def test_vertical_order():
    solution = Solution()
    
    def create_tree(values):
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
    
    # Test cases
    test_cases = [
        {
            'input': [3,9,20,None,None,15,7],
            'expected': [[9],[3,15],[20],[7]]  # Standard case
        },
        {
            'input': [3,9,8,4,0,1,7],
            'expected': [[4],[9],[3,0,1],[8],[7]]  # Multiple levels
        },
        {
            'input': [1],
            'expected': [[1]]  # Single node
        },
        {
            'input': [],
            'expected': []  # Empty tree
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        root = create_tree(test_case['input'])
        result = solution.verticalOrder(root)
        assert result == test_case['expected'], \
            f"Test case {i + 1} failed: expected {test_case['expected']}, got {result}"
        print(f"Test case {i + 1} passed:")
        print(f"Input: {test_case['input']}")
        print(f"Output: {result}\n")

if __name__ == "__main__":
    test_vertical_order()
    print("All test cases passed!")
