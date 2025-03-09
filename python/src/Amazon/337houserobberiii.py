"""
LeetCode 337: House Robber III

Problem Statement:
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses 
in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken 
into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9

Logic:
1. Use dynamic programming with a bottom-up approach on the binary tree
2. For each node, we maintain two states:
   - rob_current: maximum money if we rob this node (can't rob children)
   - not_rob_current: maximum money if we don't rob this node (can rob children)
3. For each node:
   - If we rob current node: rob_current = node.val + not_rob_left + not_rob_right
   - If we don't rob current node: not_rob_current = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)
4. Use recursion to process the entire tree and return the maximum of the two states at root
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob_helper(node):
            # Base case: if the node is None, return (0, 0)
            if not node:
                return (0, 0)

            # Recursively solve for left and right children
            left = rob_helper(node.left)
            right = rob_helper(node.right)

            # Option 1: Rob the current node, so you cannot rob its children
            rob_current = node.val + left[1] + right[1]

            # Option 2: Do not rob the current node, take the max of robbing or not robbing children
            not_rob_current = max(left) + max(right)

            # Return two values: (max money if robbing this node, max money if not robbing this node)
            return (rob_current, not_rob_current)

        # Call the helper function on the root node
        return max(rob_helper(root))

def create_tree_from_list(values):
    """Helper function to create a binary tree from a list of values."""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def run_test_cases():
    solution = Solution()
    
    # Test case 1: Example from the problem statement
    root1 = create_tree_from_list([3,2,3,None,3,None,1])
    result1 = solution.rob(root1)
    print("Test case 1:")
    print("Input: [3,2,3,null,3,null,1]")
    print(f"Expected: 7")
    print(f"Got: {result1}")
    print(f"Pass? {result1 == 7}\n")
    
    # Test case 2: Another example from the problem statement
    root2 = create_tree_from_list([3,4,5,1,3,None,1])
    result2 = solution.rob(root2)
    print("Test case 2:")
    print("Input: [3,4,5,1,3,null,1]")
    print(f"Expected: 9")
    print(f"Got: {result2}")
    print(f"Pass? {result2 == 9}\n")
    
    # Test case 3: Single node
    root3 = create_tree_from_list([1])
    result3 = solution.rob(root3)
    print("Test case 3:")
    print("Input: [1]")
    print(f"Expected: 1")
    print(f"Got: {result3}")
    print(f"Pass? {result3 == 1}\n")
    
    # Test case 4: Empty tree
    root4 = create_tree_from_list([])
    result4 = solution.rob(root4)
    print("Test case 4:")
    print("Input: []")
    print(f"Expected: 0")
    print(f"Got: {result4}")
    print(f"Pass? {result4 == 0}")

if __name__ == "__main__":
    run_test_cases()
