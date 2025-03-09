"""
LeetCode 211 - Design Add and Search Words Data Structure

Problem Statement:
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string that matches word previously added to the structure.
  word may contain dots '.' where dots can be matched with any letter.

Solution Logic:
1. Use Trie (Prefix Tree) data structure
2. TrieNode contains children (dictionary) and end_of_word flag
3. addWord: Standard trie insertion
4. search: Use recursive DFS when '.' is encountered
   - For '.' try all possible children
   - For regular char, follow specific path
5. Time: O(N) for add, O(26^m) worst case for search where m is word length
6. Space: O(N) where N is total characters in all words
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def search_in_node(word, node):
            for i, char in enumerate(word):
                if char == '.':
                    for child in node.children.values():
                        if search_in_node(word[i + 1:], child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.is_end_of_word

        return search_in_node(word, self.root)

def test_word_dictionary():
    # Test Case 1: Basic operations
    print("Test Case 1: Basic operations")
    word_dict = WordDictionary()
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")
    print("Search 'pad':", word_dict.search("pad"))  # Expected: False
    print("Search 'bad':", word_dict.search("bad"))  # Expected: True
    print("Search '.ad':", word_dict.search(".ad"))  # Expected: True
    print("Search 'b..':", word_dict.search("b.."))  # Expected: True

    # Test Case 2: Edge cases
    print("\nTest Case 2: Edge cases")
    word_dict2 = WordDictionary()
    word_dict2.addWord("")
    print("Search empty string:", word_dict2.search(""))  # Expected: True
    print("Search '.':", word_dict2.search("."))  # Expected: False

    # Test Case 3: Complex patterns
    print("\nTest Case 3: Complex patterns")
    word_dict3 = WordDictionary()
    word_dict3.addWord("hello")
    print("Search 'h.l.o':", word_dict3.search("h.l.o"))  # Expected: True
    print("Search '..ll.':", word_dict3.search("..ll."))  # Expected: True
    print("Search 'world':", word_dict3.search("world"))  # Expected: False

if __name__ == "__main__":
    test_word_dictionary()
