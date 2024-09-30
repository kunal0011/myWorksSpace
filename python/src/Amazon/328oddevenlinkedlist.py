class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Initialize pointers for odd and even nodes
        odd = head
        even = head.next
        even_head = even  # Keep the head of the even list

        # Rearrange nodes
        while even and even.next:
            odd.next = even.next  # Connect odd nodes
            odd = odd.next  # Move odd pointer forward
            even.next = odd.next  # Connect even nodes
            even = even.next  # Move even pointer forward

        # Connect the end of odd list to the head of even list
        odd.next = even_head

        return head
