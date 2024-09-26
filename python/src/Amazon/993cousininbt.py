# Definition for a binary tree node.
from typing import Optional


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
