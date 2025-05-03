"""
LeetCode 336 - Palindrome Pairs
Given a list of unique words, return all pairs of distinct indices (i, j) where the concatenation 
of words[i] + words[j] forms a palindrome.

Example 1:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: 
- "abcd" + "dcba" = "abcddcba" is palindrome
- "dcba" + "abcd" = "dcbaabcd" is palindrome
- "s" + "lls" = "slls" is palindrome
- "lls" + "sssll" = "llssssll" is palindrome

Time Complexity: O(n * k^2) where n is number of words and k is average word length
Space Complexity: O(n * k) for the hash map
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_index = -1
        self.palindrome_indices = []

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def is_palindrome(self, word: str, start: int, end: int) -> bool:
        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def insert(self, word: str, index: int) -> None:
        node = self.root
        for i in range(len(word) - 1, -1, -1):
            if self.is_palindrome(word, 0, i):
                node.palindrome_indices.append(index)
            ch = word[i]
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word_index = index
        node.palindrome_indices.append(index)
    
    def search(self, word: str, index: int, pairs: list) -> None:
        node = self.root
        for i in range(len(word)):
            if node.word_index >= 0 and self.is_palindrome(word, i, len(word) - 1):
                pairs.append([index, node.word_index])
            if word[i] not in node.children:
                return
            node = node.children[word[i]]
        
        if node.word_index >= 0 and node.word_index != index:
            pairs.append([index, node.word_index])
        
        for j in node.palindrome_indices:
            if j != index:
                pairs.append([index, j])

    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        pairs = []
        for i, word in enumerate(words):
            self.insert(word, i)
        
        for i, word in enumerate(words):
            self.search(word, i, pairs)
        
        return pairs

# Test driver
def test_palindrome_pairs():
    test_cases = [
        ["abcd", "dcba", "lls", "s", "sssll"],
        ["bat", "tab", "cat"],
        ["a", ""],
        ["a", "abc", "aba", ""]
    ]
    
    expected_outputs = [
        [[0,1], [1,0], [3,2], [2,4]],
        [[0,1], [1,0]],
        [[0,1], [1,0]],
        [[0,3], [3,0], [2,3], [3,2]]
    ]
    
    solution = Solution()
    for i, (test_input, expected) in enumerate(zip(test_cases, expected_outputs)):
        result = solution.palindromePairs(test_input)
        print(f"Test case {i + 1}:")
        print(f"Input: {test_input}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if sorted(result) == sorted(expected) else '✗ Failed'}\n")

if __name__ == "__main__":
    test_palindrome_pairs()
