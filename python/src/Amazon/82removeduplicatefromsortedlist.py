# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current:
            # Check if the current node has duplicates
            if current.next and current.val == current.next.val:
                # Skip all nodes with the same value
                while current.next and current.val == current.next.val:
                    current = current.next
                # Move prev's next to the node after the last duplicate
                prev.next = current.next
            else:
                # Move prev to the next node if no duplicate was found
                prev = prev.next

            # Move current to the next node
            current = current.next

        return dummy.next
