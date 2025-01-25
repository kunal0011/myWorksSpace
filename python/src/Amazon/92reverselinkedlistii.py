"""
LeetCode 92. Reverse Linked List II

Problem Statement:
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
- The number of nodes in the list is n
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Use a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node just before left
        for _ in range(left - 1):
            prev = prev.next

        # Initialize pointers to reverse the sublist
        curr = prev.next
        next = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = next
            next = curr
            curr = temp

        # Connect the reversed sublist back to the original list
        prev.next.next = curr
        prev.next = next

        return dummy.next


def create_linked_list(arr: list) -> ListNode:
    """Helper function to create linked list from array"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head: ListNode) -> list:
    """Helper function to convert linked list to array"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def visualize_linked_list(head: ListNode, left: int = None, right: int = None) -> str:
    """Helper function to visualize the linked list with optional highlighting"""
    result = []
    current = head
    pos = 1
    while current:
        val = str(current.val)
        if left and right and left <= pos <= right:
            val = f"[{val}]"  # Highlight reversed portion
        result.append(val)
        current = current.next
        pos += 1
    return " -> ".join(result)


def test_reverse_between():
    solution = Solution()

    test_cases = [
        {
            "arr": [1, 2, 3, 4, 5],
            "left": 2,
            "right": 4,
            "expected": [1, 4, 3, 2, 5],
            "description": "Standard case"
        },
        {
            "arr": [5],
            "left": 1,
            "right": 1,
            "expected": [5],
            "description": "Single node"
        },
        {
            "arr": [1, 2, 3],
            "left": 1,
            "right": 3,
            "expected": [3, 2, 1],
            "description": "Reverse entire list"
        },
        {
            "arr": [1, 2, 3, 4, 5],
            "left": 1,
            "right": 2,
            "expected": [2, 1, 3, 4, 5],
            "description": "Reverse from start"
        },
        {
            "arr": [1, 2, 3, 4, 5],
            "left": 4,
            "right": 5,
            "expected": [1, 2, 3, 5, 4],
            "description": "Reverse at end"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        arr = test_case["arr"]
        left = test_case["left"]
        right = test_case["right"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        head = create_linked_list(arr)

        print("Before:", visualize_linked_list(head, left, right))
        result = solution.reverseBetween(head, left, right)
        print("After: ", visualize_linked_list(result))

        result_arr = linked_list_to_array(result)
        assert result_arr == expected, \
            f"Expected {expected}, but got {result_arr}"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_reverse_between()
    print("\nAll test cases passed! 🎉")
