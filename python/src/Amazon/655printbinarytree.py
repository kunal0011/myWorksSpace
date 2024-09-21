# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        # Helper function to calculate the height of the tree
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        # Get the height of the tree
        height = get_height(root)
        # Calculate the width of the grid (2^height - 1)
        width = (1 << height) - 1

        # Initialize the result grid with empty strings
        res = [["" for _ in range(width)] for _ in range(height)]

        # Helper function to fill the grid
        def fill(node, r, c, level_width):
            if not node:
                return
            # Place the node's value in the correct position
            res[r][c] = str(node.val)
            # Recursively place the left and right children
            if node.left:
                fill(node.left, r + 1, c - level_width // 2, level_width // 2)
            if node.right:
                fill(node.right, r + 1, c + level_width // 2, level_width // 2)

        # Start filling the grid from the root
        fill(root, 0, (width - 1) // 2, (width - 1) // 2 + 1)

        return res

# Helper function to create a binary tree from a list


def create_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        curr = queue.pop(0)
        if nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
    return root


# Test the function
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    root1 = create_tree([1, 2, 3, None, 4])
    print(sol.printTree(root1))
    # Output:
    # [["", "", "", "1", "", "", ""],
    #  ["", "2", "", "", "", "3", ""],
    #  ["", "", "4", "", "", "", ""]]

    # Test case 2
    root2 = create_tree([1, 2])
    print(sol.printTree(root2))
    # Output:
    # [["", "1", ""],
    #  ["2", "", ""]]
