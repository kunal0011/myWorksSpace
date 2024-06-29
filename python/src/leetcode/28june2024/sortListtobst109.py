from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        # Step 1: Convert the linked list to an array
        values = []
        while head:
            values.append(head.val)
            head = head.next

        # Step 2: Recursive function to convert sorted array to BST
        def sortedArrayToBST(nums):
            if not nums:
                return None

            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = sortedArrayToBST(nums[:mid])
            node.right = sortedArrayToBST(nums[mid+1:])
            return node

        # Use the sorted array to construct the BST
        return sortedArrayToBST(values)
