from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode):
        if not root:
            return []

        result = []
        queue = deque([root])  # Initialize the queue with the root

        while queue:
            level_length = len(queue)
            level_sum = 0

            for _ in range(level_length):
                node = queue.popleft()
                level_sum += node.val

                # Add the children of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate the average for this level
            level_avg = level_sum / level_length
            result.append(level_avg)

        return result
