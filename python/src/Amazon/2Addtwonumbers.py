# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate sum
            total = x + y + carry
            carry = total // 10

            # Create new node
            current.next = ListNode(total % 10)
            current = current.next

            # Move to next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


def test_addTwoNumbers():
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_array(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    solution = Solution()

    # Test case 1: 243 + 564 = 807
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [7, 0, 8]

    # Test case 2: 0 + 0 = 0
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [0]

    # Test case 3: 9999999 + 9999 = 10009998
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [8, 9, 9, 9, 0, 0, 0, 1]

    print("All test cases passed!")


if __name__ == "__main__":
    test_addTwoNumbers()
