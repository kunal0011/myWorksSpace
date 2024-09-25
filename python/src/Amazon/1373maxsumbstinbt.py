class TreeNode:
    pass


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.max_sum = 0

        def traverse(node):
            # Base case: An empty node is trivially a BST with sum = 0, min = inf, max = -inf
            if not node:
                return (True, float('inf'), float('-inf'), 0)

            # Recursively check left and right subtrees
            left_is_bst, left_min, left_max, left_sum = traverse(node.left)
            right_is_bst, right_min, right_max, right_sum = traverse(
                node.right)

            # A subtree is a BST if the left and right subtrees are BSTs, and the current node's value
            # is greater than the max value in the left subtree and smaller than the min value in the right subtree
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                # This subtree is a valid BST, calculate its sum
                current_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, current_sum)

                # Return that this is a valid BST, along with its new min, max, and sum
                return (True, min(left_min, node.val), max(right_max, node.val), current_sum)
            else:
                # If it's not a valid BST, return that it's not a BST with dummy values
                return (False, 0, 0, 0)

        # Start the traversal from the root
        traverse(root)

        return self.max_sum
