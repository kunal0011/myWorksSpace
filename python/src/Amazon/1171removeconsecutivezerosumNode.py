class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)  # Dummy node to handle edge cases
        dummy.next = head

        prefix_sum = 0
        prefix_map = {}  # Maps prefix sum to the corresponding node
        current = dummy

        # First pass: record the latest occurrence of each prefix sum
        while current:
            prefix_sum += current.val
            prefix_map[prefix_sum] = current
            current = current.next

        # Second pass: reset the next pointers to remove zero-sum sublists
        current = dummy
        prefix_sum = 0
        while current:
            prefix_sum += current.val
            # Skip all nodes in between the first and last occurrence of the same prefix sum
            current.next = prefix_map[prefix_sum].next
            current = current.next

        return dummy.next

# Helper function to create a linked list from a list of values


def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print linked list


def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(" -> ".join(map(str, values)))


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    head1 = create_linked_list([1, 2, -3, 3, 1])
    result1 = sol.removeZeroSumSublists(head1)
    print_linked_list(result1)  # Expected output: 3 -> 1

    # Test case 2
    head2 = create_linked_list([1, 2, 3, -3, 4])
    result2 = sol.removeZeroSumSublists(head2)
    print_linked_list(result2)  # Expected output: 1 -> 2 -> 4

    # Test case 3
    head3 = create_linked_list([1, 2, 3, -3, -2])
    result3 = sol.removeZeroSumSublists(head3)
    print_linked_list(result3)  # Expected output: 1
