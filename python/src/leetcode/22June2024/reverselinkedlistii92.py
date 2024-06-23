
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


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))


left = 2
right = 4
print("Original list:")
printList(head)
s = Solution()
new_head = s.reverseBetween(head, left, right)
print("List after reversing from position 2 to 4:")
printList(new_head)
