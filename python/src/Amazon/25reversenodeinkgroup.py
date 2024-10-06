# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Function to reverse a portion of the linked list
        def reverseLinkedList(head, k):
            prev, curr = None, head
            while k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k -= 1
            return prev

        # Count the length of the list
        count = 0
        node = head
        while node:
            node = node.next
            count += 1

        # Create a dummy node to handle edge cases smoothly
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while count >= k:
            curr = prev.next
            next_group = curr

            # Move `next_group` pointer to the end of the current k-group
            for i in range(k - 1):
                next_group = next_group.next

            next_group_next = next_group.next
            # Reverse the k nodes
            next_group.next = None
            prev.next = reverseLinkedList(curr, k)
            curr.next = next_group_next

            prev = curr
            count -= k

        return dummy.next
