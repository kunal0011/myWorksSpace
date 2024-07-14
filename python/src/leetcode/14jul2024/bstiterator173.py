# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        # Push all the leftmost nodes onto the stack
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()
        # If the node has a right child, push all the leftmost nodes of the right child onto the stack
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        # If the stack is not empty, there are still nodes to process
        return len(self.stack) > 0


# Example usage:
# Construct a binary search tree
#       7
#      / \
#     3   15
#        /  \
#       9   20
root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))

# Initialize the iterator
iterator = BSTIterator(root)

# Iterate over the BST
print(iterator.next())    # Output: 3
print(iterator.next())    # Output: 7
print(iterator.hasNext())  # Output: True
print(iterator.next())    # Output: 9
print(iterator.hasNext())  # Output: True
print(iterator.next())    # Output: 15
print(iterator.hasNext())  # Output: True
print(iterator.next())    # Output: 20
print(iterator.hasNext())  # Output: False
