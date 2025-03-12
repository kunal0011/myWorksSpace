"""
LeetCode 445 - Add Two Numbers II

Problem Statement:
-----------------
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Key Points:
----------
1. Numbers are stored in forward order (most significant digit first)
2. Need to add numbers from right to left (least significant digit first)
3. No leading zeros except for number 0
4. Use stack to handle reverse order addition
5. Handle carry properly

Examples:
--------
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Explanation: 7243 + 564 = 7807

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Explanation: 243 + 564 = 807

Constraints:
-----------
* The number of nodes in each linked list is in the range [1, 100]
* 0 <= Node.val <= 9
* It is guaranteed that the list represents a number that does not have leading zeros.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        """Initialize a node of the linked list"""
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Add two numbers represented by linked lists in forward order.
        
        Algorithm:
        1. Use two stacks to store digits from both lists
        2. Process digits from right to left using stacks
        3. Create new nodes for sum digits in reverse
        4. Handle carry properly
        
        Time Complexity: O(max(N,M)) where N,M are lengths of lists
        Space Complexity: O(N+M) for the stacks
        """
        # Stacks to store digits in reverse order
        stack1, stack2 = [], []

        # Push all digits of l1 to stack1
        curr = l1
        while curr:
            stack1.append(curr.val)
            curr = curr.next

        # Push all digits of l2 to stack2
        curr = l2
        while curr:
            stack2.append(curr.val)
            curr = curr.next

        carry = 0
        head = None

        # Process digits from right to left
        while stack1 or stack2 or carry:
            # Get digits from stacks or use 0 if stack is empty
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create new node and add to front of result
            new_node = ListNode(total % 10)
            new_node.next = head
            head = new_node

        return head


def create_linked_list(nums):
    """Helper function to create linked list from array"""
    if not nums:
        return None
    head = ListNode(nums[0])
    curr = head
    for num in nums[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head

def linked_list_to_array(head):
    """Helper function to convert linked list to array"""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def test_add_two_numbers():
    """
    Test driver for adding two numbers represented as linked lists
    """
    test_cases = [
        (
            [7,2,4,3], [5,6,4],
            [7,8,0,7]  # 7243 + 564 = 7807
        ),
        (
            [2,4,3], [5,6,4],
            [8,0,7]  # 243 + 564 = 807
        ),
        (
            [0], [0],
            [0]  # 0 + 0 = 0
        ),
        (
            [9,9,9,9], [1],
            [1,0,0,0,0]  # 9999 + 1 = 10000
        ),
        (
            [1], [9,9,9,9],
            [1,0,0,0,0]  # 1 + 9999 = 10000
        ),
        (
            [5], [5],
            [1,0]  # 5 + 5 = 10
        ),
        (
            [2,4,6,8], [5,7,9],
            [3,0,4,7]  # 2468 + 579 = 3047
        ),
        (
            [1,2,3,4,5], [6,7,8,9],
            [1,9,1,3,4]  # 12345 + 6789 = 19134
        )
    ]
    
    solution = Solution()
    
    for i, (nums1, nums2, expected) in enumerate(test_cases, 1):
        l1 = create_linked_list(nums1)
        l2 = create_linked_list(nums2)
        result = solution.addTwoNumbers(l1, l2)
        result_array = linked_list_to_array(result)
        status = "PASSED" if result_array == expected else "FAILED"
        
        print(f"Test case {i}: {status}")
        print(f"Input numbers: {nums1} + {nums2}")
        print(f"Expected: {expected}")
        print(f"Got: {result_array}")
        print("-" * 40)

if __name__ == "__main__":
    test_add_two_numbers()
