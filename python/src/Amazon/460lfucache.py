"""
LeetCode 460 - LFU Cache (Least Frequently Used Cache)

Problem Statement:
-----------------
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
- LFUCache(int capacity) Initializes the object with the capacity of the data structure
- int get(int key) Gets the value of the key if it exists, otherwise returns -1
- void put(int key, int value) Updates the value of the key if present, or inserts the key
  if not already present. When the cache reaches its capacity, it should invalidate and 
  remove the least frequently used key before inserting a new item.

For the purpose of this problem, when there is a tie (i.e., two or more keys with the same
frequency), the least recently used key should be invalidated.

Key Points:
----------
1. Maintain frequency count for each key
2. Handle capacity constraints
3. Update frequency on both get and put operations
4. Break ties using LRU policy
5. O(1) time complexity for all operations

Examples:
--------
Input:
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation:
// capacity = 2
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_]
lfu.put(2, 2);   // cache=[2,1]
lfu.get(1);      // return 1, cache=[1,2]
lfu.put(3, 3);   // evicts key 2, cache=[3,1]
lfu.get(2);      // returns -1 (not found)
lfu.get(3);      // returns 3, cache=[3,1]
lfu.put(4, 4);   // evicts key 1, cache=[4,3]
lfu.get(1);      // returns -1 (not found)
lfu.get(3);      // returns 3, cache=[3,4]
lfu.get(4);      // returns 4, cache=[4,3]

Constraints:
-----------
* 0 <= capacity <= 10^4
* 0 <= key <= 10^5
* 0 <= value <= 10^9
* At most 2 * 10^5 calls will be made to get and put
"""

from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        """
        Initialize LFU Cache with given capacity.
        
        Time Complexity: O(1)
        Space Complexity: O(capacity) for storing cache items
        """
        self.capacity = capacity
        self.min_freq = 0  # Track minimum frequency for O(1) eviction
        self.key_to_val = {}  # Key to value mapping
        self.key_to_freq = {}  # Key to frequency mapping
        # Frequency to ordered dictionary of keys mapping
        # OrderedDict maintains insertion order for LRU within same frequency
        self.freq_to_keys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        """
        Get value by key if it exists, else return -1.
        Also updates access frequency.
        
        Time Complexity: O(1)
        """
        if key not in self.key_to_val:
            return -1
            
        val = self.key_to_val[key]
        self.update_freq(key)  # Increase frequency on access
        return val

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.
        Handles capacity constraints and updates frequencies.
        
        Time Complexity: O(1)
        """
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            # Update existing key
            self.key_to_val[key] = value
            self.update_freq(key)
        else:
            # Handle capacity constraints
            if len(self.key_to_val) >= self.capacity:
                self.evict()
                
            # Insert new key-value pair
            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = None
            self.min_freq = 1

    def update_freq(self, key: int) -> None:
        """
        Update frequency of a key after access.
        Maintains min_freq for O(1) eviction.
        
        Time Complexity: O(1)
        """
        freq = self.key_to_freq[key]
        
        # Remove from current frequency list
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1
                
        # Add to new frequency list
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = None

    def evict(self) -> None:
        """
        Evict least frequently used item.
        Uses min_freq for O(1) access to lowest frequency items.
        
        Time Complexity: O(1)
        """
        # Get least recently used key among least frequent items
        key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
        
        # Remove key from all mappings
        del self.key_to_val[key]
        del self.key_to_freq[key]
        
        # Clean up empty frequency list
        if not self.freq_to_keys[self.min_freq]:
            del self.freq_to_keys[self.min_freq]


def test_lfu_cache():
    """
    Comprehensive test driver for LFU Cache implementation
    """
    test_cases = [
        (
            # Basic operations
            ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, 3, None, -1, 3, 4]
        ),
        (
            # Empty cache
            ["LFUCache", "put", "get"],
            [[0], [0, 0], [0]],
            [None, None, -1]
        ),
        (
            # Single item cache
            ["LFUCache", "put", "get", "put", "get", "get"],
            [[1], [2, 1], [2], [3, 2], [2], [3]],
            [None, None, 1, None, -1, 2]
        ),
        (
            # Frequency tie-breaking with LRU
            ["LFUCache", "put", "put", "put", "put", "get", "get"],
            [[2], [1, 1], [2, 2], [1, 3], [3, 3], [1], [2]],
            [None, None, None, None, None, 3, -1]
        ),
        (
            # Multiple frequency levels
            ["LFUCache", "put", "get", "get", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [1], [1], [1], [2, 2], [2], [1], [2]],
            [None, None, 1, 1, 1, None, 2, 1, 2]
        )
    ]
    
    for i, (operations, inputs, expected) in enumerate(test_cases, 1):
        print(f"Running test case {i}...")
        cache = None
        
        for j, (op, exp) in enumerate(zip(operations, expected)):
            if op == "LFUCache":
                cache = LFUCache(inputs[j][0])
                print(f"Created cache with capacity {inputs[j][0]}")
            elif op == "put":
                key, value = inputs[j]
                cache.put(key, value)
                print(f"put({key}, {value})")
            else:  # get
                key = inputs[j][0]
                result = cache.get(key)
                assert result == exp, f"get({key}): Expected {exp}, but got {result}"
                print(f"get({key}) -> {result}")
        
        print("Test case PASSED")
        print("-" * 40)

if __name__ == "__main__":
    test_lfu_cache()
