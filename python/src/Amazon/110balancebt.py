# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_height(node: TreeNode):
            if not node:
                return 0  # A null node has height 0

            left_height = check_height(node.left)
            if left_height == -1:
                return -1  # Left subtree is not balanced

            right_height = check_height(node.right)
            if right_height == -1:
                return -1  # Right subtree is not balanced

            if abs(left_height - right_height) > 1:
                return -1  # Current node is not balanced

            # Return the height of the current subtree
            return max(left_height, right_height) + 1

        # If check_height returns -1, the tree is not balanced
        return check_height(root) != -1

# Helper function to build a binary tree from a list


def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


# Test case
if __name__ == "__main__":
    # Example: A balanced tree [3, 9, 20, None, None, 15, 7]
    tree_values = [3, 9, 20, None, None, 15, 7]
    root = build_tree(tree_values)

    solution = Solution()
    result = solution.isBalanced(root)

    print(f"Is the tree balanced? {result}")
