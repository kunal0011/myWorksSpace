# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Initialize two pointers, slow and fast
        slow = head
        fast = head

        # Move slow by 1 step and fast by 2 steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # When fast reaches the end, slow is at the middle
        return slow

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


# Test the Solution
if __name__ == "__main__":
    # Create linked list [1, 2, 3, 4, 5]
    head = create_linked_list([1, 2, 3, 4, 5])

    # Initialize Solution class and find the middle node
    solution = Solution()
    middle = solution.middleNode(head)

    # Print the linked list starting from the middle node
    print("Middle node and onwards:")
    print_linked_list(middle)
