import random

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: ListNode):
        # Initialize with the head of the linked list
        self.head = head

    def getRandom(self) -> int:
        # Reservoir sampling algorithm
        result, node, i = 0, self.head, 0

        while node:
            i += 1
            # Select the current node with probability 1/i
            if random.randint(1, i) == 1:
                result = node.val
            node = node.next

        return result
