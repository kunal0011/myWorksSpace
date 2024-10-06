class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # Step 1: Locate the node to be deleted
        if key < root.val:
            # The key to be deleted is in the left subtree
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # The key to be deleted is in the right subtree
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found: root.val == key
            # Case 1: Node has no children (leaf node) or only one child
            if not root.left:
                return root.right  # Replace with right child (could be None)
            elif not root.right:
                return root.left  # Replace with left child (could be None)

            # Case 2: Node has two children
            # Find the inorder successor (smallest node in the right subtree)
            temp = self.findMin(root.right)
            root.val = temp.val  # Replace the root's value with the successor's value
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)

        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        # Find the node with the minimum value (leftmost node in the subtree)
        while node.left:
            node = node.left
        return node
