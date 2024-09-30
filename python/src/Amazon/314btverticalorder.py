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
