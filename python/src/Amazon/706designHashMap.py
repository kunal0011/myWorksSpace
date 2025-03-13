"""
LeetCode 706: Design HashMap

Design a HashMap without using any built-in hash table libraries.
Implement the MyHashMap class:
- MyHashMap() initializes the object with an empty map.
- void put(int key, int value) inserts a (key, value) pair into the HashMap.
- int get(int key) returns the value to which the specified key is mapped, or -1 if no mapping exists.
- void remove(int key) removes the key and its corresponding value if the map contains the mapping.
"""

class MyHashMap:
    def __init__(self):
        self.size = 2069  # Using a prime number for better distribution
        self.buckets = [[] for _ in range(self.size)]
        self.item_count = 0
        self.load_factor_threshold = 0.7

    def _hash(self, key: int) -> int:
        # Better hash function using multiplicative hashing
        hash_value = key * 2654435769  # Using golden ratio multiplier
        return (hash_value & 0xFFFFFFFF) % self.size

    def _resize(self):
        if self.item_count / self.size < self.load_factor_threshold:
            return
        
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.item_count = 0
        
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket[i][1] = value
                return
        
        bucket.append([key, value])
        self.item_count += 1
        self._resize()

    def get(self, key: int) -> int:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for kv in bucket:
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket.pop(i)
                self.item_count -= 1
                return

def test_hash_map():
    print("Testing MyHashMap implementation...")
    
    # Test case 1: Basic operations
    hash_map = MyHashMap()
    operations = [
        ("put", 1, 1),
        ("put", 2, 2),
        ("get", 1),    # should return 1
        ("get", 3),    # should return -1
        ("put", 2, 1), # update value
        ("get", 2),    # should return 1
        ("remove", 2),
        ("get", 2),    # should return -1
    ]
    
    for op in operations:
        if op[0] == "put":
            hash_map.put(op[1], op[2])
            print(f"Put {op[1]}:{op[2]}")
        elif op[0] == "get":
            result = hash_map.get(op[1])
            print(f"Get {op[1]} -> {result}")
        else:  # remove
            hash_map.remove(op[1])
            print(f"Remove {op[1]}")
    
    # Test case 2: Collision handling
    print("\nTesting collision handling...")
    hash_map = MyHashMap()
    for i in range(100):
        hash_map.put(i * hash_map.size, i)  # These keys will have the same hash
        if i < 5:  # Print first few operations
            print(f"Put {i * hash_map.size}:{i}")
    
    for i in range(5):  # Check first few values
        result = hash_map.get(i * hash_map.size)
        print(f"Get {i * hash_map.size} -> {result}")

if __name__ == "__main__":
    test_hash_map()
