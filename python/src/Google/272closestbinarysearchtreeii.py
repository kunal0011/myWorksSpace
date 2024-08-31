from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        # Get all values in sorted order
        values = inorder(root)

        # Find the closest k values using two pointers
        def find_closest(values, target, k):
            left, right = 0, len(values) - 1
            while right - left >= k:
                if abs(values[left] - target) < abs(values[right] - target):
                    right -= 1
                else:
                    left += 1
            return values[left:left + k]

        return find_closest(values, target, k)
