"""
LeetCode 382 - Linked List Random Node

Problem Statement:
Given a singly linked list, return a random node's value from the linked list. 
Each node must have the same probability of being chosen.

Implement the Solution class:
- Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
- int getRandom() Returns a random node's value from the linked list.

The solution uses Reservoir Sampling algorithm which allows us to randomly select k items 
from a list of n items, where n is either a very large or unknown number.

Time Complexity: 
- Constructor: O(1)
- getRandom: O(n)
Space Complexity: O(1)
"""

import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        Uses Reservoir Sampling algorithm.
        """
        scope = 1
        chosen_value = 0
        current = self.head
        
        while current:
            # Randomly replace answer with current value with probability 1/scope
            if random.randint(1, scope) == 1:
                chosen_value = current.val
            current = current.next
            scope += 1
            
        return chosen_value


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def test_linked_list_random():
    # Test cases
    test_cases = [
        [1, 2, 3],
        [1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ]
    
    for i, nums in enumerate(test_cases, 1):
        print(f"\nTest case {i}:")
        print(f"Linked List: {nums}")
        
        # Create linked list
        head = create_linked_list(nums)
        solution = Solution(head)
        
        # Test random selection
        # Run multiple times to verify randomness
        frequency = {}
        trials = 10000
        
        for _ in range(trials):
            val = solution.getRandom()
            frequency[val] = frequency.get(val, 0) + 1
        
        print("Frequency distribution after 10000 trials:")
        expected_freq = trials / len(nums)
        for num in nums:
            actual_freq = frequency.get(num, 0)
            print(f"Value {num}: {actual_freq} times " + 
                  f"({actual_freq/trials*100:.1f}% vs expected {100/len(nums):.1f}%)")


if __name__ == "__main__":
    test_linked_list_random()