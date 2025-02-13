"""
LeetCode 146. LRU Cache

Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity 
  from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put
"""

from typing import Optional, Dict, List, Tuple


class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.
        Time complexity: O(1)
        """
        self.capacity = capacity
        self.cache = {}  # key -> Node mapping

        # Initialize dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Get value for key if it exists.
        Time complexity: O(1)
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Put key-value pair into cache.
        Time complexity: O(1)
        """
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # Remove least recently used item (next to head)
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

    def _remove(self, node: Node) -> None:
        """Helper function to remove node from doubly linked list."""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node: Node) -> None:
        """Helper function to add node before tail (most recently used)."""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get_state(self) -> Tuple[List[Tuple[int, int]], List[int]]:
        """Helper function to get current cache state."""
        # Get items in order from most to least recently used
        items = []
        curr = self.tail.prev
        while curr != self.head:
            items.append((curr.key, curr.value))
            curr = curr.prev

        # Get keys in order
        keys = [item[0] for item in items]

        return items, keys


def test_lru_cache():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "operations": ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            "params": [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            "expected": [None, None, None, 1, None, -1, None, -1, 3, 4],
            "description": "Standard operations"
        },
        {
            "operations": ["LRUCache", "put", "get", "put", "get", "get"],
            "params": [[1], [2, 1], [2], [3, 2], [2], [3]],
            "expected": [None, None, 1, None, -1, 2],
            "description": "Capacity 1 cache"
        },
        {
            "operations": ["LRUCache", "put", "put", "put", "put", "get", "get"],
            "params": [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]],
            "expected": [None, None, None, None, None, -1, 3],
            "description": "Multiple updates"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")

        cache = None
        results = []

        for op, params in zip(test_case['operations'], test_case['params']):
            print(f"\nOperation: {op}{params}")

            if op == "LRUCache":
                cache = LRUCache(params[0])
                results.append(None)
                print(f"Initialized cache with capacity {params[0]}")
            elif op == "put":
                cache.put(params[0], params[1])
                results.append(None)
                items, keys = cache.get_state()
                print(f"After put({params[0]}, {params[1]}):")
                print(f"Cache items (MRU to LRU): {items}")
                print(f"Key order (MRU to LRU): {keys}")
            else:  # get
                result = cache.get(params[0])
                results.append(result)
                items, keys = cache.get_state()
                print(f"get({params[0]}) returned: {result}")
                print(f"Cache items (MRU to LRU): {items}")
                print(f"Key order (MRU to LRU): {keys}")

        # Verify results
        assert results == test_case['expected'], \
            f"Test failed. Expected {test_case['expected']}, got {results}"

        print("\n✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_lru_cache()
