# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        while head:
            # Left shift num by 1 bit (equivalent to multiplying by 2)
            # and add the current node's value
            num = num * 2 + head.val
            head = head.next
        return num


# Test cases
if __name__ == "__main__":
    # Helper function to create a linked list from a list of values
    def create_linked_list(values):
        dummy = ListNode()
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    sol = Solution()

    # Test case 1
    head1 = create_linked_list([1, 0, 1])
    result1 = sol.getDecimalValue(head1)
    assert result1 == 5, f"Test case 1 failed: {result1}"

    # Test case 2
    head2 = create_linked_list([0])
    result2 = sol.getDecimalValue(head2)
    assert result2 == 0, f"Test case 2 failed: {result2}"

    # Test case 3
    head3 = create_linked_list([1])
    result3 = sol.getDecimalValue(head3)
    assert result3 == 1, f"Test case 3 failed: {result3}"

    print("All test cases passed!")
