"""
LeetCode 677: Map Sum Pairs

Problem Statement:
Design a map that allows you to do the following:
- insert a (key, value) pair into the map
- return the sum of values of all keys that start with a given prefix

Example:
Input: 
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output: [null, null, 3, null, 5]

Logic:
1. Use a combination of HashMap and Trie data structure
2. HashMap stores the actual key-value pairs
3. Trie stores the running sum at each node for prefix calculations
4. For insert: Calculate difference with existing value and update all prefix sums
5. For sum: Traverse to the prefix node and return its sum

Time Complexity:
- Insert: O(k) where k is the length of the key
- Sum: O(p) where p is the length of the prefix

Space Complexity: O(T) where T is the total length of all keys
"""


class MapSum:
    def __init__(self):
        self.map = {}  # Dictionary to store key-value pairs
        self.trie = {}  # Trie to store the prefix sums

    def insert(self, key: str, val: int) -> None:
        # Get the difference if key already exists
        diff = val - self.map.get(key, 0)
        self.map[key] = val  # Update the map with the new value

        # Insert into the trie
        cur = self.trie
        for c in key:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
            # Update the sum at each node
            cur['#'] = cur.get('#', 0) + diff

    def sum(self, prefix: str) -> int:
        cur = self.trie

        # Traverse the trie using the prefix
        for c in prefix:
            if c not in cur:
                return 0  # Prefix not found
            cur = cur[c]

        # Return the sum stored at the last node of the prefix
        return cur.get('#', 0)

# Test driver


def test_map_sum():
    # Test case 1: Basic functionality
    print("Test Case 1:")
    map_sum = MapSum()
    map_sum.insert("apple", 3)
    print("Sum of prefix 'ap':", map_sum.sum("ap"))  # Expected: 3
    map_sum.insert("app", 2)
    print("Sum of prefix 'ap':", map_sum.sum("ap"))  # Expected: 5

    # Test case 2: Updating existing key
    print("\nTest Case 2:")
    map_sum = MapSum()
    map_sum.insert("apple", 3)
    print("Sum of prefix 'ap':", map_sum.sum("ap"))  # Expected: 3
    map_sum.insert("apple", 2)  # Update value
    print("Sum of prefix 'ap':", map_sum.sum("ap"))  # Expected: 2

    # Test case 3: Multiple prefixes
    print("\nTest Case 3:")
    map_sum = MapSum()
    map_sum.insert("apple", 3)
    map_sum.insert("app", 2)
    map_sum.insert("apricot", 5)
    print("Sum of prefix 'ap':", map_sum.sum("ap"))  # Expected: 10
    print("Sum of prefix 'apr':", map_sum.sum("apr"))  # Expected: 5


if __name__ == "__main__":
    test_map_sum()
