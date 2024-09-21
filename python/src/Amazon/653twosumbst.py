# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # Helper function for in-order traversal
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        # Get the in-order traversal of the BST
        nums = inorder(root)

        # Use two-pointer technique to find if two numbers sum to k
        l, r = 0, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total == k:
                return True
            elif total < k:
                l += 1
            else:
                r -= 1
        return False

# Helper function to create a binary search tree from a list


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
    root1 = create_tree([5, 3, 6, 2, 4, None, 7])
    print(sol.findTarget(root1, 9))  # Output: True

    # Test case 2
    root2 = create_tree([5, 3, 6, 2, 4, None, 7])
    print(sol.findTarget(root2, 28))  # Output: False
