# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        # Create a dictionary to store the index of each value in the inorder traversal for quick lookup
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}

        def array_to_tree(left, right):
            if left > right:
                return None

            # Select the postorder_index element as the root and decrement it
            root_value = postorder[self.postorder_index]
            root = TreeNode(root_value)

            # Root splits inorder list into left and right subtrees
            index = inorder_index_map[root_value]

            # Decrement postorder_index
            self.postorder_index -= 1

            # Build right and left subtree
            # Note that we build the right subtree first because the next element in postorder
            # is the root of the right subtree
            root.right = array_to_tree(index + 1, right)
            root.left = array_to_tree(left, index - 1)

            return root

        # Initialize the current index of postorder traversal
        self.postorder_index = len(postorder) - 1
        return array_to_tree(0, len(inorder) - 1)


# Example usage:
# Inorder and Postorder traversal lists
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

# Create a solution instance and build the tree
solution = Solution()
root = solution.buildTree(inorder, postorder)

# Function to print the tree in a readable way (level order traversal)


def print_tree(root):
    if not root:
        return "Empty Tree"
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            if node:
                current_level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                current_level.append("null")
        result.append(current_level)
    return result


# Print the constructed binary tree
print(print_tree(root))
