from collections import defaultdict, deque


class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores frequency of sentences at each node
        self.sentence_freq = defaultdict(int)


class AutocompleteSystem:
    def __init__(self, sentences, times):
        # Initialize the trie root and current state variables
        self.root = TrieNode()
        self.current_node = self.root
        self.current_search = ""  # To keep track of the ongoing search
        # Store frequency of all sentences
        self.sentence_freq = defaultdict(int)

        # Insert all the initial sentences into the Trie
        for i, sentence in enumerate(sentences):
            self.sentence_freq[sentence] = times[i]
            self.add_sentence_to_trie(sentence)

    def add_sentence_to_trie(self, sentence):
        """Inserts a sentence into the trie and updates the frequency at each node"""
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentence_freq[sentence] = self.sentence_freq[sentence]

    def input(self, c: str):
        if c == '#':
            # End of the input, update the system with the current search query
            self.sentence_freq[self.current_search] += 1
            self.add_sentence_to_trie(self.current_search)
            self.current_search = ""
            self.current_node = self.root
            return []

        # Add character to the current search query
        self.current_search += c

        # Traverse the trie based on the current input
        if self.current_node and c in self.current_node.children:
            self.current_node = self.current_node.children[c]
        else:
            self.current_node = None  # No matches available

        # If no valid node is found, return an empty list
        if self.current_node is None:
            return []

        # Return the top 3 sentences from the current node
        return self.get_top_3_sentences(self.current_node)

    def get_top_3_sentences(self, node: TrieNode):
        """Get the top 3 sentences based on frequency and lexicographical order"""
        # Sort sentences first by frequency, then lexicographically
        sorted_sentences = sorted(
            node.sentence_freq.keys(),
            key=lambda x: (-node.sentence_freq[x], x)
        )
        return sorted_sentences[:3]

# Test cases


def test_autocomplete_system():
    sentences = ["i love you", "island", "iroman", "i love leetcode"]
    times = [5, 3, 2, 2]

    system = AutocompleteSystem(sentences, times)

    # Testing input character by character
    assert system.input('i') == ["i love you", "island",
                                 "i love leetcode"], f"Test failed at 'i'"
    assert system.input(' ') == ["i love you",
                                 "i love leetcode"], f"Test failed at ' '"
    assert system.input('a') == [], f"Test failed at 'a'"
    assert system.input('#') == [], f"Test failed at '#' for first query"

    # Testing after adding new query
    assert system.input('i') == ["i love you", "island",
                                 "i love leetcode"], f"Test failed at 'i'"
    assert system.input(' ') == [
        "i love you", "i love leetcode"], f"Test failed at ' ' after adding 'i a' query"
    assert system.input('l') == ["i love you",
                                 "i love leetcode"], f"Test failed at 'l'"
    assert system.input('o') == ["i love you",
                                 "i love leetcode"], f"Test failed at 'o'"
    assert system.input('#') == [], f"Test failed at '#' for second query"

    print("All test cases passed!")


# Run the test cases
test_autocomplete_system()
