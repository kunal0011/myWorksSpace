"""
LeetCode 337 - House Robber III

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

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree (due to recursion stack)
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


def create_tree(values):
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


def test_house_robber():
    # Test cases
    test_cases = [
        [3, 2, 3, None, 3, None, 1],
        [3, 4, 5, 1, 3, None, 1],
        [3, 1, None, None, 2],
        [],
        [1],
        [4, 1, 2, 3],
    ]

    expected_outputs = [7, 9, 5, 0, 1, 7]

    solution = Solution()
    for i, (test_input, expected) in enumerate(zip(test_cases, expected_outputs)):
        root = create_tree(test_input)
        result = solution.rob(root)
        print(f"Test case {i + 1}:")
        print(f"Input: {test_input}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}\n")


if __name__ == "__main__":
    test_house_robber()
