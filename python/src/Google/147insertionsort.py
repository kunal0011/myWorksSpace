class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Initialize a dummy node to act as the sorted portion of the list
        dummy = ListNode(0)
        current = head

        while current:
            # At each iteration, we need to insert current into the sorted part
            prev = dummy
            # Find the right position to insert current
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Save the next node to be processed
            next_node = current.next

            # Insert current between prev and prev.next
            current.next = prev.next
            prev.next = current

            # Move to the next node in the input list
            current = next_node

        # Return the sorted list starting from dummy.next
        return dummy.next
