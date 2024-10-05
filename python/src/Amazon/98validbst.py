# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # iterative
    def isValidBST(self, root: TreeNode) -> bool:
        # store (node, lower, upper) tuples in a single queue
        queue = [(root, None, None)]

        # another option:
        # queue = [(root, -math.inf, math.inf)]

        while queue:
            node, lower, upper = queue.pop(0)

            if node is None:
                continue

            val = node.val
            if lower is not None and val <= lower:
                return False
            if upper is not None and val >= upper:
                return False

            queue.append((node.right, val, upper))
            queue.append((node.left, lower, val))

        return True
