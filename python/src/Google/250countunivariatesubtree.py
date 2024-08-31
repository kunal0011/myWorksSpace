class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0

        def is_univalue(node: TreeNode) -> bool:
            if not node:
                return True

            # Check if the left and right subtrees are univalue
            left_univalue = is_univalue(node.left)
            right_univalue = is_univalue(node.right)

            # If left or right subtree is not univalue, current subtree cannot be univalue
            if not left_univalue or not right_univalue:
                return False

            # Check if current node forms a univalue subtree with its children
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False

            # If current subtree is univalue, increment count
            self.count += 1
            return True

        is_univalue(root)
        return self.count
