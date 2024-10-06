class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Step 1: Create a new node for each original node and insert it after the original node
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Step 2: Assign random pointers for the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the original and copied nodes
        current = head
        copy_head = head.next
        while current:
            copy_node = current.next
            current.next = copy_node.next
            if copy_node.next:
                copy_node.next = copy_node.next.next
            current = current.next

        return copy_head
