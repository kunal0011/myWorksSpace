"""
LeetCode 432 - All O`one Data Structure

Problem Statement:
-----------------
Design a data structure to store the strings' count with the ability to return the strings 
with maximum and minimum counts.

Implement the AllOne class:
- AllOne() Initializes the object of the data structure.
- inc(String key) Increments the count of the string key by 1. If key doesn't exist, insert it with count 1.
- dec(String key) Decrements the count of the string key by 1. If the count becomes 0, remove the string.
- getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
- getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".

Key Points:
----------
1. All operations must run in O(1) average time complexity
2. Need to efficiently track both frequency counts and min/max values
3. Uses a combination of hash maps and doubly-linked list
4. Must handle edge cases (empty structure, single element, etc.)

Examples:
--------
Input:
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output:
[null, null, null, "hello", "hello", null, "hello", "leet"]

Constraints:
-----------
* 1 <= key.length <= 10
* key consists of lowercase English letters
* It's guaranteed that for each call to dec, key is existing in the data structure
* At most 5 * 10^4 calls will be made to inc, dec, getMaxKey, and getMinKey
"""

class Node:
    def __init__(self, count: int):
        """
        Initialize a node in the frequency list
        
        Args:
            count: The frequency count this node represents
        """
        self.count = count
        self.keys = set()  # Set of keys with this frequency
        self.prev = None   # Previous node in the doubly-linked list
        self.next = None   # Next node in the doubly-linked list


class AllOne:
    def __init__(self):
        """
        Initialize the All O`one data structure with dummy head and tail nodes
        """
        self.head = Node(float('-inf'))  # Dummy head with -∞ count
        self.tail = Node(float('inf'))   # Dummy tail with +∞ count
        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_count = {}    # Maps key to its frequency
        self.freq_node = {}    # Maps frequency to the corresponding node

    def _add_node(self, new_node: Node, prev_node: Node, next_node: Node) -> None:
        """Helper method to add a node between prev_node and next_node"""
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node

    def _remove_node(self, node: Node) -> None:
        """Helper method to remove a node from the list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.freq_node[node.count]

    def _move_key(self, key: str, old_node: Node, new_node: Node) -> None:
        """Helper method to move a key from old_node to new_node"""
        old_node.keys.remove(key)
        if not old_node.keys:
            self._remove_node(old_node)
        new_node.keys.add(key)

    def inc(self, key: str) -> None:
        """
        Increment the count for a key by 1
        Time Complexity: O(1)
        """
        count = self.key_count.get(key, 0)
        self.key_count[key] = count + 1

        cur_node = self.freq_node.get(count)
        next_node = self.freq_node.get(count + 1)

        if not next_node:
            next_node = Node(count + 1)
            self.freq_node[count + 1] = next_node
            self._add_node(next_node, 
                          cur_node if cur_node else self.head,
                          cur_node.next if cur_node else self.head.next)

        if count > 0:
            self._move_key(key, cur_node, next_node)
        else:
            next_node.keys.add(key)

    def dec(self, key: str) -> None:
        """
        Decrement the count for a key by 1
        Time Complexity: O(1)
        """
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
        """
        Get any key with maximum frequency
        Time Complexity: O(1)
        """
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        """
        Get any key with minimum frequency
        Time Complexity: O(1)
        """
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))


def test_all_one():
    """
    Test driver for the AllOne data structure
    """
    test_cases = [
        # Test case 1: Basic operations
        {
            'operations': ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"],
            'inputs': [[], ["hello"], ["hello"], [], [], ["leet"], [], []],
            'expected': [None, None, None, "hello", "hello", None, "hello", "leet"]
        },
        # Test case 2: Decrement operations
        {
            'operations': ["AllOne", "inc", "inc", "inc", "dec", "getMaxKey", "getMinKey"],
            'inputs': [[], ["hello"], ["world"], ["hello"], ["hello"], [], []],
            'expected': [None, None, None, None, None, "hello", "world"]
        },
        # Test case 3: Empty structure
        {
            'operations': ["AllOne", "getMaxKey", "getMinKey"],
            'inputs': [[], [], []],
            'expected': [None, "", ""]
        },
        # Test case 4: Multiple frequencies
        {
            'operations': ["AllOne", "inc", "inc", "inc", "inc", "inc", "dec", "getMaxKey", "getMinKey"],
            'inputs': [[], ["a"], ["b"], ["b"], ["b"], ["a"], ["b"], [], []],
            'expected': [None, None, None, None, None, None, None, "b", "a"]
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Running test case {i}...")
        obj = AllOne()
        results = []
        
        for op, inp in zip(test_case['operations'], test_case['inputs']):
            if op == "AllOne":
                results.append(None)
            elif op == "inc":
                results.append(obj.inc(inp[0]))
            elif op == "dec":
                results.append(obj.dec(inp[0]))
            elif op == "getMaxKey":
                results.append(obj.getMaxKey())
            elif op == "getMinKey":
                results.append(obj.getMinKey())
        
        status = "PASSED" if results == test_case['expected'] else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Operations: {test_case['operations']}")
        print(f"Inputs: {test_case['inputs']}")
        print(f"Expected: {test_case['expected']}")
        print(f"Got: {results}")
        print("-" * 40)

if __name__ == "__main__":
    test_all_one()
