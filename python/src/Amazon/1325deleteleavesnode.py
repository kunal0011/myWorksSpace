# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None

        # Post-order traversal: process the children first
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # If it's a leaf node with value equal to target, remove it
        if not root.left and not root.right and root.val == target:
            return None

        return root

# Testing


def tree_to_list(root):
    if not root:
        return []
    return tree_to_list(root.left) + [root.val] + tree_to_list(root.right)


root = TreeNode(1,
                TreeNode(2, TreeNode(2)),
                TreeNode(3, TreeNode(2), TreeNode(4)))

solution = Solution()
new_root = solution.removeLeafNodes(root, 2)
print("Python Test Result:", tree_to_list(new_root))  # Output: [1, 3, 4]
