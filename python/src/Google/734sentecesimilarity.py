"""
LeetCode 734: Sentence Similarity

Problem Statement:
Given two sentences words1 and words2 (each represented as an array of strings), and a list of similar word pairs,
determine if two sentences are similar.
For example, "great acting skills" and "fine drama talent" are similar if ("great", "fine"), ("acting","drama"), ("skills","talent") 
are in the similar word pairs.
Note that the similarity relation is not transitive.

Logic:
1. First check if sentences have same length (if not, return False)
2. Create a set of similar pairs for O(1) lookup
   - Add both directions (a,b) and (b,a) since similarity is bidirectional
3. Compare words at each position:
   - Words are similar if they are identical or form a similar pair
   - If any pair of words is not similar, return False
4. Return True if all checks pass

Time Complexity: O(N + P) where N is length of sentences and P is number of pairs
Space Complexity: O(P) where P is number of pairs for storing similar pairs set
"""


class Solution:
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        # If the sentences have different lengths, they can't be similar
        if len(sentence1) != len(sentence2):
            return False

        # Create a set for similarity pairs for quick lookup
        similar_set = set()
        for pair in similarPairs:
            similar_set.add((pair[0], pair[1]))
            similar_set.add((pair[1], pair[0]))  # Add both directions

        # Check each word in both sentences
        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2 and (word1, word2) not in similar_set:
                return False

        return True


def test_sentence_similarity():
    solution = Solution()

    # Test case 1: Basic similarity
    words1 = ["great", "acting", "skills"]
    words2 = ["fine", "drama", "talent"]
    pairs = [["great", "fine"], ["acting", "drama"], ["skills", "talent"]]
    assert solution.areSentencesSimilar(words1, words2, pairs) == True
    print(f"Test case 1 passed: {words1} is similar to {words2}")

    # Test case 2: Different lengths
    words1 = ["great"]
    words2 = ["great", "fine"]
    pairs = [["great", "fine"]]
    assert solution.areSentencesSimilar(words1, words2, pairs) == False
    print(f"Test case 2 passed: Different lengths detected")

    # Test case 3: Same words, no pairs needed
    words1 = ["great", "skills"]
    words2 = ["great", "skills"]
    pairs = []
    assert solution.areSentencesSimilar(words1, words2, pairs) == True
    print(f"Test case 3 passed: Identical words")

    # Test case 4: No similar pairs found
    words1 = ["great", "acting"]
    words2 = ["fine", "drama"]
    pairs = [["great", "good"]]  # No matching pair
    assert solution.areSentencesSimilar(words1, words2, pairs) == False
    print(f"Test case 4 passed: No similar pairs")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_sentence_similarity()
