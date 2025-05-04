"""
LeetCode 642 - Design Search Autocomplete System

Problem Statement:
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and array times of the same size. sentences[i] is a previously typed sentence, and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:
- The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
- The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
- If less than 3 hot sentences exist, return as many as you can.
- When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

Logic:
1. Use a Trie data structure to store sentences and their frequencies
2. Each TrieNode contains:
   - children nodes (dictionary)
   - is_end flag to mark end of sentence
   - hot_degree to store frequency
   - sentence to store complete sentence at leaf nodes
3. For each input character:
   - Track current input string
   - Search Trie for matching prefixes
   - Sort matches by hot degree and lexicographical order
   - Return top 3 matches

Time Complexity:
- Constructor: O(n*k) where n is number of sentences, k is average length
- Input: O(p + q*log(q)) where p is current prefix length, q is number of matching sentences

Space Complexity: O(n*k) for Trie storage
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.hot_degree = 0
        self.sentence = ""


class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]):
        self.root = TrieNode()
        self.curr_input = ""

        # Build Trie with initial sentences
        for sentence, time in zip(sentences, times):
            self._insert(sentence, time)

    def _insert(self, sentence: str, hot_degree: int) -> None:
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
        node.sentence = sentence
        node.hot_degree += hot_degree

    def _search(self, prefix: str) -> list[tuple[str, int]]:
        node = self.root
        result = []

        # Traverse to prefix node
        for c in prefix:
            if c not in node.children:
                return result
            node = node.children[c]

        # DFS to collect all sentences with this prefix
        def dfs(curr_node):
            if curr_node.is_end:
                result.append((curr_node.sentence, curr_node.hot_degree))
            for child in curr_node.children.values():
                dfs(child)

        dfs(node)
        return result

    def input(self, c: str) -> list[str]:
        if c == '#':
            self._insert(self.curr_input, 1)
            self.curr_input = ""
            return []

        self.curr_input += c
        matches = self._search(self.curr_input)

        # Sort by hot degree (descending) and lexicographical order
        matches.sort(key=lambda x: (-x[1], x[0]))

        # Return top 3 matches
        return [sentence for sentence, _ in matches[:3]]


# Test driver
def test_autocomplete_system():
    print("Test Case 1:")
    sentences = ["i love you", "island", "iroman", "i love leetcode"]
    times = [5, 3, 2, 2]
    auto = AutocompleteSystem(sentences, times)

    test_inputs = [
        'i', ' ', 'a', '#',
        'i', ' ', 'l', 'o', 'v', 'e', ' ', 'y', 'o', 'u', '#'
    ]

    print("Initial sentences:", sentences)
    print("Initial frequencies:", times)
    print("\nTesting input sequence:")

    for char in test_inputs:
        result = auto.input(char)
        if char != '#':
            print(f"Input '{char}' -> Suggestions: {result}")
        else:
            print("Input '#' -> Sentence completed")

    print("\nTest Case 2:")
    auto2 = AutocompleteSystem(["abc", "abbc", "a"], [3, 2, 1])

    test_inputs2 = ['a', 'b', '#']

    for char in test_inputs2:
        result = auto2.input(char)
        if char != '#':
            print(f"Input '{char}' -> Suggestions: {result}")
        else:
            print("Input '#' -> Sentence completed")


if __name__ == "__main__":
    test_autocomplete_system()
