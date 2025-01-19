from typing import List, Optional
import heapq

"""
LeetCode 23. Merge k Sorted Lists

Problem Statement:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order
- The sum of lists[i].length will not exceed 10^4

Approach:
1. Use a min-heap to efficiently find the smallest element among k lists
2. Initialize heap with first node from each list
3. Pop smallest element and add next node from its list to heap
4. Time Complexity: O(N * log(k)) where N is total nodes and k is number of lists
5. Space Complexity: O(k) for the heap
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Remove empty lists
        lists = [lst for lst in lists if lst]
        if not lists:
            return None

        # Initialize the min heap with first node from each list
        heap = []
        for i, head in enumerate(lists):
            heapq.heappush(heap, (head.val, i, head))

        # Create dummy node for result
        dummy = ListNode(0)
        current = dummy

        # Process nodes from heap
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            # If there are more nodes in this list, add to heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

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


def test_merge_k_lists():
    """
    Test function to verify the mergeKLists solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "input": [[1, 4, 5], [1, 3, 4], [2, 6]],
            "expected": [1, 1, 2, 3, 4, 4, 5, 6],
            "description": "Standard case with three lists"
        },
        {
            "input": [],
            "expected": [],
            "description": "Empty input array"
        },
        {
            "input": [[]],
            "expected": [],
            "description": "Single empty list"
        },
        {
            "input": [[1], [2], [3]],
            "expected": [1, 2, 3],
            "description": "Single elements in each list"
        },
        {
            "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "description": "Non-overlapping sorted lists"
        },
        {
            "input": [[1, 1, 1], [1, 1, 1]],
            "expected": [1, 1, 1, 1, 1, 1],
            "description": "Lists with duplicate values"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_lists = test_case["input"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: lists={input_lists}")

        # Convert input arrays to linked lists
        lists = [create_linked_list(lst) for lst in input_lists]

        # Get result and convert back to array for comparison
        result = solution.mergeKLists(lists)
        result_array = linked_list_to_array(result)

        assert result_array == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result_array}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_merge_k_lists()
        print("\nAll test cases passed successfully! 🎉")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
