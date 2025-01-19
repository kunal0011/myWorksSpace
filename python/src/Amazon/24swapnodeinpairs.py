from typing import Optional

"""
LeetCode 24. Swap Nodes in Pairs

Problem Statement:
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
- The number of nodes in the list is in the range [0, 100]
- 0 <= Node.val <= 100

Approach:
1. Use a dummy node to handle edge cases
2. Use three pointers (prev, curr, next) to perform swaps
3. Iterate through list swapping pairs
4. Time Complexity: O(n)
5. Space Complexity: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty list or single node
        if not head or not head.next:
            return head

        # Create dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            # Nodes to be swapped
            first = head
            second = head.next

            # Perform swap
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers
            prev = first
            head = first.next

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


def test_swap_pairs():
    """
    Test function to verify the swapPairs solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "input": [1, 2, 3, 4],
            "expected": [2, 1, 4, 3],
            "description": "Even number of nodes"
        },
        {
            "input": [1],
            "expected": [1],
            "description": "Single node"
        },
        {
            "input": [],
            "expected": [],
            "description": "Empty list"
        },
        {
            "input": [1, 2, 3],
            "expected": [2, 1, 3],
            "description": "Odd number of nodes"
        },
        {
            "input": [1, 2],
            "expected": [2, 1],
            "description": "Two nodes"
        },
        {
            "input": [1, 2, 3, 4, 5],
            "expected": [2, 1, 4, 3, 5],
            "description": "Five nodes"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_arr = test_case["input"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: {input_arr}")

        # Create linked list from input array
        head = create_linked_list(input_arr)

        # Get result and convert back to array for comparison
        result = solution.swapPairs(head)
        result_array = linked_list_to_array(result)

        assert result_array == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result_array}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_swap_pairs()
        print("\nAll test cases passed successfully! 🎉")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
