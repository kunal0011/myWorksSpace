"""
LeetCode 208 - Implement Trie (Prefix Tree)

Problem Statement:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and
retrieve strings. Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Solution Logic:
- TrieNode: Each node contains a dictionary of children nodes and a boolean to mark end of word
- insert(): Add characters one by one, creating new nodes as needed
- search(): Navigate through the trie following the characters, return true only if word exists and is marked as end
- startsWith(): Similar to search but only checks if the prefix path exists
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def test_trie():
    # Test cases
    trie = Trie()
    
    # Test 1: Basic insertion and search
    trie.insert("apple")
    print("Test 1:")
    print("Search 'apple':", trie.search("apple"))    # Expected: True
    print("Search 'app':", trie.search("app"))        # Expected: False
    print("Starts with 'app':", trie.startsWith("app"))  # Expected: True
    
    # Test 2: Empty string
    print("\nTest 2:")
    trie.insert("")
    print("Search empty string:", trie.search(""))    # Expected: True
    
    # Test 3: Multiple words
    print("\nTest 3:")
    trie.insert("apartment")
    trie.insert("app")
    print("Search 'app':", trie.search("app"))       # Expected: True
    print("Search 'apt':", trie.search("apt"))       # Expected: False

if __name__ == "__main__":
    test_trie()
