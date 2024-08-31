# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode):
        if not root:
            return []

        stack, output = [root], []

        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                # Push right first so that left is processed first (LIFO order)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return output
