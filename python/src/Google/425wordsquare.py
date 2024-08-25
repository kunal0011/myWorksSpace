class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)

    def search_by_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.words


class Solution:
    def wordSquares(self, words):
        if not words:
            return []

        # Step 1: Build the Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        n = len(words[0])
        results = []

        # Step 2: Backtrack to find all word squares
        def backtrack(step, word_square):
            if step == n:
                results.append(list(word_square))
                return

            # Get the prefix for the next word
            prefix = ''.join([word_square[i][step] for i in range(step)])
            for candidate in trie.search_by_prefix(prefix):
                word_square.append(candidate)
                backtrack(step + 1, word_square)
                word_square.pop()

        for word in words:
            word_square = [word]
            backtrack(1, word_square)

        return results
