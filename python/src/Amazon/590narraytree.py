# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traverse(node):
            if not node:
                return
            # First traverse all the children
            for child in node.children:
                traverse(child)
            # Then visit the node itself
            result.append(node.val)

        result = []
        traverse(root)
        return result


# Test case
if __name__ == "__main__":
    # Example tree:
    #        1
    #      / | \
    #     3  2  4
    #    / \
    #   5   6
    node5 = Node(5)
    node6 = Node(6)
    node3 = Node(3, [node5, node6])
    node2 = Node(2)
    node4 = Node(4)
    root = Node(1, [node3, node2, node4])

    sol = Solution()
    print(sol.postorder(root))  # Expected output: [5, 6, 3, 2, 4, 1]
