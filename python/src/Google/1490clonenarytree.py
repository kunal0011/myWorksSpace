# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # Create a copy of the current node
        clone_root = Node(root.val)

        # Recursively clone all the children
        for child in root.children:
            clone_root.children.append(self.cloneTree(child))

        return clone_root
