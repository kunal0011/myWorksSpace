class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Node(float('-inf'))  # Dummy head with -∞ count
        self.tail = Node(float('inf'))   # Dummy tail with +∞ count
        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_count = {}  # Maps key to its frequency
        self.freq_node = {}  # Maps frequency to the corresponding node

    def _add_node(self, new_node, prev_node, next_node):
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.freq_node[node.count]

    def _move_key(self, key, old_node, new_node):
        old_node.keys.remove(key)
        if not old_node.keys:
            self._remove_node(old_node)
        new_node.keys.add(key)

    def inc(self, key: str) -> None:
        count = self.key_count.get(key, 0)
        self.key_count[key] = count + 1

        cur_node = self.freq_node.get(count)
        next_node = self.freq_node.get(count + 1)

        if not next_node:
            next_node = Node(count + 1)
            self.freq_node[count + 1] = next_node
            self._add_node(next_node, cur_node if cur_node else self.head,
                           cur_node.next if cur_node else self.head.next)

        if count > 0:
            self._move_key(key, cur_node, next_node)
        else:
            next_node.keys.add(key)

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return

        count = self.key_count[key]
        cur_node = self.freq_node[count]
        if count == 1:
            del self.key_count[key]
            cur_node.keys.remove(key)
            if not cur_node.keys:
                self._remove_node(cur_node)
            return

        self.key_count[key] = count - 1
        prev_node = self.freq_node.get(count - 1)
        if not prev_node:
            prev_node = Node(count - 1)
            self.freq_node[count - 1] = prev_node
            self._add_node(prev_node, cur_node.prev, cur_node)

        self._move_key(key, cur_node, prev_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
