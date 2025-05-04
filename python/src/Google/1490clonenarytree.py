"""
LeetCode 1490. Clone N-ary Tree

Problem Statement:
Given a root node reference of a N-ary tree, return a deep copy (clone) of the tree.
Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree (recursion stack)
"""

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        # Logic:
        # 1. Use DFS (recursion) to traverse the tree
        # 2. For each node:
        #    - Create a new node with same value
        #    - Recursively clone all children
        #    - Append cloned children to current node's children list
        # 3. Base case: return None for null nodes

        if not root:
            return None

        # Create a copy of the current node
        clone_root = Node(root.val)

        # Recursively clone all the children
        for child in root.children:
            clone_root.children.append(self.cloneTree(child))

        return clone_root


# Test driver
def printNaryTree(node: 'Node', level: int = 0) -> None:
    if not node:
        return
    print("  " * level + str(node.val))
    for child in node.children:
        printNaryTree(child, level + 1)


if __name__ == "__main__":
    # Create test cases
    # Test Case 1: Simple tree with 3 children
    root1 = Node(1)
    root1.children = [Node(3), Node(2), Node(4)]
    root1.children[0].children = [Node(5), Node(6)]

    # Test Case 2: Single node
    root2 = Node(1)

    # Test Case 3: Empty tree
    root3 = None

    solution = Solution()

    # Test all cases
    test_cases = [(root1, "Tree with multiple children"),
                  (root2, "Single node tree"),
                  (root3, "Empty tree")]

    for i, (root, description) in enumerate(test_cases):
        print(f"\nTest case {i + 1}: {description}")
        print("Original tree:")
        printNaryTree(root)

        cloned = solution.cloneTree(root)
        print("\nCloned tree:")
        printNaryTree(cloned)

        # Verify that the trees are separate (modifying original shouldn't affect clone)
        if root:
            root.val = 999  # Modify original
            print("\nOriginal after modification (val=999):")
            printNaryTree(root)
            print("\nCloned tree should remain unchanged:")
            printNaryTree(cloned)
        print("\n" + "="*50)
