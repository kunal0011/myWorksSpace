import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        # Initialize result and counter
        result, current, count = -1, self.head, 0

        # Traverse the linked list
        while current:
            count += 1
            # Replace the result with current node's value with probability 1/count
            if random.randint(1, count) == count:
                result = current.val
            current = current.next

        return result


# Test cases
if __name__ == "__main__":
    # Create linked list: 1 -> 2 -> 3
    head = ListNode(1, ListNode(2, ListNode(3)))

    # Initialize solution
    sol = Solution(head)

    # Call getRandom multiple times to see random behavior
    for _ in range(5):
        print(sol.getRandom())  # Should randomly print 1, 2, or 3 each time
