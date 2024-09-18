# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.running_sum = 0

        # Reverse in-order traversal to accumulate the sum
        def reverse_inorder(node):
            if not node:
                return

            # Traverse the right subtree first
            reverse_inorder(node.right)

            # Update the current node's value
            self.running_sum += node.val
            node.val = self.running_sum

            # Traverse the left subtree
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root


# Helper function to print the tree in level order


def print_tree_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Removing trailing nulls for better readability
    while result and result[-1] is None:
        result.pop()
    return result


# Testing
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

solution = Solution()
new_root = solution.bstToGst(root)
# Output: [30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8]
print("Python Test Result:", print_tree_level_order(new_root))
