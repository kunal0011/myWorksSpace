# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.longest = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        # Helper function to calculate the longest path with the same value
        def dfs(node):
            if not node:
                return 0

            # Recursively call dfs for left and right children
            left_length = dfs(node.left)
            right_length = dfs(node.right)

            # Initialize path lengths through the left and right children
            left_path = right_path = 0

            # If the left child has the same value, extend the path
            if node.left and node.left.val == node.val:
                left_path = left_length + 1

            # If the right child has the same value, extend the path
            if node.right and node.right.val == node.val:
                right_path = right_length + 1

            # Update the longest path found so far
            self.longest = max(self.longest, left_path + right_path)

            # Return the longest single path going either left or right
            return max(left_path, right_path)

        # Call dfs on the root
        dfs(root)
        return self.longest

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
    root1 = create_tree([5, 4, 5, 1, 1, 5])
    print(sol.longestUnivaluePath(root1))  # Output: 2

    # Test case 2
    root2 = create_tree([1, 4, 5, 4, 4, 5])
    print(sol.longestUnivaluePath(root2))  # Output: 2
