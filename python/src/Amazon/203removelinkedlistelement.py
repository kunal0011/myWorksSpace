# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next

# Helper function to create linked list from Python list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to Python list for easy comparison
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
def test_remove_elements():
    sol = Solution()

    # Test Case 1
    head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
    val = 6
    new_head = sol.removeElements(head, val)
    assert linked_list_to_list(new_head) == [
        1, 2, 3, 4, 5], "Test Case 1 Failed"

    # Test Case 2
    head = create_linked_list([7, 7, 7, 7])
    val = 7
    new_head = sol.removeElements(head, val)
    assert linked_list_to_list(new_head) == [], "Test Case 2 Failed"

    # Test Case 3
    head = create_linked_list([1, 2, 3])
    val = 4
    new_head = sol.removeElements(head, val)
    assert linked_list_to_list(new_head) == [1, 2, 3], "Test Case 3 Failed"

    # Test Case 4
    head = create_linked_list([])
    val = 1
    new_head = sol.removeElements(head, val)
    assert linked_list_to_list(new_head) == [], "Test Case 4 Failed"

    print("All test cases passed!")

# Run the tests
test_remove_elements()
