"""
LeetCode 143. Reorder List

Problem Statement:
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → L2 → ... → Ln-1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4]
- 1 <= Node.val <= 1000
"""

from typing import Optional, List, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not head or not head.next:
            return

        # Step 1: Find middle of the list
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        curr = slow.next
        slow.next = None  # Break the list

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: Merge two halves
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

    def reorderListWithSteps(self, head: Optional[ListNode]) -> List[List[int]]:
        """
        Returns list of states after each step.
        Time complexity: O(n)
        Space complexity: O(n) for tracking states
        """
        if not head or not head.next:
            return [[self.get_values(head)]]

        states = []
        states.append(self.get_values(head))

        # Step 1: Find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Record state after finding middle
        states.append(self.get_values(head))

        # Step 2: Reverse second half
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Record state after reversal
        second_half = prev
        temp_head = ListNode(0)
        temp_head.next = head
        curr = temp_head
        while curr.next:
            curr = curr.next
        curr.next = second_half
        states.append(self.get_values(temp_head.next))
        curr.next = None

        # Step 3: Merge halves
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            states.append(self.get_values(head))

        return states

    def get_values(self, node: Optional[ListNode]) -> List[int]:
        """Helper function to get list of values from linked list."""
        values = []
        while node:
            values.append(node.val)
            node = node.next
        return values


def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """Helper function to create linked list from values."""
    if not values:
        return None

    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def visualize_steps(steps: List[List[int]]) -> None:
    """Helper function to visualize reordering steps."""
    print("\nReordering Steps:")
    for i, step in enumerate(steps):
        arrows = " → ".join(map(str, step))
        print(f"Step {i}: {arrows}")


def test_reorder_list():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "values": [1, 2, 3, 4],
            "expected": [1, 4, 2, 3],
            "description": "Even length list"
        },
        {
            "values": [1, 2, 3, 4, 5],
            "expected": [1, 5, 2, 4, 3],
            "description": "Odd length list"
        },
        {
            "values": [1],
            "expected": [1],
            "description": "Single node"
        },
        {
            "values": [1, 2],
            "expected": [1, 2],
            "description": "Two nodes"
        },
        {
            "values": [1, 2, 3],
            "expected": [1, 3, 2],
            "description": "Three nodes"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Input: {test_case['values']}")

        # Test both implementations
        head1 = create_linked_list(test_case['values'])
        head2 = create_linked_list(test_case['values'])

        solution.reorderList(head1)
        steps = solution.reorderListWithSteps(head2)

        result1 = solution.get_values(head1)
        result2 = steps[-1]  # Final state

        print(f"\nResults:")
        print(f"Final order: {' → '.join(map(str, result1))}")

        visualize_steps(steps)

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {result2}"

        # Verify all nodes are present
        assert sorted(result1) == sorted(test_case['values']), \
            "Some nodes are missing in the result"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_reorder_list()
