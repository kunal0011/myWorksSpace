"""
LeetCode 234 - Palindrome Linked List

Problem Statement:
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
Must solve it in O(n) time and O(1) space.

Solution Logic:
1. Find middle of list using slow/fast pointers
2. Reverse second half of list
3. Compare first half with reversed second half
4. Time: O(n), Space: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: Compare the first and second halves
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        # Step 4: Restore the list (optional, if required)
        # (Code to restore the list would go here)

        return True

def create_linked_list(values):
    """Helper function to create linked list from list of values."""
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    """Helper function to print linked list."""
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    return "->".join(values)

def test_palindrome():
    solution = Solution()
    
    # Test Case 1: Even length palindrome
    head1 = create_linked_list([1,2,2,1])
    print("Test 1: Even length palindrome")
    print(f"List: {print_linked_list(head1)}")
    print(f"Is palindrome: {solution.isPalindrome(head1)}")  # Expected: True
    
    # Test Case 2: Odd length palindrome
    head2 = create_linked_list([1,2,3,2,1])
    print("\nTest 2: Odd length palindrome")
    print(f"List: {print_linked_list(head2)}")
    print(f"Is palindrome: {solution.isPalindrome(head2)}")  # Expected: True
    
    # Test Case 3: Not a palindrome
    head3 = create_linked_list([1,2,3])
    print("\nTest 3: Not a palindrome")
    print(f"List: {print_linked_list(head3)}")
    print(f"Is palindrome: {solution.isPalindrome(head3)}")  # Expected: False
    
    # Test Case 4: Single node
    head4 = create_linked_list([1])
    print("\nTest 4: Single node")
    print(f"List: {print_linked_list(head4)}")
    print(f"Is palindrome: {solution.isPalindrome(head4)}")  # Expected: True

if __name__ == "__main__":
    test_palindrome()
