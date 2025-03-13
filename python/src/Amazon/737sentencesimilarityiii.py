"""
LeetCode 737: Sentence Similarity II

Given two sentences words1, words2 (each represented as an array of strings), and a list 
of similar word pairs pairs, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar, if the similar 
word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "fine" are 
similar, and "fine" and "good" are similar, then "great" and "good" are similar.

Also, a word is always similar with itself. For example, the sentences 
words1 = ["great"], words2 = ["great"] are similar, even if no similarities are provided.
"""

from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(int)  # Added rank for optimization

    def find(self, word: str) -> str:
        if word not in self.parent:
            self.parent[word] = word
        if word != self.parent[word]:
            self.parent[word] = self.find(self.parent[word])
        return self.parent[word]

    def union(self, word1: str, word2: str) -> None:
        root1, root2 = self.find(word1), self.find(word2)
        if root1 != root2:
            # Union by rank
            if self.rank[root1] < self.rank[root2]:
                root1, root2 = root2, root1
            self.parent[root2] = root1
            if self.rank[root1] == self.rank[root2]:
                self.rank[root1] += 1


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        # Early return for empty or mismatched sentences
        if len(words1) != len(words2):
            return False
        if not words1 and not words2:
            return True
        if words1 == words2:
            return True

        uf = UnionFind()
        
        # Build the similarity groups
        for word1, word2 in pairs:
            uf.union(word1, word2)

        # Check if corresponding words are similar
        return all(uf.find(w1) == uf.find(w2) for w1, w2 in zip(words1, words2))


def test_sentence_similarity():
    """Comprehensive test function for sentence similarity"""
    test_cases = [
        # Test case 1: Basic similarity
        (
            ["great", "acting", "skills"],
            ["fine", "drama", "talent"],
            [["great", "fine"], ["acting", "drama"], ["skills", "talent"]],
            True
        ),
        # Test case 2: Transitive similarity
        (
            ["great", "acting"],
            ["good", "drama"],
            [["great", "fine"], ["fine", "good"], ["acting", "drama"]],
            True
        ),
        # Test case 3: Same sentences
        (
            ["great"],
            ["great"],
            [],
            True
        ),
        # Test case 4: Different lengths
        (
            ["great"],
            ["great", "good"],
            [],
            False
        ),
        # Test case 5: No similarity path
        (
            ["great", "acting"],
            ["fine", "drama"],
            [["great", "good"], ["fine", "nice"]],
            False
        ),
        # Test case 6: Empty sentences
        (
            [],
            [],
            [],
            True
        )
    ]

    solution = Solution()
    for i, (words1, words2, pairs, expected) in enumerate(test_cases, 1):
        result = solution.areSentencesSimilarTwo(words1, words2, pairs)
        success = result == expected
        print(f"\nTest case {i}:")
        print(f"Sentence 1: {words1}")
        print(f"Sentence 2: {words2}")
        print(f"Pairs: {pairs}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if success else '✗ Failed'}")


if __name__ == "__main__":
    test_sentence_similarity()
