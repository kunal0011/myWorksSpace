# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Dummy node to store the sorted list
        sorted_head = ListNode(-1)
        current = head

        while current:
            # Store the next node to be processed
            next_node = current.next
            # Remove current node from the original list
            current.next = None

            # Find the insertion position in the sorted list
            prev = sorted_head
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert current node into the sorted list
            current.next = prev.next
            prev.next = current

            # Move to the next node in the original list
            current = next_node

        return sorted_head.next
