# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # Step 1: Find the length of the linked list and the k-th node from the beginning
        first = last = head
        for _ in range(k - 1):
            first = first.next

        # Step 2: Use two-pointer technique to find the k-th node from the end
        temp = first
        while temp.next:
            temp = temp.next
            last = last.next

        # Step 3: Swap the values of the two nodes
        first.val, last.val = last.val, first.val

        return head
