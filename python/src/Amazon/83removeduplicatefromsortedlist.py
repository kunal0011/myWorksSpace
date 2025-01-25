"""
LeetCode 83. Remove Duplicates from Sorted List

Problem Statement:
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
- The number of nodes in the list is in the range [0, 300]
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Handle empty list or single node
        if not head or not head.next:
            return head

        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                # Skip duplicate
                curr.next = curr.next.next
            else:
                # Move to next node
                curr = curr.next

        return head


def create_linked_list(arr: list) -> ListNode:
    """Helper function to create linked list from array"""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_list_to_array(head: ListNode) -> list:
    """Helper function to convert linked list to array"""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


def test_delete_duplicates():
    solution = Solution()

    test_cases = [
        {
            "input": [1, 1, 2],
            "expected": [1, 2],
            "description": "Basic case"
        },
        {
            "input": [1, 1, 2, 3, 3],
            "expected": [1, 2, 3],
            "description": "Multiple duplicates"
        },
        {
            "input": [1, 1, 1],
            "expected": [1],
            "description": "All same values"
        },
        {
            "input": [1, 2, 3],
            "expected": [1, 2, 3],
            "description": "No duplicates"
        },
        {
            "input": [],
            "expected": [],
            "description": "Empty list"
        },
        {
            "input": [1],
            "expected": [1],
            "description": "Single element"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_arr = test_case["input"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Input: {input_arr}")

        head = create_linked_list(input_arr)
        result = solution.deleteDuplicates(head)
        result_arr = linked_list_to_array(result)

        assert result_arr == expected, \
            f"Expected {expected}, but got {result_arr}"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_delete_duplicates()
    print("\nAll test cases passed! 🎉")
