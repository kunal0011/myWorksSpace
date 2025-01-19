from typing import Optional

"""
LeetCode 25. Reverse Nodes in k-Group

Problem Statement:
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
- The number of nodes in the list is n
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

Approach:
1. Count nodes to handle groups
2. Use helper function to reverse k nodes
3. Keep track of previous group's end
4. Time Complexity: O(n)
5. Space Complexity: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        # Dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while head:
            # Check if we have k nodes left
            group_start = head
            count = 0
            while count < k and head:
                head = head.next
                count += 1

            if count == k:  # If we have k nodes, reverse them
                new_group_start = self.reverseK(group_start, k)
                prev_group_end.next = new_group_start
                prev_group_end = group_start  # Original start becomes end after reverse
                group_start.next = head

        return dummy.next

    def reverseK(self, head: ListNode, k: int) -> ListNode:
        """Helper function to reverse k nodes starting from head"""
        prev = None
        curr = head
        for _ in range(k):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev


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


def test_reverse_k_group():
    """
    Test function to verify the reverseKGroup solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "input": [1, 2, 3, 4, 5],
            "k": 2,
            "expected": [2, 1, 4, 3, 5],
            "description": "Reverse pairs"
        },
        {
            "input": [1, 2, 3, 4, 5],
            "k": 3,
            "expected": [3, 2, 1, 4, 5],
            "description": "Reverse groups of 3"
        },
        {
            "input": [1],
            "k": 1,
            "expected": [1],
            "description": "Single node"
        },
        {
            "input": [1, 2],
            "k": 2,
            "expected": [2, 1],
            "description": "Two nodes, k=2"
        },
        {
            "input": [1, 2, 3, 4, 5, 6],
            "k": 4,
            "expected": [4, 3, 2, 1, 5, 6],
            "description": "Six nodes, k=4"
        },
        {
            "input": [1, 2, 3, 4],
            "k": 4,
            "expected": [4, 3, 2, 1],
            "description": "Exact multiple of k"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_arr = test_case["input"]
        k = test_case["k"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: list={input_arr}, k={k}")

        # Create linked list from input array
        head = create_linked_list(input_arr)

        # Get result and convert back to array for comparison
        result = solution.reverseKGroup(head, k)
        result_array = linked_list_to_array(result)

        assert result_array == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result_array}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_reverse_k_group()
        print("\nAll test cases passed successfully! 🎉")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
