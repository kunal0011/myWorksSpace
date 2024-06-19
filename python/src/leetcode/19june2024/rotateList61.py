from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        # Calculate the length of the linked list
        current = head
        n = 1
        while current.next:
            current = current.next
            n += 1

        # Adjust k to be within the range [0, n-1]
        k = k % n
        if k == 0:
            return head

        # Find the new tail and break the loop
        current.next = head  # make it circular
        steps_to_new_tail = n - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # New head is the node right after the new tail
        new_head = new_tail.next

        # Break the loop
        new_tail.next = None

        return new_head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(s.rotateRight(head, 2))
