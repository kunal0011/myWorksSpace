"""
LeetCode 642: Design Search Autocomplete System

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and an integer array times of the same length. For each sentence, times[i] represents the number 
of times this sentence was previously typed. Initially, you need to output top 3 historical hot sentences that have the same prefix as 
the part of the sentence already typed.

Rules:
1. The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
2. The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). 
   If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
3. If less than 3 hot sentences exist, return as many as you can.
4. When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.frequency = 0
        self.sentence = ""

class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]):
        self.root = TrieNode()
        self.current_node = self.root
        self.current_input = ""
        
        # Initialize the system with given sentences and frequencies
        for sentence, freq in zip(sentences, times):
            self._insert(sentence, freq)
    
    def _insert(self, sentence: str, freq: int) -> None:
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.frequency = freq
        node.sentence = sentence
    
    def _find_all_sentences(self, node: TrieNode) -> list[tuple[int, str]]:
        result = []
        
        def dfs(current: TrieNode):
            if current.is_end:
                result.append((-current.frequency, current.sentence))
            for child in current.children.values():
                dfs(child)
        
        dfs(node)
        return result
    
    def input(self, c: str) -> list[str]:
        if c == '#':
            # End of sentence, add it to the system
            self._insert(self.current_input, 1)
            self.current_input = ""
            self.current_node = self.root
            return []
        
        self.current_input += c
        
        # Move to the next node
        if self.current_node and c in self.current_node.children:
            self.current_node = self.current_node.children[c]
            # Find all sentences with current prefix
            suggestions = self._find_all_sentences(self.current_node)
            # Sort by frequency (negated for descending) and then by sentence
            suggestions.sort()
            # Return top 3 sentences
            return [sentence for _, sentence in suggestions[:3]]
        else:
            self.current_node = None
            return []


def test_autocomplete_system():
    """Test driver for AutocompleteSystem"""
    print("Test 1: Basic functionality")
    sentences = ["i love you", "island", "iroman", "i love leetcode"]
    times = [5, 3, 2, 2]
    auto = AutocompleteSystem(sentences, times)
    
    test_cases = [
        ('i', ["i love you", "island", "i love leetcode"]),
        (' ', ["i love you", "i love leetcode"]),
        ('a', ["i love you", "i love leetcode"]),
        ('#', []),
        ('i', ["i love you", "island", "i love leetcode"]),
        ('s', ["island"]),
        ('l', ["island"]),
        ('a', ["island"]),
        ('n', ["island"]),
        ('d', ["island"]),
        ('#', [])
    ]
    
    for i, (input_char, expected) in enumerate(test_cases, 1):
        result = auto.input(input_char)
        status = "✓" if result == expected else "✗"
        print(f"\nTest {i}: {status}")
        print(f"Input: '{input_char}'")
        print(f"Expected: {expected}")
        print(f"Got: {result}")

if __name__ == "__main__":
    test_autocomplete_system()
