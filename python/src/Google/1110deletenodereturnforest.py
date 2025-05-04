"""
LeetCode 1110: Delete Nodes And Return Forest

Problem Statement:
Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest. You may return the result in any order.

Logic:
1. Use post-order traversal to process nodes bottom-up
2. Convert to_delete list to set for O(1) lookup
3. For each node:
   - Recursively process left and right subtrees
   - If node value is in to_delete:
     * Add its children to forest (they become new roots)
     * Return None to delete the node
   - If node is a root, add it to forest
4. Handle special case for root node

Time Complexity: O(n) where n is number of nodes
Space Complexity: O(h + d) where h is height of tree, d is size of to_delete
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        # Convert to_delete to a set for quick lookup
        to_delete_set = set(to_delete)
        forest = []

        # Helper function to perform postorder traversal and delete nodes
        def postorder(node: TreeNode, is_root: bool) -> TreeNode:
            if not node:
                return None

            # Recursively delete nodes in the left and right subtrees
            node.left = postorder(node.left, False)
            node.right = postorder(node.right, False)

            # Check if the current node needs to be deleted
            if node.val in to_delete_set:
                # If the node is to be deleted, add its children to the forest
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None  # Return None to remove this node

            # If the node is a root of the forest, add it to the result
            if is_root:
                forest.append(node)

            return node

        # Start the postorder traversal from the root
        postorder(root, True)

        return forest


def test_delete_nodes():
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

    def get_values(nodes):
        result = []
        for node in nodes:
            values = []
            queue = [node]
            while queue:
                curr = queue.pop(0)
                values.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(values)
        return sorted(result)

    solution = Solution()

    # Test case 1: Basic case
    root1 = create_tree([1, 2, 3, 4, 5, 6, 7])
    to_delete1 = [3, 5]
    result1 = solution.delNodes(root1, to_delete1)
    result_vals1 = get_values(result1)
    expected1 = [[1, 2, 4], [6], [7]]
    assert sorted(
        result_vals1) == expected1, f"Test case 1 failed. Expected {expected1}, got {result_vals1}"
    print(f"Test case 1 passed: Forest roots = {result_vals1}")

    # Test case 2: Delete root
    root2 = create_tree([1, 2, 3])
    to_delete2 = [1]
    result2 = solution.delNodes(root2, to_delete2)
    result_vals2 = get_values(result2)
    expected2 = [[2], [3]]
    assert sorted(
        result_vals2) == expected2, f"Test case 2 failed. Expected {expected2}, got {result_vals2}"
    print(f"\nTest case 2 passed: Forest roots = {result_vals2}")

    # Test case 3: Delete leaf nodes
    root3 = create_tree([1, 2, 3, 4, 5])
    to_delete3 = [4, 5]
    result3 = solution.delNodes(root3, to_delete3)
    result_vals3 = get_values(result3)
    expected3 = [[1, 2, 3]]
    assert sorted(
        result_vals3) == expected3, f"Test case 3 failed. Expected {expected3}, got {result_vals3}"
    print(f"\nTest case 3 passed: Forest roots = {result_vals3}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_delete_nodes()
