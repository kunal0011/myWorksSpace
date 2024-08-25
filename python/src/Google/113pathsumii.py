from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, current_path, current_sum):
            if not node:
                return

            # Add the current node's value to the path and sum
            current_path.append(node.val)
            current_sum += node.val

            # Check if we are at a leaf node and if the path sum equals targetSum
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(current_path))
            else:
                # Continue the search on the left and right children
                dfs(node.left, current_path, current_sum)
                dfs(node.right, current_path, current_sum)

            # Backtrack: remove the current node from the path
            current_path.pop()

        result = []
        dfs(root, [], 0)
        return result
