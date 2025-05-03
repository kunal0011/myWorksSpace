"""
LeetCode 572 - Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root 
with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree is a tree that consists of a node in tree and all of this node's descendants.

Logic:
1. For each node in the main tree (root):
   - Check if the subtree rooted at this node is identical to subRoot
   - If identical, return True
   - If not, recursively check left and right subtrees
2. Two trees are identical if:
   - Both are null (empty)
   - Values are same and their left and right subtrees are identical

Time Complexity: O(m*n) where m and n are number of nodes in root and subRoot
Space Complexity: O(h) where h is height of main tree (recursion stack)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # Helper function to check if two trees are identical
        def isSameTree(t1: TreeNode, t2: TreeNode) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and
                    isSameTree(t1.left, t2.left) and
                    isSameTree(t1.right, t2.right))

        # Main function to check if t is a subtree of s
        if not s:
            return False
        if isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


def create_tree(values):
    """Helper function to create a binary tree from list of values."""
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


def run_test_cases():
    solution = Solution()
    test_cases = [
        {
            "root": [3, 4, 5, 1, 2],
            "subRoot": [4, 1, 2],
            "expected": True,
            "explanation": "The tree [4,1,2] is a subtree of [3,4,5,1,2]"
        },
        {
            "root": [3, 4, 5, 1, 2, None, None, None, None, 0],
            "subRoot": [4, 1, 2],
            "expected": False,
            "explanation": "The tree structures are different"
        },
        {
            "root": [1, 1],
            "subRoot": [1],
            "expected": True,
            "explanation": "Single node subtree"
        },
        {
            "root": [1],
            "subRoot": [2],
            "expected": False,
            "explanation": "Different values"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        root = create_tree(test["root"])
        subRoot = create_tree(test["subRoot"])
        result = solution.isSubtree(root, subRoot)
        print(f"\nTest Case {i}:")
        print(f"Root tree: {test['root']}")
        print(f"Subtree: {test['subRoot']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}")
        print(f"{'✓ Passed' if result == test['expected'] else '✗ Failed'}")


if __name__ == "__main__":
    run_test_cases()
