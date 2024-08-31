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
