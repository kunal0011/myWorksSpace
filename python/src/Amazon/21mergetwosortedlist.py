class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Initialize a dummy node
        dummy = ListNode()
        current = dummy

        # Iterate while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining part of list1 or list2
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list starting from the node after dummy
        return dummy.next

# Example usage:
# (Assume ListNode class and helper functions to create linked lists are defined)


def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# Create example lists
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)
print_linked_list(merged_list)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
