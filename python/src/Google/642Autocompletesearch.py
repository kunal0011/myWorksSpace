from collections import defaultdict
import heapq
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq_map = defaultdict(int)


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.keyword = ""
        self.cur_node = self.root

        # Build the Trie
        for sentence, time in zip(sentences, times):
            self.add_sentence(sentence, time)

    def add_sentence(self, sentence: str, time: int):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.freq_map[sentence] += time

    def search_top_3(self, node: TrieNode) -> List[str]:
        # Use a heap to get the top 3 frequent sentences
        heap = []
        for sentence, freq in node.freq_map.items():
            heapq.heappush(heap, (-freq, sentence))
            if len(heap) > 3:
                heapq.heappop(heap)

        return [heapq.heappop(heap)[1] for _ in range(len(heap))][::-1]

    def input(self, c: str) -> List[str]:
        if c == '#':
            # End of input, add the keyword to Trie
            self.add_sentence(self.keyword, 1)
            self.keyword = ""
            self.cur_node = self.root
            return []

        self.keyword += c

        if self.cur_node and c in self.cur_node.children:
            self.cur_node = self.cur_node.children[c]
            return self.search_top_3(self.cur_node)
        else:
            self.cur_node = None
            return []


autocompleteSystem = AutocompleteSystem(
    ["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
print(autocompleteSystem.input('i'))
print(autocompleteSystem.input(' '))
print(autocompleteSystem.input('a'))
print(autocompleteSystem.input('#'))
