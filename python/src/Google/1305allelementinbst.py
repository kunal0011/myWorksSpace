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
