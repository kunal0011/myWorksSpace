"""
LeetCode 369 - Plus One Linked List

Problem Statement:
Given a non-negative integer represented as a linked list of digits, plus one to the number.
The digits are stored in reverse order, and each of their nodes contains a single digit.
The most significant digit is at the tail of the linked list.
Return the head of the linked list after adding one.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # Step 1: Reverse the linked list
        def reverseList(node):
            prev = None
            curr = node
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev
        
        # Step 2: Add one to the number
        def addOne(node):
            curr = node
            carry = 1
            
            while curr and carry:
                val = curr.val + carry
                curr.val = val % 10
                carry = val // 10
                
                if carry and not curr.next:
                    curr.next = ListNode(0)
                curr = curr.next
            
            return node
        
        # Main process
        # First reverse
        reversed_head = reverseList(head)
        # Add one
        result = addOne(reversed_head)
        # Reverse back
        return reverseList(result)


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
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

def test_plus_one():
    solution = Solution()
    
    # Test cases
    test_cases = [
        [1,2,3],       # 123 + 1 = 124
        [4,3,2,1],     # 1234 + 1 = 1235
        [9],           # 9 + 1 = 10
        [9,9,9],       # 999 + 1 = 1000
        [0],           # 0 + 1 = 1
    ]
    
    for i, nums in enumerate(test_cases, 1):
        # Create linked list
        head = create_linked_list(nums)
        
        # Calculate expected result
        expected = str(int(''.join(map(str, nums[::-1]))) + 1)
        expected = list(map(int, expected[::-1]))
        
        # Get actual result
        result = solution.plusOne(head)
        result_arr = linked_list_to_array(result)
        
        print(f"Test case {i}:")
        print(f"Input number: {''.join(map(str, nums[::-1]))}")
        print(f"Expected: {''.join(map(str, expected[::-1]))}")
        print(f"Got: {''.join(map(str, result_arr[::-1]))}")
        print(f"Pass: {result_arr == expected}\n")


if __name__ == "__main__":
    test_plus_one()