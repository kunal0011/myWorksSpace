# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        def preorder(node):
            if not node:
                return []
            # Preorder traversal (root -> left -> right)
            return [str(node.val)] + preorder(node.left) + preorder(node.right)

        # Join the preorder traversal list into a comma-separated string
        return ','.join(preorder(root))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        # Convert the data into a list of integers
        preorder_vals = list(map(int, data.split(',')))

        # Helper function to construct the BST
        def build_bst(min_val, max_val):
            if not preorder_vals or preorder_vals[0] < min_val or preorder_vals[0] > max_val:
                return None
            # Pop the first element as it is the root
            val = preorder_vals.pop(0)
            node = TreeNode(val)
            # All values for the left subtree should be less than `val`
            node.left = build_bst(min_val, val)
            # All values for the right subtree should be greater than `val`
            node.right = build_bst(val, max_val)
            return node

        # Rebuild the BST with initial min and max range for the whole tree
        return build_bst(float('-inf'), float('inf'))
