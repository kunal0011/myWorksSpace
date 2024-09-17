# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # If we reached a null node, return None
        if not original:
            return None
        
        # If we found the target node in the original tree, return the corresponding node in the cloned tree
        if original == target:
            return cloned
        
        # Recursively search in the left and right subtrees
        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result:
            return left_result
        
        return self.getTargetCopy(original.right, cloned.right, target)

# Example for testing:
# Create the original and cloned trees, as well as the target node (not covered here for brevity)
