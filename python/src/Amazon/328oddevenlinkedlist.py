"""
LeetCode 328 - Odd Even Linked List

Problem Statement:
Given the head of a singly linked list, group all the nodes with odd indices together 
followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.

Logic:
1. Use two pointers approach:
   - odd pointer for nodes at odd positions
   - even pointer for nodes at even positions
2. Key steps:
   - Save head of even list
   - Connect odd nodes together
   - Connect even nodes together
   - Connect end of odd list to head of even list
3. Time: O(n), Space: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Initialize pointers for odd and even nodes
        odd = head
        even = head.next
        even_head = even  # Keep the head of the even list

        # Rearrange nodes
        while even and even.next:
            odd.next = even.next  # Connect odd nodes
            odd = odd.next  # Move odd pointer forward
            even.next = odd.next  # Connect even nodes
            even = even.next  # Move even pointer forward

        # Connect the end of odd list to the head of even list
        odd.next = even_head

        return head

def test_odd_even_list():
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def linked_list_to_array(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1,2,3,4,5], [1,3,5,2,4]),      # Odd length list
        ([2,1,3,5,6,4,7], [2,3,6,7,1,5,4]), # Even length list
        ([1], [1]),                       # Single node
        ([], []),                         # Empty list
        ([1,2], [1,2])                    # Two nodes
    ]
    
    for i, (values, expected) in enumerate(test_cases):
        head = create_linked_list(values)
        result = solution.oddEvenList(head)
        result_array = linked_list_to_array(result)
        assert result_array == expected, \
            f"Test case {i + 1} failed: expected {expected}, got {result_array}"
        print(f"Test case {i + 1} passed:")
        print(f"Input: {values}")
        print(f"Output: {result_array}\n")

if __name__ == "__main__":
    test_odd_even_list()
    print("All test cases passed!")
