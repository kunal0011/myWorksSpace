class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        def helper(node):
            if not node:
                return ["null"]
            # Preorder traversal
            return [str(node.val)] + helper(node.left) + helper(node.right)

        # Join the list into a string
        return ','.join(helper(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        # Split the data string into list of values
        values = data.split(',')

        def helper():
            # Get the next value
            val = values.pop(0)
            if val == "null":
                return None
            # Create a new node
            node = TreeNode(int(val))
            # Recursively construct left and right subtrees
            node.left = helper()
            node.right = helper()
            return node

        return helper()
