# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Use a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node just before left
        for _ in range(left - 1):
            prev = prev.next

        # Initialize pointers to reverse the sublist
        curr = prev.next
        next = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = next
            next = curr
            curr = temp

        # Connect the reversed sublist back to the original list
        prev.next.next = curr
        prev.next = next

        return dummy.next
