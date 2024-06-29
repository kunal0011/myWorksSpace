# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Step 1: Detect if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # If we exit the loop normally, there is no cycle
            return None

        # Step 2: Find the entry to the cycle
        entry = head
        while entry != slow:
            entry = entry.next
            slow = slow.next

        return entry


# Example usage:
# Creating a cycle linked list: 3 -> 2 -> 0 -> -4 -> 2 (cycle to the second node)
head = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)

head.next = second
second.next = third
third.next = fourth
fourth.next = second
sol = Solution()
result = sol.detectCycle(head)
print(result.val if result else "no cycle")  # Output: 2
