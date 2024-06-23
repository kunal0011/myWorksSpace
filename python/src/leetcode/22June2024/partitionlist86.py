from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        # Pointers to build the two lists
        less = less_dummy
        greater = greater_dummy

        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next

        # Connect the end of the less list to the start of the greater list
        less.next = greater_dummy.next
        # End the greater list
        greater.next = None

        # Return the head of the new list
        return less_dummy.next


def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# Example usage
s = Solution()
head = ListNode(1, ListNode(4, ListNode(
    3, ListNode(2, ListNode(5, ListNode(2))))))
x = 3
print("Original list:")
printList(head)

new_head = s.partition(head, x)
print("Partitioned list:")
printList(new_head)
