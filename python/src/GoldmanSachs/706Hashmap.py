class MyHashMap:

    def __init__(self):
        # Initialize the hash map with a fixed size and use a list of lists (buckets) to handle collisions.
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        # Hash function to get the index for the key
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # Check if key exists and update the value if it does
        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket[i][1] = value
                return

        # If key does not exist, append the new (key, value) pair
        bucket.append([key, value])

    def get(self, key: int) -> int:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # Traverse the bucket to find the key
        for kv in bucket:
            if kv[0] == key:
                return kv[1]

        # Return -1 if key is not found
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # Traverse the bucket to find and remove the key
        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket.pop(i)
                return
