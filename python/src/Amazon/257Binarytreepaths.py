"""
LeetCode 257 - Binary Tree Paths

Problem Statement:
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children. The paths should be returned as strings where
nodes are connected with arrows "->".

Solution Logic:
1. Use DFS with path tracking
2. For each node:
   - Add current value to path
   - If leaf node, add complete path to result
   - Else recurse on children with updated path
3. Time: O(N), Space: O(H) for recursion stack
   where N = nodes, H = height of tree
"""

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


def create_tree(values):
    """Helper function to create binary tree."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def test_binary_tree_paths():
    solution = Solution()
    
    # Test Case 1: Regular binary tree
    root1 = create_tree([1,2,3,None,5])
    print("Test 1: Regular binary tree")
    print(f"Paths: {solution.binaryTreePaths(root1)}")  # Expected: ["1->2->5", "1->3"]
    
    # Test Case 2: Single node
    root2 = create_tree([1])
    print("\nTest 2: Single node")
    print(f"Paths: {solution.binaryTreePaths(root2)}")  # Expected: ["1"]
    
    # Test Case 3: Empty tree
    root3 = None
    print("\nTest 3: Empty tree")
    print(f"Paths: {solution.binaryTreePaths(root3)}")  # Expected: []
    
    # Test Case 4: Complete binary tree
    root4 = create_tree([1,2,3,4,5,6,7])
    print("\nTest 4: Complete binary tree")
    print(f"Paths: {solution.binaryTreePaths(root4)}")
    # Expected: ["1->2->4", "1->2->5", "1->3->6", "1->3->7"]

if __name__ == "__main__":
    test_binary_tree_paths()
