class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, word):
        if word not in self.parent:
            self.parent[word] = word
        if word != self.parent[word]:
            self.parent[word] = self.find(
                self.parent[word])  # Path compression
        return self.parent[word]

    def union(self, word1, word2):
        root1 = self.find(word1)
        root2 = self.find(word2)
        if root1 != root2:
            self.parent[root2] = root1


class Solution:
    def areSentencesSimilarTwo(self, words1: list[str], words2: list[str], pairs: list[list[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        uf = UnionFind()

        # Union all word pairs
        for word1, word2 in pairs:
            uf.union(word1, word2)

        # Check if each word in words1 is similar to the corresponding word in words2
        for w1, w2 in zip(words1, words2):
            if uf.find(w1) != uf.find(w2):
                return False

        return True


# Test the function
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    words1_1 = ["great", "acting", "skills"]
    words2_1 = ["fine", "drama", "talent"]
    pairs_1 = [["great", "good"], ["fine", "good"],
               ["acting", "drama"], ["skills", "talent"]]
    print(sol.areSentencesSimilarTwo(words1_1, words2_1, pairs_1))  # Output: True

    # Test case 2
    words1_2 = ["great"]
    words2_2 = ["great"]
    pairs_2 = []
    print(sol.areSentencesSimilarTwo(words1_2, words2_2, pairs_2))  # Output: True

    # Test case 3
    words1_3 = ["great"]
    words2_3 = ["fine"]
    pairs_3 = [["great", "good"], ["fine", "good"]]
    print(sol.areSentencesSimilarTwo(words1_3, words2_3, pairs_3))  # Output: True
