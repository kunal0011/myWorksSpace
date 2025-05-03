"""
LeetCode 425: Word Squares

Problem Statement:
Given an array of unique strings words, return all the word squares you can build from words.
A sequence of strings forms a valid word square if the kth row and column read the exact 
same string, where 0 ≤ k < max(numRows, numCols).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because 
each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 5
- All words[i] have the same length
- words[i] consists of only lowercase English letters
- All words[i] are unique
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []  # Store words that pass through this node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, word_index: int) -> None:
        node = self.root
        # Store the word index at each prefix
        node.words.append(word_index)
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word_index)

    def get_words_with_prefix(self, prefix: str) -> list[int]:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.words


def wordSquares(words: list[str]) -> list[list[str]]:
    if not words:
        return []

    # Build trie for efficient prefix lookup
    trie = Trie()
    for i, word in enumerate(words):
        trie.insert(word, i)

    n = len(words[0])  # All words have same length
    result = []

    def backtrack(square: list[str]) -> None:
        if len(square) == n:
            result.append(square[:])
            return

        # Get the prefix we need to match for the next word
        pos = len(square)
        prefix = ''.join(word[pos] for word in square)

        # Get all words that have this prefix
        candidates = trie.get_words_with_prefix(prefix)
        for word_idx in candidates:
            square.append(words[word_idx])
            backtrack(square)
            square.pop()

    # Try each word as the first word of the square
    for i, word in enumerate(words):
        backtrack([word])

    return result

# Test driver


def run_tests():
    test_cases = [
        {
            "words": ["area", "lead", "wall", "lady", "ball"],
            "expected": [
                ["ball", "area", "lead", "lady"],
                ["wall", "area", "lead", "lady"]
            ],
            "explanation": "Two valid word squares possible"
        },
        {
            "words": ["abat", "baba", "atan", "atal"],
            "expected": [
                ["abat", "baba", "atan", "tana"],
                ["abat", "baba", "atal", "tala"]
            ],
            "explanation": "Two valid word squares possible"
        },
        {
            "words": ["a"],
            "expected": [["a"]],
            "explanation": "Single character word square"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = wordSquares(test["words"])
        # Sort results for consistent comparison
        result = sorted([sorted(sq) for sq in result])
        expected = sorted([sorted(sq) for sq in test["expected"]])
        status = "PASSED" if result == expected else "FAILED"

        print(f"Test {i}: {status}")
        print(f"Input words: {test['words']}")
        print(f"Expected word squares:")
        for square in test["expected"]:
            print("\n".join(square))
            print()
        print(f"Got word squares:")
        for square in result:
            print("\n".join(square))
            print()
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Word Squares problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Trie-based Approach:
   - Build a trie to efficiently find words with given prefixes
   - Store word indices at each node for quick lookup
   - Each node maintains list of all words that share the prefix

2. Backtracking Strategy:
   - Start with each word as first word in square
   - For each subsequent position:
     * Calculate required prefix from existing words
     * Find all words with that prefix using trie
     * Try each candidate and backtrack

3. Key Optimizations:
   - Use trie for O(L) prefix lookups where L is word length
   - Store word indices instead of full words in trie
   - Early termination when no words match required prefix

Time Complexity: O(N*L) for trie construction + O(N*26^L) for backtracking
where N is number of words and L is word length
Space Complexity: O(N*L) for trie storage
"""
