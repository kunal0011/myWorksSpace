from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val = {}          # Maps key -> value
        self.key_to_freq = {}         # Maps key -> frequency
        # Maps frequency -> keys with that frequency
        self.freq_to_keys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        # Get the value of the key
        val = self.key_to_val[key]
        # Update the frequency of the key
        self.update_freq(key)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            # Update the value and frequency if key exists
            self.key_to_val[key] = value
            self.update_freq(key)
        else:
            if len(self.key_to_val) >= self.capacity:
                # Evict the least frequently used key
                self.evict()
            # Insert new key-value pair
            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = None
            self.min_freq = 1

    def update_freq(self, key: int) -> None:
        # Get the current frequency of the key
        freq = self.key_to_freq[key]
        # Remove the key from the current frequency list
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            # If no more keys have this frequency, remove the frequency
            del self.freq_to_keys[freq]
            # Update min_freq if necessary
            if freq == self.min_freq:
                self.min_freq += 1
        # Increment the key's frequency
        self.key_to_freq[key] += 1
        freq = self.key_to_freq[key]
        # Add the key to the new frequency list
        self.freq_to_keys[freq][key] = None

    def evict(self) -> None:
        # Find the least frequently used key
        key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
        # Remove the key from the cache
        del self.key_to_val[key]
        del self.key_to_freq[key]
        # If no keys are left at this frequency, remove the frequency from freq_to_keys
        if not self.freq_to_keys[self.min_freq]:
            del self.freq_to_keys[self.min_freq]

# Test the LFUCache class


def test_lfu_cache():
    lfu = LFUCache(2)

    lfu.put(1, 1)
    lfu.put(2, 2)

    assert lfu.get(1) == 1, f"Expected 1 but got {lfu.get(1)}"

    lfu.put(3, 3)  # Evicts key 2
    assert lfu.get(2) == -1, f"Expected -1 but got {lfu.get(2)}"
    assert lfu.get(3) == 3, f"Expected 3 but got {lfu.get(3)}"

    lfu.put(4, 4)  # Evicts key 1
    assert lfu.get(1) == -1, f"Expected -1 but got {lfu.get(1)}"
    assert lfu.get(3) == 3, f"Expected 3 but got {lfu.get(3)}"
    assert lfu.get(4) == 4, f"Expected 4 but got {lfu.get(4)}"

    print("All test cases passed!")


# Run the test cases
test_lfu_cache()
