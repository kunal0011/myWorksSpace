# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # Helper function to reverse a linked list
        def reverseList(head: ListNode) -> ListNode:
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # Step 1: Reverse the linked list
        head = reverseList(head)

        # Step 2: Add one to the reversed list
        current = head
        carry = 1

        while current:
            current.val += carry
            if current.val < 10:
                carry = 0
                break
            current.val = 0
            if not current.next:
                current.next = ListNode(0)
            current = current.next

        # Step 3: Reverse the list back to its original order
        head = reverseList(head)

        return head
