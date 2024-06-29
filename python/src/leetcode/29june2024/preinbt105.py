# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        # Create a dictionary to store the index of each value in the inorder traversal for quick lookup
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}

        def array_to_tree(left, right):
            if left > right:
                return None

            # Select the preorder_index element as the root and increment it
            root_value = preorder[self.preorder_index]
            root = TreeNode(root_value)

            # Root splits inorder list into left and right subtrees
            index = inorder_index_map[root_value]

            # Increment preorder_index
            self.preorder_index += 1

            # Build left and right subtree
            # Exclude inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, index - 1)
            root.right = array_to_tree(index + 1, right)

            return root

        # Initialize the current index of preorder traversal
        self.preorder_index = 0
        return array_to_tree(0, len(inorder) - 1)


# Example usage:
# Preorder and Inorder traversal lists
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

# Create a solution instance and build the tree
solution = Solution()
root = solution.buildTree(preorder, inorder)

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
