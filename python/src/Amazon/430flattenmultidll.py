# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # Helper function to flatten the list and return the tail of the flattened list
        def flatten_dfs(node):
            curr = node
            last = None

            while curr:
                next_node = curr.next

                # If there's a child, we need to flatten it
                if curr.child:
                    # Flatten the child list
                    child_tail = flatten_dfs(curr.child)

                    # Insert the flattened child between curr and next_node
                    curr.next = curr.child
                    curr.child.prev = curr
                    curr.child = None

                    # If there was a next node, connect the child tail to it
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail

                    last = child_tail
                else:
                    last = curr

                curr = next_node

            return last

        # Start flattening from the head
        flatten_dfs(head)
        return head

# Example usage


def print_list(head):
    curr = head
    while curr:
        print(f"Node({curr.val})", end=" -> ")
        curr = curr.next
    print("None")


# Example: Creating a multilevel doubly linked list
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.child = node7
node7.next = node8
node8.prev = node7
node8.child = node9
node9.next = node10
node10.prev = node9
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4
node5.next = node6
node6.prev = node5

# Flatten the list
solution = Solution()
solution.flatten(node1)

# Print the flattened list
# Expected output: 1 -> 2 -> 3 -> 7 -> 8 -> 9 -> 10 -> 4 -> 5 -> 6 -> None
print_list(node1)
