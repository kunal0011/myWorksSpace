"""
LeetCode 1261: Find Elements in a Contaminated Binary Tree

Problem Statement:
Given a binary tree with the following rules:
1. root.val == 0
2. If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
3. If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.
Implement the FindElements class:
- FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
- bool find(int target) Returns true if the target value exists in the recovered binary tree.

Logic:
1. Recovery (Constructor):
   - Use DFS to recover original values based on given rules
   - Store recovered values in a set for O(1) lookup
   - For node with value x:
     * left child = 2x + 1
     * right child = 2x + 2

2. Find operation:
   - Simply check if target exists in recovered values set

Time Complexity: 
- Constructor: O(n) where n is number of nodes
- find(): O(1) using set lookup
Space Complexity: O(n) for storing recovered values
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.recovered_values = set()

        def recover(node, val):
            if not node:
                return
            node.val = val
            self.recovered_values.add(val)
            recover(node.left, 2 * val + 1)
            recover(node.right, 2 * val + 2)

        recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.recovered_values


def test_find_elements():
    # Test case 1: Basic tree
    root1 = TreeNode(-1)
    root1.left = TreeNode(-1)
    root1.right = TreeNode(-1)
    root1.left.left = TreeNode(-1)

    fe1 = FindElements(root1)

    # Test various finds
    assert fe1.find(1) == True, "Test case 1.1 failed"
    assert fe1.find(3) == True, "Test case 1.2 failed"
    assert fe1.find(5) == False, "Test case 1.3 failed"
    print("Test case 1 passed: Basic tree operations")

    # Test case 2: Single node tree
    root2 = TreeNode(-1)
    fe2 = FindElements(root2)
    assert fe2.find(0) == True, "Test case 2.1 failed"
    assert fe2.find(1) == False, "Test case 2.2 failed"
    print("\nTest case 2 passed: Single node tree")

    # Test case 3: Complete binary tree
    root3 = TreeNode(-1)
    root3.left = TreeNode(-1)
    root3.right = TreeNode(-1)
    root3.left.left = TreeNode(-1)
    root3.left.right = TreeNode(-1)
    root3.right.left = TreeNode(-1)
    root3.right.right = TreeNode(-1)

    fe3 = FindElements(root3)
    assert fe3.find(2) == True, "Test case 3.1 failed"
    assert fe3.find(4) == True, "Test case 3.2 failed"
    assert fe3.find(6) == True, "Test case 3.3 failed"
    assert fe3.find(8) == False, "Test case 3.4 failed"
    print("\nTest case 3 passed: Complete binary tree")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_find_elements()
