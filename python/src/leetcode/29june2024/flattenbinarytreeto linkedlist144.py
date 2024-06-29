# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # Helper function to perform flattening
        def flatten_tree(node):
            if not node:
                return None

            # Flatten left and right subtrees
            left_tail = flatten_tree(node.left)
            right_tail = flatten_tree(node.right)

            # If there is a left subtree, we need to move it to the right
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            # We need to return the "tail" of the flattened tree
            return right_tail if right_tail else left_tail if left_tail else node

        flatten_tree(root)


# Example usage:
# Creating the binary tree: [1,2,5,3,4,null,6]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

# Flattening the tree
sol = Solution()
sol.flatten(root)

# Helper function to print the flattened tree as a list


def print_flattened_tree(root: TreeNode):
    while root:
        print(root.val, end=" -> " if root.right else "")
        root = root.right
    print()


# Print the flattened tree
print_flattened_tree(root)  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
