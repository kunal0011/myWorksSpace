"""
LeetCode 206 - Reverse Linked List

Problem Statement:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:
Input: head = [1->2->3->4->5]
Output: [5->4->3->2->1]

Solution Logic:
1. Use three pointers: prev, curr, and next_node
2. Initialize prev as None and curr as head
3. For each node:
   - Save next_node reference
   - Reverse the link (curr.next = prev)
   - Move prev and curr one step forward
4. Return prev as new head
Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # Store next node
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev to current node
            curr = next_node       # Move to next node

        return prev  # prev will be the new head of the reversed list

# Test cases
def test_reverse_list():
    # Test Case 1: Normal list
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    
    solution = Solution()
    reversed1 = solution.reverseList(head1)
    assert reversed1.val == 3
    assert reversed1.next.val == 2
    assert reversed1.next.next.val == 1
    assert reversed1.next.next.next == None
    
    # Test Case 2: Single node
    head2 = ListNode(1)
    reversed2 = solution.reverseList(head2)
    assert reversed2.val == 1
    assert reversed2.next == None
    
    # Test Case 3: Empty list
    head3 = None
    reversed3 = solution.reverseList(head3)
    assert reversed3 == None
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_reverse_list()
