# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Initialize two pointers to p and q
        a, b = p, q

        # Traverse upwards to find the common ancestor
        while a != b:
            # If a is None, switch to q; otherwise, move to the parent of a
            a = a.parent if a else q
            # If b is None, switch to p; otherwise, move to the parent of b
            b = b.parent if b else p

        # When a == b, we have found the LCA
        return a
