# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode):
        # Convert Linked List to a List (array)
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        # This will store the result
        result = [0] * len(values)

        # Stack to keep track of indices whose next greater element hasn't been found yet
        stack = []

        # Traverse through the values list
        for i in range(len(values)):
            # If stack is not empty and current value is greater than the value at the index stored in the stack
            while stack and values[i] > values[stack[-1]]:
                # Pop from the stack and update the result for that index
                index = stack.pop()
                result[index] = values[i]
            # Push current index to the stack
            stack.append(i)

        return result

# Helper function to create a linked list from a list


def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print the linked list


def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)


# Test the Solution
if __name__ == "__main__":
    # Create linked list [2, 1, 5]
    head = create_linked_list([2, 1, 5])

    # Initialize Solution class and find next greater nodes
    solution = Solution()
    result = solution.nextLargerNodes(head)

    # Print the result
    print("Next greater nodes:", result)
