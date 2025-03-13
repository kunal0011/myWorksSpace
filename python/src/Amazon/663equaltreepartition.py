"""
LeetCode 663: Equal Tree Partition

Problem Statement:
Given the root of a binary tree, return true if you can partition the tree into two trees with equal sums 
of values after removing just one edge on the original tree.

Key points:
1. We need to find if there exists a way to split the tree into two non-empty trees with equal sums
2. We can only remove one edge
3. Both resulting trees must be valid binary trees
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        # Store all subtree sums except root
        sums = set()
        
        def get_sum(node: TreeNode) -> int:
            if not node:
                return 0
                
            curr_sum = node.val + get_sum(node.left) + get_sum(node.right)
            
            # Only add to set if not root to handle case when total sum is 0
            if node != root:
                sums.add(curr_sum)
                
            return curr_sum
        
        total = get_sum(root)
        # Tree can be partitioned if total sum is even and half of it exists in sums
        return total % 2 == 0 and (total // 2) in sums

def create_tree(values):
    """Helper function to create a binary tree from a list of values"""
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

def test_equal_tree_partition():
    solution = Solution()
    
    # Test cases: [values, expected_result, description]
    test_cases = [
        ([5, 10, 10, None, None, 2, 3], True, "Basic case with equal partition"),
        ([1, 2, 10, None, None, 2, 20], False, "Cannot be partitioned equally"),
        ([0, -1, 1], False, "Zero sum tree"),
        ([1], False, "Single node"),
        ([1, 1], True, "Two equal nodes"),
        ([10, 5, 5], True, "Three nodes with equal partition"),
        ([4, 2, 6, 1, 3, 5, 7], False, "Complete binary tree"),
        ([], False, "Empty tree"),
    ]
    
    for i, (values, expected, description) in enumerate(test_cases, 1):
        root = create_tree(values)
        result = solution.checkEqualTree(root)
        assert result == expected, f"Test case {i} failed: {description}"
        print(f"Test case {i} passed: {description}")
        print(f"Input: {values}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 50)

if __name__ == "__main__":
    test_equal_tree_partition()
