"""
LeetCode 662: Maximum Width of Binary Tree

Problem Statement:
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), 
where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level 
are also counted into the length calculation.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # Queue will store tuples of (node, level, position)
        queue = [(root, 0, 0)]  # (node, level, position)
        max_width = 0
        cur_level = 0
        start_index = 0
        
        while queue:
            node, level, index = queue.pop(0)
            
            # If we are starting a new level
            if level > cur_level:
                cur_level = level
                start_index = index
            
            # Calculate current position relative to start of level
            # This prevents integer overflow for deep trees
            current_width = index - start_index + 1
            max_width = max(max_width, current_width)
            
            # Append children to the queue with the updated index
            pos = index - start_index  # Relative position
            if node.left:
                queue.append((node.left, level + 1, pos * 2))
            if node.right:
                queue.append((node.right, level + 1, pos * 2 + 1))
                
        return max_width

def create_tree(values) -> TreeNode:
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

def test_width_of_binary_tree():
    solution = Solution()
    
    # Test cases as [values, expected_width]
    test_cases = [
        ([1,3,2,5,3,None,9], 4),
        ([1,3,2,5], 2),
        ([1,3,None,5,3], 2),
        ([1], 1),
        ([1,1,1,1,1,1,1,None,None,None,1,None,None,None,None,2,2,2,2], 8),
    ]
    
    for i, (values, expected) in enumerate(test_cases, 1):
        root = create_tree(values)
        result = solution.widthOfBinaryTree(root)
        assert result == expected, f"Test case {i} failed: got {result}, expected {expected}"
        print(f"Test case {i} passed! Width: {result}")
    
    print("All tests passed!")

if __name__ == "__main__":
    test_width_of_binary_tree()
