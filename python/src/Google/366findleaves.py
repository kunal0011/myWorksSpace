from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.collectLeaves(root, result)
        return result

    def collectLeaves(self, node: Optional[TreeNode], result: List[List[int]]) -> int:
        if not node:
            return -1  # Base case: null nodes are at height -1

        leftHeight = self.collectLeaves(node.left, result)
        rightHeight = self.collectLeaves(node.right, result)
        currentHeight = max(leftHeight, rightHeight) + 1

        # Ensure the result list has enough lists to store nodes at 'currentHeight'
        if len(result) == currentHeight:
            result.append([])

        result[currentHeight].append(node.val)
        return currentHeight


# Example usage:
if __name__ == "__main__":
    # Creating the binary tree:
    #          1
    #         / \
    #        2   3
    #       / \
    #      4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Solution instance
    solution = Solution()
    result = solution.findLeaves(root)
    print(result)  # Output: [[4, 5, 3], [2], [1]]
