# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        # Initialize variables to track the nodes to be swapped
        self.first = self.second = self.prev = None

        # Inorder traversal to identify the swapped nodes
        def inorder(node):
            if not node:
                return

            # Traverse the left subtree
            inorder(node.left)

            # Find the first and second nodes that are out of order
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev  # First incorrect node
                self.second = node  # Second incorrect node

            # Update prev node
            self.prev = node

            # Traverse the right subtree
            inorder(node.right)

        # Perform inorder traversal to find the two swapped nodes
        inorder(root)

        # Swap the values of the two incorrect nodes
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
