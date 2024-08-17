class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Iterate while there are nodes to process in either list, or there's a carry left
        while l1 or l2 or carry:
            # Get values from the current nodes of l1 and l2, if present
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            total = total % 10

            # Create a new node with the computed value and move to the next
            current.next = ListNode(total)
            current = current.next

            # Move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the result list, starting from the next of dummy node
        return dummy.next
