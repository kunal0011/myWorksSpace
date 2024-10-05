class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # Create dummy head and tail nodes for the doubly linked list
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._move_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.hashmap) == self.capacity:
                self._evict_least_recently_used()
            new_node = ListNode(key, value)
            self.hashmap[key] = new_node
            self._add_to_front(new_node)

    def _move_to_front(self, node: ListNode) -> None:
        # Remove node from its current position
        self._remove_node(node)
        # Add node to the front of the doubly linked list
        self._add_to_front(node)

    def _add_to_front(self, node: ListNode) -> None:
        # Adjust pointers to insert node after dummy head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: ListNode) -> None:
        # Adjust pointers to remove node from the doubly linked list
        node.prev.next = node.next
        node.next.prev = node.prev

    def _evict_least_recently_used(self) -> None:
        # Remove tail.prev from hashmap and doubly linked list
        del self.hashmap[self.tail.prev.key]
        self._remove_node(self.tail.prev)
