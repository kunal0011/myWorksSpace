class Solution:
    def twoSumBSTs(self, root1, root2, target):
        # Helper function to do inorder traversal and return the set of values
        def inorder(node):
            if not node:
                return set()
            return inorder(node.left) | {node.val} | inorder(node.right)

        # Get the set of values from the first BST
        values_in_root1 = inorder(root1)

        # Helper function to check if there's a complement in the set
        def find(node):
            if not node:
                return False
            if (target - node.val) in values_in_root1:
                return True
            return find(node.left) or find(node.right)

        # Traverse the second BST and check for complement
        return find(root2)
