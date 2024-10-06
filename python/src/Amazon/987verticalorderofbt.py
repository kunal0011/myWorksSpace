from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> list[list[int]]:
        if not root:
            return []

        # Dictionary to hold nodes by column and (level, value)
        nodes = defaultdict(list)

        # BFS queue: stores tuples of (node, column, level)
        queue = deque([(root, 0, 0)])

        while queue:
            node, col, level = queue.popleft()

            # Append the node's value with its level for sorting later
            nodes[col].append((level, node.val))

            # Add left and right children with updated column and level
            if node.left:
                queue.append((node.left, col - 1, level + 1))
            if node.right:
                queue.append((node.right, col + 1, level + 1))

        # Sort by column first, then by level, and then by value
        result = []
        for col in sorted(nodes.keys()):
            # Sort first by level, then by value
            result.append([val for level, val in sorted(nodes[col])])

        return result
