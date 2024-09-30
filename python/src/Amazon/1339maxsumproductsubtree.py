# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        MOD = 10**9 + 7

        # Step 1: Find the total sum of all nodes in the tree
        total_sum = 0

        def calculate_total_sum(node):
            nonlocal total_sum
            if not node:
                return 0
            left_sum = calculate_total_sum(node.left)
            right_sum = calculate_total_sum(node.right)
            total_sum = total_sum + node.val
            return node.val + left_sum + right_sum

        calculate_total_sum(root)

        # Step 2: Find the maximum product by splitting at different nodes
        max_product = 0

        def find_max_product(node):
            nonlocal max_product
            if not node:
                return 0
            left_sum = find_max_product(node.left)
            right_sum = find_max_product(node.right)

            # Current subtree sum
            subtree_sum = node.val + left_sum + right_sum

            # Compute the product of splitting the tree here
            product = subtree_sum * (total_sum - subtree_sum)
            max_product = max(max_product, product)

            return subtree_sum

        find_max_product(root)

        # Return the max product found, modulo 10**9 + 7
        return max_product % MOD

# Testing the implementation


def test_max_product():
    # Constructing the binary tree:
    #         1
    #        / \
    #       2   3
    #      /|   |\
    #     4 5   6 7

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Expected output: 110 (Splitting at the edge between node 1 and node 2)
    solution = Solution()
    result = solution.maxProduct(root)
    print(f"Maximum product of split binary tree: {result}")


# Run the test
test_max_product()
