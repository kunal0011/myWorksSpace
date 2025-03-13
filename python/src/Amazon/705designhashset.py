"""
LeetCode 705: Design HashSet

Design a HashSet without using any built-in hash table libraries.
Implement MyHashSet class:
- void add(key): Inserts the value key into the HashSet.
- bool contains(key): Returns whether the value key exists in the HashSet or not.
- void remove(key): Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Constraints:
- 0 <= key <= 10^6
- At most 10^4 calls will be made to add, remove, and contains
"""

class MyHashSet:
    def __init__(self):
        self.size = 1031  # Prime number for better distribution
        self.buckets = [[] for _ in range(self.size)]
    
    def _hash(self, key: int) -> int:
        return key % self.size
    
    def add(self, key: int) -> None:
        hash_key = self._hash(key)
        if not self.contains(key):
            self.buckets[hash_key].append(key)
    
    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        try:
            bucket.remove(key)
        except ValueError:
            pass
    
    def contains(self, key: int) -> bool:
        hash_key = self._hash(key)
        return key in self.buckets[hash_key]

def test_hash_set():
    """Test driver for MyHashSet implementation"""
    test_cases = [
        {
            'operations': ['add', 'add', 'contains', 'contains', 'add', 'contains', 'remove', 'contains'],
            'values': [1, 2, 1, 3, 2, 2, 2, 2],
            'expected': [None, None, True, False, None, True, None, False],
            'description': 'Basic operations'
        },
        {
            'operations': ['add', 'remove', 'contains'],
            'values': [1000000, 1000000, 1000000],
            'expected': [None, None, False],
            'description': 'Large numbers'
        },
        {
            'operations': ['add', 'add', 'add', 'contains', 'remove', 'contains'],
            'values': [1, 1, 1, 1, 1, 1],
            'expected': [None, None, None, True, None, False],
            'description': 'Duplicate operations'
        }
    ]

    for i, case in enumerate(test_cases, 1):
        print(f"\nTest case {i}: {case['description']}")
        hash_set = MyHashSet()
        
        for op, val, exp in zip(case['operations'], case['values'], case['expected']):
            if op == 'add':
                hash_set.add(val)
                print(f"Added {val}")
            elif op == 'remove':
                hash_set.remove(val)
                print(f"Removed {val}")
            elif op == 'contains':
                result = hash_set.contains(val)
                print(f"Contains {val}: expected {exp}, got {result}")
                assert result == exp, f"Failed: Expected {exp}, got {result}"
        
        print(f"✓ Test case {i} passed")

if __name__ == "__main__":
    test_hash_set()
