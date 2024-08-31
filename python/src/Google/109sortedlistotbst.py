# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Helper function to find the middle element of the linked list
        def find_middle(start, end):
            slow = fast = start
            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            return slow

        # Main function to recursively build the BST
        def convert_list_to_bst(start, end):
            if start == end:
                return None

            mid = find_middle(start, end)
            node = TreeNode(mid.val)

            # Recursively build the left and right subtrees
            node.left = convert_list_to_bst(start, mid)
            node.right = convert_list_to_bst(mid.next, end)

            return node

        return convert_list_to_bst(head, None)
