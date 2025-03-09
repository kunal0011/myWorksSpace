"""
LeetCode 222 - Count Complete Tree Nodes

Problem Statement:
Given the root of a complete binary tree, return the number of nodes.
A complete binary tree is a binary tree in which every level, except possibly the last, 
is completely filled, and all nodes in the last level are as far left as possible.

Solution Logic:
1. Use binary tree properties:
   - Perfect binary tree has 2^h - 1 nodes where h is height
   - Complete tree has perfect subtrees
2. For each subtree:
   - If left height equals right height, it's perfect (2^h - 1 nodes)
   - Otherwise, recursively count left and right subtrees
3. Time: O(log^2 n), Space: O(log n)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        left_height = get_height(root.left)
        right_height = get_height(root.right)

        if left_height == right_height:
            # Left subtree is perfect, move to the right subtree
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is perfect, move to the left subtree
            return (1 << right_height) + self.countNodes(root.left)


def create_complete_tree(values: list) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values):
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def test_count_nodes():
    solution = Solution()
    
    # Test Case 1: Perfect binary tree
    tree1 = create_complete_tree([1,2,3,4,5,6,7])
    print("Test 1: Perfect binary tree")
    print(f"Node count: {solution.countNodes(tree1)}")  # Expected: 7
    
    # Test Case 2: Complete but not perfect
    tree2 = create_complete_tree([1,2,3,4,5,6])
    print("\nTest 2: Complete but not perfect tree")
    print(f"Node count: {solution.countNodes(tree2)}")  # Expected: 6
    
    # Test Case 3: Empty tree
    print("\nTest 3: Empty tree")
    print(f"Node count: {solution.countNodes(None)}")  # Expected: 0
    
    # Test Case 4: Single node
    tree4 = create_complete_tree([1])
    print("\nTest 4: Single node tree")
    print(f"Node count: {solution.countNodes(tree4)}")  # Expected: 1

if __name__ == "__main__":
    test_count_nodes()
