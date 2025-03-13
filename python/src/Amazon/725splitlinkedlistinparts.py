"""
LeetCode 725: Split Linked List in Parts

Given the head of a singly linked list and an integer k, split the linked list into k consecutive parts.

The length of each part should be as equal as possible: no two parts should have a size differing by 
more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should 
always have a size greater than or equal to parts occurring later.

Return an array of the k parts.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> list[ListNode]:
        # Optimized length calculation using single pass
        length = 0
        curr = root
        while curr:
            length += 1
            curr = curr.next

        base_size, extra = divmod(length, k)
        curr = root
        parts = []

        for i in range(k):
            if not curr:
                parts.append(None)
                continue

            parts.append(curr)
            # Calculate size for current part
            current_size = base_size + (1 if i < extra else 0)
            
            # Move to the end of current part
            for _ in range(current_size - 1):
                curr = curr.next
            
            # Disconnect the part
            next_start = curr.next
            curr.next = None
            curr = next_start

        return parts

# Helper function to create a linked list from a list of values
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def print_linked_list(node: ListNode) -> str:
    """Helper function to convert linked list to string representation"""
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    return '->'.join(values) if values else 'None'

# Enhanced test driver
def run_tests():
    solution = Solution()
    test_cases = [
        # Test case 1: Even distribution with remainder
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3),
        # Test case 2: More parts than elements
        ([1, 2, 3], 5),
        # Test case 3: Empty list
        ([], 3),
        # Test case 4: Single element
        ([1], 3),
        # Test case 5: Equal distribution
        ([1, 2, 3, 4], 2)
    ]

    for i, (values, k) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: list = {values}, k = {k}")
        
        # Create input linked list
        head = create_linked_list(values)
        
        # Get result
        result = solution.splitListToParts(head, k)
        
        # Print result
        print("Output parts:")
        for j, part in enumerate(result):
            print(f"Part {j + 1}: {print_linked_list(part)}")
        
        # Verify parts count
        assert len(result) == k, f"Expected {k} parts, got {len(result)}"
        
        # Verify total elements
        total_elements = sum(1 for part in result if part is not None)
        assert total_elements == len(values), "Total elements mismatch"

if __name__ == "__main__":
    run_tests()
