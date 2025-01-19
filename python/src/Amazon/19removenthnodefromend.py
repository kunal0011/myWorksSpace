from typing import Optional

"""
LeetCode 19. Remove Nth Node From End of List

Problem Statement:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Approach:
1. Use two pointers (first and second) with a dummy node
2. Move first pointer n+1 steps ahead
3. Move both pointers until first reaches end
4. Remove the node after second pointer
5. Time Complexity: O(n) where n is the length of list
6. Space Complexity: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that helps simplify edge cases
        dummy = ListNode(0, head)
        first = second = dummy

        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from end
        second.next = second.next.next

        return dummy.next


def create_linked_list(arr):
    """Helper function to create a linked list from an array"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head):
    """Helper function to convert linked list to array for comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def test_remove_nth_from_end():
    """
    Test function to verify the removeNthFromEnd solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "input": [1, 2, 3, 4, 5],
            "n": 2,
            "expected": [1, 2, 3, 5],
            "description": "Standard case - remove 2nd node from end"
        },
        {
            "input": [1],
            "n": 1,
            "expected": [],
            "description": "Single node - remove only node"
        },
        {
            "input": [1, 2],
            "n": 1,
            "expected": [1],
            "description": "Two nodes - remove last node"
        },
        {
            "input": [1, 2],
            "n": 2,
            "expected": [2],
            "description": "Two nodes - remove first node"
        },
        {
            "input": [1, 2, 3],
            "n": 3,
            "expected": [2, 3],
            "description": "Remove first node of three nodes"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_list = test_case["input"]
        n = test_case["n"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: list={input_list}, n={n}")

        # Create linked list from input array
        head = create_linked_list(input_list)

        # Get result and convert back to array for comparison
        result = solution.removeNthFromEnd(head, n)
        result_array = linked_list_to_array(result)

        assert result_array == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result_array}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_remove_nth_from_end()
        print("\nAll test cases passed successfully! 🎉")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
