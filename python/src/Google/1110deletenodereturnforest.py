class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        # Convert to_delete to a set for quick lookup
        to_delete_set = set(to_delete)
        forest = []

        # Helper function to perform postorder traversal and delete nodes
        def postorder(node: TreeNode, is_root: bool) -> TreeNode:
            if not node:
                return None

            # Recursively delete nodes in the left and right subtrees
            node.left = postorder(node.left, False)
            node.right = postorder(node.right, False)

            # Check if the current node needs to be deleted
            if node.val in to_delete_set:
                # If the node is to be deleted, add its children to the forest
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None  # Return None to remove this node

            # If the node is a root of the forest, add it to the result
            if is_root:
                forest.append(node)

            return node

        # Start the postorder traversal from the root
        postorder(root, True)

        return forest
