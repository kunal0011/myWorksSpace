# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        curr = head
        while curr != None:
            count += 1
            curr = curr.next

        n = count - n + 1
        if n == 1:
            return head.next
        k = 1
        curr = head
        prev = None
        while k < n:
            prev = curr
            curr = curr.next
            k += 1
        if curr.next != None:
            prev.next = curr.next
        else:
            prev.next = None

        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s = Solution()
    s.removeNthFromEnd(head, 2)
