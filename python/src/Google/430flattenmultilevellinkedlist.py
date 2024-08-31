class Node:
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        # Initialize a stack
        stack = []
        current = head

        while current:
            if current.child:
                # If current node has a next, push it onto the stack
                if current.next:
                    stack.append(current.next)

                # Link current node's next to its child and update child's prev pointer
                current.next = current.child
                current.child.prev = current
                current.child = None

            # If we reach the end of the current level and there's something on the stack
            if not current.next and stack:
                # Pop the stack and continue with the next node
                current.next = stack.pop()
                current.next.prev = current

            # Move to the next node
            current = current.next

        return head
