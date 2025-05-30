from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if root is None:
                return
            nonlocal prev, first, second
            dfs(root.left)
            if prev and prev.val > root.val:
                if first is None:
                    first = prev
                second = root
            prev = root
            dfs(root.right)

        prev = first = second = None
        dfs(root)
        first.val, second.val = second.val, first.val


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)

# Recover the BST
s = Solution()
s.recoverTree(root)
