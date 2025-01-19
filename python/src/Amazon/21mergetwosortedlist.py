from typing import Optional

"""
LeetCode 21. Merge Two Sorted Lists

Problem Statement:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by 
splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order

Approach:
1. Use a dummy node to handle edge cases
2. Compare nodes from both lists and link smaller one
3. Move pointer in the list from which node was taken
4. Attach remaining nodes from non-empty list
5. Time Complexity: O(n + m) where n, m are lengths of input lists
6. Space Complexity: O(1) as we reuse existing nodes
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node
        dummy = ListNode()
        current = dummy

        # Compare and merge while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach remaining nodes from either list
        current.next = list1 if list1 else list2

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


def test_merge_two_lists():
    """
    Test function to verify the mergeTwoLists solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "list1": [1, 2, 4],
            "list2": [1, 3, 4],
            "expected": [1, 1, 2, 3, 4, 4],
            "description": "Standard case with equal length lists"
        },
        {
            "list1": [],
            "list2": [],
            "expected": [],
            "description": "Empty lists"
        },
        {
            "list1": [],
            "list2": [0],
            "expected": [0],
            "description": "One empty list"
        },
        {
            "list1": [1, 3, 5],
            "list2": [2, 4, 6],
            "expected": [1, 2, 3, 4, 5, 6],
            "description": "Alternating values"
        },
        {
            "list1": [1, 2, 3],
            "list2": [4, 5, 6],
            "expected": [1, 2, 3, 4, 5, 6],
            "description": "Non-overlapping ranges"
        },
        {
            "list1": [1],
            "list2": [2],
            "expected": [1, 2],
            "description": "Single node lists"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        list1_arr = test_case["list1"]
        list2_arr = test_case["list2"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: list1={list1_arr}, list2={list2_arr}")

        # Create linked lists from input arrays
        list1 = create_linked_list(list1_arr)
        list2 = create_linked_list(list2_arr)

        # Get result and convert back to array for comparison
        result = solution.mergeTwoLists(list1, list2)
        result_array = linked_list_to_array(result)

        assert result_array == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result_array}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_merge_two_lists()
        print("\nAll test cases passed successfully! 🎉")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
