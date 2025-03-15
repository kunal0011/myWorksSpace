"""
LeetCode 876: Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Constraints:
- The number of nodes in the list is in the range [1, 100]
- 1 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
            
        # Floyd's Tortoise and Hare algorithm
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

def validate_list(head: ListNode) -> bool:
    """Validate linked list according to constraints"""
    count = 0
    current = head
    while current:
        if not 1 <= current.val <= 100:
            return False
        count += 1
        if count > 100:
            return False
        current = current.next
    return count >= 1

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print the linked list from a given node
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)

def test_middle_node():
    """Test function for Middle of Linked List"""
    test_cases = [
        ([1,2,3,4,5], [3,4,5]),
        ([1,2,3,4,5,6], [4,5,6]),
        ([1], [1]),
        ([1,2], [2]),
        ([1,2,3], [2,3]),
        ([1,2,3,4,5,6,7], [4,5,6,7])
    ]
    
    solution = Solution()
    
    for i, (input_list, expected) in enumerate(test_cases, 1):
        head = create_linked_list(input_list)
        is_valid = validate_list(head)
        result = solution.middleNode(head)
        result_list = []
        current = result
        while current:
            result_list.append(current.val)
            current = current.next
            
        print(f"\nTest case {i}:")
        print(f"Input list: {input_list}")
        print(f"List length: {len(input_list)}")
        print(f"Middle index: {(len(input_list)-1)//2}")
        print(f"Expected from middle: {expected}")
        print(f"Got from middle: {result_list}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result_list == expected else '✗'}")

if __name__ == "__main__":
    test_middle_node()
