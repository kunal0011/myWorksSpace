class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Given the head of a linked list, remove all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Example
# Input: head = [1, 2, 3, 3, 4, 4, 5]
# Output: [1, 2, 5]
# Explanation: Nodes with values 3 and 4 are duplicated, so they are removed.
# Solution Using Python
# To solve this problem, you need to follow these steps:

# Count Frequencies: Use a dictionary to count the frequency of each value in the list.
# Filter Unique Nodes: Iterate through the list again, keeping only nodes with a count of 1.


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        # Step 1: Count frequencies
        count = {}
        current = head
        while current:
            count[current.val] = count.get(current.val, 0) + 1
            current = current.next

        # Step 2: Remove nodes with duplicates
        dummy = ListNode(0)  # Dummy node to simplify edge cases
        dummy.next = head
        current = dummy

        while current.next:
            if count[current.next.val] > 1:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next
