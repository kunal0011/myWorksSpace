"""
LeetCode 148. Sort List

Problem Statement:
Given the head of a linked list, return the list after sorting it in ascending order.
Can you sort the linked list in O(n log n) time and O(1) space (i.e. constant space)?

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is in the range [0, 5 * 10^4]
- -10^5 <= Node.val <= 10^5
"""

from typing import Optional, List, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge sort implementation.
        Time complexity: O(n log n)
        Space complexity: O(log n) for recursion stack
        """
        if not head or not head.next:
            return head

        # Find middle of list
        slow = fast = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Split list into two halves
        prev.next = None

        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)

        # Merge sorted halves
        return self.merge(left, right)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Helper function to merge two sorted lists."""
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next

    def sortListWithSteps(self, head: Optional[ListNode]) -> Tuple[Optional[ListNode], List[List[int]]]:
        """
        Returns both sorted list and intermediate steps.
        Time complexity: O(n log n)
        Space complexity: O(n) for tracking steps
        """
        def merge_with_steps(l1: Optional[ListNode], l2: Optional[ListNode], steps: List[List[int]]) -> Optional[ListNode]:
            if not l1 or not l2:
                return l1 or l2

            dummy = ListNode(0)
            curr = dummy
            steps.append(["Merging", self.get_values(l1), self.get_values(l2)])

            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            curr.next = l1 or l2
            result = dummy.next
            steps.append(["Merged result", self.get_values(result)])
            return result

        def sort_with_steps(head: Optional[ListNode], steps: List[List[int]]) -> Optional[ListNode]:
            if not head or not head.next:
                return head

            steps.append(["Splitting", self.get_values(head)])

            # Find middle
            slow = fast = prev = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            # Split list
            prev.next = None

            # Recursively sort
            left = sort_with_steps(head, steps)
            right = sort_with_steps(slow, steps)

            # Merge
            return merge_with_steps(left, right, steps)

        steps = []
        sorted_list = sort_with_steps(head, steps)
        return sorted_list, steps

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


def visualize_steps(steps: List[List]) -> None:
    """Helper function to visualize sorting steps."""
    print("\nSorting Steps:")
    for i, step in enumerate(steps):
        action = step[0]
        if action == "Splitting":
            print(f"Step {i}: Splitting list: {step[1]}")
        elif action == "Merging":
            print(f"Step {i}: Merging lists: {step[1]} and {step[2]}")
        else:  # Merged result
            print(f"Step {i}: Merged result: {step[1]}")


def test_sort_list():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "values": [4, 2, 1, 3],
            "expected": [1, 2, 3, 4],
            "description": "Basic case"
        },
        {
            "values": [-1, 5, 3, 4, 0],
            "expected": [-1, 0, 3, 4, 5],
            "description": "Negative numbers"
        },
        {
            "values": [],
            "expected": [],
            "description": "Empty list"
        },
        {
            "values": [1],
            "expected": [1],
            "description": "Single node"
        },
        {
            "values": [5, 4, 3, 2, 1],
            "expected": [1, 2, 3, 4, 5],
            "description": "Reverse sorted"
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

        result1 = solution.sortList(head1)
        result2, steps = solution.sortListWithSteps(head2)

        result1_values = solution.get_values(result1)
        result2_values = solution.get_values(result2)

        print(f"\nResults:")
        print(f"Sorted list: {result1_values}")

        visualize_steps(steps)

        assert result1_values == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1_values}"
        assert result2_values == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {result2_values}"

        # Verify all elements are present
        assert sorted(test_case['values']) == result1_values, \
            "Some elements are missing in the result"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_sort_list()
