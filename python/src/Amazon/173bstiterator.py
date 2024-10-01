# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        # Initialize the stack with the leftmost nodes
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        # Push all the leftmost nodes onto the stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the top node from the stack
        topmost_node = self.stack.pop()

        # If the node has a right child, add its leftmost nodes to the stack
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)

        return topmost_node.val

    def hasNext(self) -> bool:
        # If the stack is not empty, there are still elements in the BST
        return len(self.stack) > 0
