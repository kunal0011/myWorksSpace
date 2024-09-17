# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # Helper function to match the linked list with the path in the tree
        def dfs(head, root):
            if not head:  # If we have matched all nodes in the linked list
                return True
            if not root:  # If we reach a leaf node in the tree and haven't finished the list
                return False
            if root.val != head.val:  # If current node values don't match
                return False
            # Recursively check left and right subtrees
            return dfs(head.next, root.left) or dfs(head.next, root.right)

        # Main function to traverse the tree
        if not root:
            return False
        # Check if the current tree node starts a matching path, or search in the left or right subtree
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


# Example testing:
# Linked list: 4 -> 2 -> 8
head = ListNode(4, ListNode(2, ListNode(8)))

# Binary tree:
#       1
#      / \
#     4   4
#    /   / \
#   2   2   5
#  /   / \
# 1   6   8
root = TreeNode(1)
root.left = TreeNode(4, TreeNode(2, TreeNode(1)), None)
root.right = TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8)), TreeNode(5))

solution = Solution()
print("Python Test Result:", solution.isSubPath(head, root))  # Output: True
