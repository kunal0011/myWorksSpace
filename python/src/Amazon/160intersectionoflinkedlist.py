"""
LeetCode 160. Intersection of Two Linked Lists

Problem Statement:
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference to the node with value = 8
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5].
There are 2 nodes before the intersected node in A and 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference to the node with value = 2
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).

Constraints:
- The number of nodes of listA is in the m.
- The number of nodes of listB is in the n.
- 1 <= m, n <= 3 * 10^4
- 1 <= Node.val <= 10^5
- 0 <= skipA < m
- 0 <= skipB < n
- intersectVal is 0 if listA and listB do not intersect.
- intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Time complexity: O(n + m) where n and m are lengths of the lists
        Space complexity: O(1)

        Uses the two-pointer technique where each pointer traverses both lists
        to handle the difference in lengths automatically.
        """
        if not headA or not headB:
            return None

        # Initialize pointers
        ptrA = headA
        ptrB = headB

        # Traverse both lists
        while ptrA != ptrB:
            # Move to next node or switch to other list's head
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        # Either found intersection or both are None (no intersection)
        return ptrA


def create_linked_list(values: list, intersection_node: Optional[ListNode] = None) -> ListNode:
    """Helper function to create a linked list with optional intersection point."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    if intersection_node:
        current.next = intersection_node

    return head


def get_linked_list_values(head: ListNode) -> list:
    """Helper function to get values from linked list."""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def test_intersection():
    """Test function with various test cases."""
    solution = Solution()

    test_cases = [
        {
            "list_a": [4, 1, 8, 4, 5],
            "list_b": [5, 6, 1, 8, 4, 5],
            "intersection_index_a": 2,
            "description": "Basic case with intersection"
        },
        {
            "list_a": [1, 9, 1, 2, 4],
            "list_b": [3, 2, 4],
            "intersection_index_a": 3,
            "description": "Lists of different lengths"
        },
        {
            "list_a": [2, 6, 4],
            "list_b": [1, 5],
            "intersection_index_a": -1,
            "description": "No intersection"
        },
        {
            "list_a": [1],
            "list_b": [1],
            "intersection_index_a": 0,
            "description": "Single node intersection"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        # Create the intersection node if specified
        intersection_node = None
        if test_case["intersection_index_a"] >= 0:
            intersection_values = test_case["list_a"][test_case["intersection_index_a"]:]
            intersection_node = create_linked_list(intersection_values)

        # Create both lists
        list_a_values = test_case["list_a"][:test_case["intersection_index_a"]
                                            ] if test_case["intersection_index_a"] >= 0 else test_case["list_a"]
        list_b_values = test_case["list_b"][:-len(
            intersection_values)] if intersection_node else test_case["list_b"]

        headA = create_linked_list(list_a_values, intersection_node)
        headB = create_linked_list(list_b_values, intersection_node)

        # Find intersection
        result = solution.getIntersectionNode(headA, headB)

        # Verify result
        if test_case["intersection_index_a"] >= 0:
            assert result == intersection_node, \
                f'Test case {i} failed. Expected intersection at value {intersection_node.val}'
        else:
            assert result is None, \
                f'Test case {i} failed. Expected no intersection but got one'

        print(f'Test case {i} passed: {test_case["description"]}')

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_intersection()
