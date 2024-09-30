
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # Initialize sum
        total_sum = 0

        # Define DFS function
        def dfs(node):
            nonlocal total_sum
            if node:
                # If the current node is within the range, add to sum
                if low <= node.val <= high:
                    total_sum += node.val
                # If the current node's value is greater than low, explore the left subtree
                if node.val > low:
                    dfs(node.left)
                # If the current node's value is less than high, explore the right subtree
                if node.val < high:
                    dfs(node.right)

        # Start DFS from the root
        dfs(root)
        return total_sum


# Test the solution with a test case
if __name__ == "__main__":
    # Create the tree [10,5,15,3,7,None,18]
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)

    solution = Solution()

    # Test case: range is [7, 15]
    low, high = 7, 15
    result = solution.rangeSumBST(root, low, high)
    # Expected output: 32
    print(f"Range sum between {low} and {high} is: {result}")
