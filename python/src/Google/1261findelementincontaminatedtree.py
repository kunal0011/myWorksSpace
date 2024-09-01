from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.recovered_values = set()

        def recover(node, val):
            if not node:
                return
            node.val = val
            self.recovered_values.add(val)
            recover(node.left, 2 * val + 1)
            recover(node.right, 2 * val + 2)

        recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.recovered_values
