from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, path):
            if node:
                # Append the current node's value to the path
                path += str(node.val)
                # If it's a leaf node, add the path to the result list
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    # Otherwise, continue the search on left and right children
                    path += '->'
                    dfs(node.left, path)
                    dfs(node.right, path)

        paths = []
        dfs(root, '')
        return paths
