"""
LeetCode 981: Time Based Key-Value Store

Design a time-based key-value data structure that can store multiple values for the same key 
at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the data structure
- void set(String key, String value, int timestamp) Stores key with value at the given timestamp
- String get(String key, int timestamp) Returns value for key at timestamp, or "" if none

All timestamps of set are strictly increasing.

Constraints:
- 1 <= key.length, value.length <= 100
- key and value consist of lowercase English letters and digits
- 1 <= timestamp <= 10^7
- At most 2 * 10^5 calls will be made to set and get
"""

from collections import defaultdict
from typing import List, Tuple
from time import perf_counter

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)
        self.calls = 0  # Track number of calls for validation
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        """Store key-value pair at timestamp"""
        self.calls += 1
        if not self._validate_input(key, value, timestamp):
            return
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        """Get value for key at or before timestamp"""
        self.calls += 1
        values = self.store[key]
        if not values:
            return ""
            
        # Binary search for timestamp
        left, right = 0, len(values)
        while left < right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
                
        return values[left - 1][1] if left > 0 else ""
    
    def _validate_input(self, key: str, value: str = "", timestamp: int = 0) -> bool:
        """Validate input according to constraints"""
        if not (1 <= len(key) <= 100 and (not value or 1 <= len(value) <= 100)):
            return False
        if not key.isalnum() or (value and not value.isalnum()):
            return False
        if not 1 <= timestamp <= 10**7:
            return False
        if self.calls > 2 * 10**5:
            return False
        return True

def test_time_map():
    """Test function for TimeMap"""
    test_cases = [
        [
            ("set", "foo", "bar", 1),
            ("get", "foo", None, 1, "bar"),
            ("get", "foo", None, 3, "bar"),
            ("set", "foo", "bar2", 4),
            ("get", "foo", None, 4, "bar2"),
            ("get", "foo", None, 5, "bar2"),
        ],
        [
            ("set", "love", "high", 10),
            ("set", "love", "low", 20),
            ("get", "love", None, 5, ""),
            ("get", "love", None, 10, "high"),
            ("get", "love", None, 15, "high"),
            ("get", "love", None, 20, "low"),
            ("get", "love", None, 25, "low"),
        ]
    ]
    
    for i, operations in enumerate(test_cases, 1):
        time_map = TimeMap()
        print(f"\nTest case {i}:")
        
        start_time = perf_counter()
        for op in operations:
            if op[0] == "set":
                print(f"\nset({op[1]}, {op[2]}, {op[3]})")
                time_map.set(op[1], op[2], op[3])
                print(f"Store state: {dict(time_map.store)}")
            else:  # get
                result = time_map.get(op[1], op[3])
                expected = op[4]
                print(f"\nget({op[1]}, {op[3]})")
                print(f"Expected: {expected}")
                print(f"Got: {result}")
                print(f"Correct: {'✓' if result == expected else '✗'}")
                
        end_time = perf_counter()
        print(f"\nTime taken: {(end_time - start_time)*1000:.3f}ms")
        print(f"Total operations: {time_map.calls}")

if __name__ == "__main__":
    test_time_map()
