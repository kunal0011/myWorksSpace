"""
LeetCode 366 - Find Leaves of Binary Tree

Problem Statement:
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
1. Collect all the leaf nodes.
2. Remove those leaf nodes.
3. Repeat until the tree is empty.

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree for recursion stack
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: TreeNode) -> list[list[int]]:
        """
        Collects leaves level by level using bottom-up DFS approach.
        The height of a node is defined as the number of edges from the node to the deepest leaf.
        Leaves have height 0, their parents have height 1, and so on.
        
        :param root: Root of the binary tree
        :return: List of lists containing node values at each level
        """
        if not root:
            return []
        
        result = []
        
        def getHeight(node: TreeNode) -> int:
            """
            Returns the height of the node and adds its value to the appropriate level
            """
            if not node:
                return -1
            
            # Get height of left and right subtrees
            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)
            
            # Current node's height is max of left and right plus 1
            currentHeight = max(leftHeight, rightHeight) + 1
            
            # Extend result list if needed
            while len(result) <= currentHeight:
                result.append([])
                
            # Add current node's value to its level
            result[currentHeight].append(node.val)
            
            return currentHeight
        
        getHeight(root)
        return result


def test_find_leaves():
    """
    Test cases for findLeaves function
    """
    def create_tree(values: list) -> TreeNode:
        """Helper function to create a binary tree from list"""
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

    solution = Solution()
    
    # Test case 1: Example from LeetCode
    print("Running test cases...")
    tree1 = create_tree([1,2,3,4,5])
    result1 = solution.findLeaves(tree1)
    expected1 = [[4,5,3],[2],[1]]
    assert result1 == expected1, f"Test case 1 failed. Expected {expected1}, got {result1}"

    # Test case 2: Single node
    tree2 = create_tree([1])
    result2 = solution.findLeaves(tree2)
    expected2 = [[1]]
    assert result2 == expected2, f"Test case 2 failed. Expected {expected2}, got {result2}"

    # Test case 3: Empty tree
    tree3 = None
    result3 = solution.findLeaves(tree3)
    expected3 = []
    assert result3 == expected3, f"Test case 3 failed. Expected {expected3}, got {result3}"

    # Test case 4: Unbalanced tree
    tree4 = create_tree([1,2,None,3,None,4])
    result4 = solution.findLeaves(tree4)
    expected4 = [[4],[3],[2],[1]]
    assert result4 == expected4, f"Test case 4 failed. Expected {expected4}, got {result4}"

    # Test case 5: Complete binary tree
    tree5 = create_tree([1,2,3,4,5,6,7])
    result5 = solution.findLeaves(tree5)
    expected5 = [[4,5,6,7],[2,3],[1]]
    assert result5 == expected5, f"Test case 5 failed. Expected {expected5}, got {result5}"

    print("All test cases passed successfully!")


if __name__ == "__main__":
    test_find_leaves()