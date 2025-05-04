"""
LeetCode 1305: All Elements in Two Binary Search Trees

Problem Statement:
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

Logic:
1. Use inorder traversal to get sorted lists from both BSTs
2. Merge two sorted lists using two-pointer technique:
   - Compare elements from both lists
   - Add smaller element to result
   - Move pointer of used list
3. Add remaining elements from either list

Time Complexity: O(m + n) where m, n are sizes of trees
Space Complexity: O(m + n) for storing result
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: 'TreeNode', root2: 'TreeNode') -> list[int]:
        def inorder(root: 'TreeNode') -> list[int]:
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []

        # Get the sorted elements from both trees
        list1 = inorder(root1)
        list2 = inorder(root2)

        # Merge the two sorted lists
        i, j = 0, 0
        merged = []

        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1

        # If there are remaining elements in list1
        while i < len(list1):
            merged.append(list1[i])
            i += 1

        # If there are remaining elements in list2
        while j < len(list2):
            merged.append(list2[j])
            j += 1

        return merged


def test_get_all_elements():
    solution = Solution()

    # Test case 1: Basic BSTs
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)

    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(3)

    result1 = solution.getAllElements(root1, root2)
    expected1 = [0, 1, 1, 2, 3, 4]
    assert result1 == expected1, f"Test case 1 failed. Expected {expected1}, got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: Empty trees
    result2 = solution.getAllElements(None, None)
    assert result2 == [], f"Test case 2 failed. Expected [], got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: One empty tree
    root3 = TreeNode(5)
    root3.left = TreeNode(3)
    root3.right = TreeNode(7)

    result3 = solution.getAllElements(root3, None)
    expected3 = [3, 5, 7]
    assert result3 == expected3, f"Test case 3 failed. Expected {expected3}, got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: Single node trees
    root4 = TreeNode(1)
    root5 = TreeNode(2)

    result4 = solution.getAllElements(root4, root5)
    expected4 = [1, 2]
    assert result4 == expected4, f"Test case 4 failed. Expected {expected4}, got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_get_all_elements()
