class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node that helps simplify edge cases
        dummy = ListNode(0, head)
        first = second = dummy

        # Move `first` pointer `n+1` steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both `first` and `second` pointers until `first` reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # `second.next` is the node to be removed
        second.next = second.next.next

        return dummy.next

# Example usage


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Creating the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

solution = Solution()
# Remove the 2nd node from the end (node with value 4)
new_head = solution.removeNthFromEnd(head, 2)

print_list(new_head)  # Output: 1 -> 2 -> 3 -> 5 -> None
