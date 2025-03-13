"""
LeetCode 669: Trim a Binary Search Tree

Problem Statement:
Given the root of a binary search tree and the lowest and highest boundaries low and high, 
trim the tree so that all its elements lies in [low, high]. 
Trimming the tree should not change the relative structure of the elements that will remain in the tree 
(i.e., any node's descendant should remain a descendant).

Key Points:
1. If a node's value is outside [low, high], we need to replace it with its appropriate child
2. If node's value < low, we should return node's right subtree
3. If node's value > high, we should return node's left subtree
4. We keep the node if its value is within range and recursively trim its children
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
            
        # If root.val < low, trim left subtree and all nodes less than low
        if root.val < low:
            return self.trimBST(root.right, low, high)
            
        # If root.val > high, trim right subtree and all nodes greater than high
        if root.val > high:
            return self.trimBST(root.left, low, high)
            
        # If root.val is within range, recursively trim both subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root

def create_tree(values):
    """Helper function to create a BST from a list of values"""
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

def tree_to_list(root):
    """Convert tree to list for easy comparison"""
    if not root:
        return []
        
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return result

def test_trim_bst():
    solution = Solution()
    
    # Test cases: [tree_values, low, high, expected_result, description]
    test_cases = [
        ([1,0,2], 1, 2, [1,2], "Basic case"),
        ([3,0,4,None,2,None,None,1], 1, 3, [3,2,1], "Complex tree"),
        ([1], 1, 2, [1], "Single node within range"),
        ([1,None,2], 2, 4, [2], "Tree with nodes outside lower bound"),
        ([3,2,4,1], 2, 3, [3,2], "Tree with nodes outside upper bound"),
        ([], 1, 2, [], "Empty tree"),
    ]
    
    for i, (values, low, high, expected, description) in enumerate(test_cases, 1):
        print(f"\nTest case {i}: {description}")
        root = create_tree(values)
        result = solution.trimBST(root, low, high)
        result_list = tree_to_list(result)
        
        assert result_list == expected, \
            f"Failed: Expected {expected}, got {result_list}"
        
        print(f"Input: values={values}, low={low}, high={high}")
        print(f"Expected: {expected}")
        print(f"Got: {result_list}")
        print("Test passed!")

if __name__ == "__main__":
    test_trim_bst()
