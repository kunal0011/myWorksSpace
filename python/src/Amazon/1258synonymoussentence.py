from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, word):
        if word not in self.parent:
            self.parent[word] = word
        if self.parent[word] != word:
            self.parent[word] = self.find(self.parent[word])
        return self.parent[word]

    def union(self, word1, word2):
        root1 = self.find(word1)
        root2 = self.find(word2)
        if root1 != root2:
            self.parent[root1] = root2


class Solution:
    def generateSentences(self, synonyms, text):
        # Step 1: Use Union-Find to group synonyms
        uf = UnionFind()

        for word1, word2 in synonyms:
            uf.union(word1, word2)

        # Step 2: Create a mapping from parent to all words in the same group
        groups = defaultdict(list)
        for word in uf.parent:
            parent = uf.find(word)
            groups[parent].append(word)

        # Sort the words in each group for lexicographical order
        for parent in groups:
            groups[parent].sort()

        # Step 3: Backtracking to generate all possible sentences
        def backtrack(index, current_sentence):
            if index == len(words):
                result.append(" ".join(current_sentence))
                return

            word = words[index]
            if word in uf.parent:
                parent = uf.find(word)
                for synonym in groups[parent]:
                    backtrack(index + 1, current_sentence + [synonym])
            else:
                backtrack(index + 1, current_sentence + [word])

        # Split the sentence into words
        words = text.split()
        result = []
        backtrack(0, [])

        return result
