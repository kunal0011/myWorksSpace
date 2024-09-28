class ListNode:
    pass


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Find the middle of the linked list using slow and fast pointers
        middle = self.findMiddle(head)
        left_half = head
        right_half = middle.next
        middle.next = None

        # Recursively sort the two halves
        left_sorted = self.sortList(left_half)
        right_sorted = self.sortList(right_half)

        # Merge the two sorted halves
        return self.merge(left_sorted, right_sorted)

    def findMiddle(self, head):
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev  # Return prev to get the actual middle node

    def merge(self, left, right):
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        if left:
            current.next = left
        if right:
            current.next = right

        return dummy.next
