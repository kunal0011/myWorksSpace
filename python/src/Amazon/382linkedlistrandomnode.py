"""
LeetCode 382: Linked List Random Node

Given a singly linked list, return a random node's value from the linked list. 
Each node must have the same probability of being chosen.

Implement the Solution class:
- Solution(ListNode head): Initializes the object with the head of the singly-linked list.
- int getRandom(): Returns a random node's value from the linked list.

Follow up:
- What if the linked list is extremely large and its length is unknown to you?
- Could you solve this efficiently without using extra space?

The solution uses Reservoir Sampling algorithm which is optimal when:
1. The size of the linked list is unknown
2. We want to give equal probability to each node
3. We can only traverse the list once
4. We want to use O(1) extra space

Time Complexity:
- Constructor: O(1)
- getRandom(): O(n) where n is the length of the list
Space Complexity: O(1)
"""

import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        """
        Initialize your data structure here.
        :param head: The head of the linked list
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value from the linked list using reservoir sampling.
        This ensures each node has equal probability of being selected.
        
        Returns:
            int: The value of the randomly selected node
        """
        if not self.head:
            return 0
            
        result = self.head.val
        current = self.head.next
        count = 1
        
        # Reservoir sampling algorithm
        while current:
            count += 1
            # Generate a random number in range [0, count)
            # If it's 0, update result (probability of 1/count)
            if random.randint(0, count - 1) == 0:
                result = current.val
            current = current.next
            
        return result


def create_linked_list(values: list) -> Optional[ListNode]:
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
        
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list:
    """Helper function to convert linked list to list for testing."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def run_test_cases() -> None:
    """Function to run comprehensive test cases"""
    
    # Test case 1: Basic case with distribution check
    print("\nTest Case 1: Distribution test with [1, 2, 3]")
    head1 = create_linked_list([1, 2, 3])
    solution = Solution(head1)
    
    # Test random distribution
    count = {1: 0, 2: 0, 3: 0}
    trials = 3000
    
    for _ in range(trials):
        val = solution.getRandom()
        count[val] += 1
    
    print("Random distribution after 3000 trials:")
    for num, freq in count.items():
        print(f"Number {num}: {freq/trials:.2%}")
    print(f"Expected distribution: ~33.33% each")
    
    # Test case 2: Single node
    print("\nTest Case 2: Single node [1]")
    head2 = create_linked_list([1])
    solution2 = Solution(head2)
    result2 = solution2.getRandom()
    print(f"Got: {result2}")
    print(f"Result: {'PASSED' if result2 == 1 else 'FAILED'}")
    
    # Test case 3: Empty list
    print("\nTest Case 3: Empty list")
    solution3 = Solution(None)
    result3 = solution3.getRandom()
    print(f"Got: {result3}")
    print(f"Result: {'PASSED' if result3 == 0 else 'FAILED'}")
    
    # Test case 4: Longer list distribution
    print("\nTest Case 4: Longer list [1, 2, 3, 4, 5]")
    head4 = create_linked_list([1, 2, 3, 4, 5])
    solution4 = Solution(head4)
    
    count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    trials = 5000
    
    for _ in range(trials):
        val = solution4.getRandom()
        count[val] += 1
    
    print("Random distribution after 5000 trials:")
    for num, freq in count.items():
        print(f"Number {num}: {freq/trials:.2%}")
    print(f"Expected distribution: ~20% each")


if __name__ == "__main__":
    run_test_cases()
