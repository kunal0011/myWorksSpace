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

        # Queue will store tuples of node and its index
        queue = [(root, 0)]
        max_width = 0

        while queue:
            level_length = len(queue)
            _, first_index = queue[0]
            _, last_index = queue[-1]

            # Calculate width of this level
            max_width = max(max_width, last_index - first_index + 1)

            # Traverse the current level
            for _ in range(level_length):
                node, index = queue.pop(0)

                # Append children to the queue with the updated index
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

        return max_width

# Test cases


def test_width_of_binary_tree():
    # Test case 1: Basic binary tree
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)

    sol = Solution()
    # Expected width of the widest level is 4
    assert sol.widthOfBinaryTree(root) == 4

    # Test case 2: Single node
    root = TreeNode(1)
    assert sol.widthOfBinaryTree(root) == 1  # Single node, width is 1

    # Test case 3: Left skewed tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    # All nodes are on one side, width is 1
    assert sol.widthOfBinaryTree(root) == 1

    # Test case 4: Right skewed tree
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.right = TreeNode(7)
    # All nodes are on one side, width is 1
    assert sol.widthOfBinaryTree(root) == 1

    print("All tests passed!")


# Run the tests
test_width_of_binary_tree()
