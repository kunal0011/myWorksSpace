class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> list[ListNode]:
        # Count the length of the linked list
        current = root
        total_length = 0
        while current:
            total_length += 1
            current = current.next

        # Determine the size of each part
        part_length = total_length // k  # Minimum size of each part
        remainder = total_length % k     # Extra nodes to distribute

        # Split the linked list
        result = []
        current = root

        for i in range(k):
            head = current
            # Add one more node to the first 'remainder' parts
            size = part_length + (1 if i < remainder else 0)
            for j in range(size - 1):
                if current:
                    current = current.next
            if current:
                # Split the current part from the rest
                next_part, current.next = current.next, None
                current = next_part
            result.append(head)

        return result

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


# Test the function
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    root1 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k1 = 3
    parts1 = sol.splitListToParts(root1, k1)
    for part in parts1:
        # Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
        print(linked_list_to_list(part))

    # Test case 2
    root2 = create_linked_list([1, 2])
    k2 = 5
    parts2 = sol.splitListToParts(root2, k2)
    for part in parts2:
        print(linked_list_to_list(part))  # Output: [[1], [2], [], [], []]
