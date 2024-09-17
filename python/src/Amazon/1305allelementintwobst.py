# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        def inorder_traversal(root):
            """Helper function to perform inorder traversal of a BST."""
            if root is None:
                return []
            return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

        # Get the sorted lists from both trees
        list1 = inorder_traversal(root1)
        list2 = inorder_traversal(root2)

        # Merge the two sorted lists
        result = []
        i = j = 0

        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1

        # Append remaining elements from list1 or list2
        result.extend(list1[i:])
        result.extend(list2[j:])

        return result


# Test cases
if __name__ == "__main__":
    # Helper function to create a binary tree from a list
    def insert_into_bst(root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
        return root

    # Example 1
    root1 = None
    for val in [2, 1, 4]:
        root1 = insert_into_bst(root1, val)

    root2 = None
    for val in [1, 0, 3]:
        root2 = insert_into_bst(root2, val)

    sol = Solution()
    result = sol.getAllElements(root1, root2)
    assert result == [0, 1, 1, 2, 3, 4], f"Test case 1 failed: {result}"

    # Example 2: both trees are empty
    root1 = None
    root2 = None
    result = sol.getAllElements(root1, root2)
    assert result == [], f"Test case 2 failed: {result}"

    print("All test cases passed!")
