"""
LeetCode 82. Remove Duplicates from Sorted List II

Problem Statement:
Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

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

        # Create dummy node to handle cases where head needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            # Check if current node is the start of duplicates
            if curr.val == curr.next.val:
                # Skip all nodes with the same value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Move one more step to skip last duplicate
                curr = curr.next
                # Connect previous node to next distinct value
                prev.next = curr
            else:
                # Move both pointers forward
                prev = curr
                curr = curr.next

        return dummy.next


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
            "input": [1, 2, 3, 3, 4, 4, 5],
            "expected": [1, 2, 5],
            "description": "Multiple duplicates"
        },
        {
            "input": [1, 1, 1, 2, 3],
            "expected": [2, 3],
            "description": "Duplicates at start"
        },
        {
            "input": [1, 2, 2],
            "expected": [1],
            "description": "Duplicates at end"
        },
        {
            "input": [1, 1],
            "expected": [],
            "description": "All duplicates"
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
