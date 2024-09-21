# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        # Helper function to calculate the total sum of the tree
        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        # Helper function to check the sum of subtrees
        def dfs(node):
            if not node:
                return 0
            current_sum = node.val + dfs(node.left) + dfs(node.right)
            if current_sum * 2 == total and node is not root:
                self.found = True
            return current_sum

        total = total_sum(root)
        if total % 2 != 0:  # If total sum is odd, can't split it into two equal parts
            return False

        self.found = False
        dfs(root)
        return self.found

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
    root1 = create_tree([5, 10, 10, None, None, 2, 3])
    print(sol.checkEqualTree(root1))  # Output: True

    # Test case 2
    root2 = create_tree([1, 2, 10, None, None, 2, 20])
    print(sol.checkEqualTree(root2))  # Output: False
