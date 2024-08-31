class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leaf_sequence(node: TreeNode):
            leaves = []

            def dfs(node):
                if not node:
                    return
                if not node.left and not node.right:
                    leaves.append(node.val)
                dfs(node.left)
                dfs(node.right)
            dfs(node)
            return leaves

        leaves1 = get_leaf_sequence(root1)
        leaves2 = get_leaf_sequence(root2)

        return leaves1 == leaves2


# Example usage
# Tree 1
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root1.right.right = TreeNode(8)

# Tree 2
root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.right = TreeNode(8)

solution = Solution()
print(solution.leafSimilar(root1, root2))  # Output: True or False
