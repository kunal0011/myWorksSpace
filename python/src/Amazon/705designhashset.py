class MyHashSet:

    def __init__(self):
        # Use a large prime number to reduce the chances of collisions
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        # Hash function to calculate bucket index
        return key % self.size

    def add(self, key: int) -> None:
        # Get the bucket index
        bucket_index = self._hash(key)
        # If key is not already in the bucket, add it
        if key not in self.buckets[bucket_index]:
            self.buckets[bucket_index].append(key)

    def remove(self, key: int) -> None:
        # Get the bucket index
        bucket_index = self._hash(key)
        # If key exists in the bucket, remove it
        if key in self.buckets[bucket_index]:
            self.buckets[bucket_index].remove(key)

    def contains(self, key: int) -> bool:
        # Get the bucket index
        bucket_index = self._hash(key)
        # Return True if key is in the bucket, False otherwise
        return key in self.buckets[bucket_index]
